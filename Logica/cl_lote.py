"""Lógica de lotes (agricola.lote)."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class LoteFila:
    id_lote: int
    codigo: str
    nombre: str
    cultivo: str
    variedad: str
    patron: str
    hectareas: float
    total_plantas: Optional[int]
    fecha_siembra: Optional[date]
    sistema_riego: str
    estado: str


class ClLote:

    def listar(self, id_fundo: int, filtro: str = "",
               estado: str = "todos") -> list[LoteFila]:
        sql = """
            SELECT l.id_lote, l.codigo, l.nombre,
                   COALESCE(t.nombre,''), COALESCE(v.nombre,''),
                   COALESCE(p.nombre,''),
                   l.hectareas, l.total_plantas, l.fecha_siembra,
                   COALESCE(l.sistema_riego,''), l.estado
              FROM agricola.lote l
              LEFT JOIN agricola.tipo_cultivo t ON t.id_tipo_cultivo = l.id_tipo_cultivo
              LEFT JOIN agricola.variedad     v ON v.id_variedad     = l.id_variedad
              LEFT JOIN agricola.patron       p ON p.id_patron       = l.id_patron
             WHERE l.id_fundo = %s
        """
        params: list = [id_fundo]
        if filtro:
            sql += " AND (l.codigo ILIKE %s OR l.nombre ILIKE %s) "
            patron = f"%{filtro}%"
            params += [patron, patron]
        if estado != "todos":
            sql += " AND l.estado = %s "
            params.append(estado)
        sql += " ORDER BY l.codigo "

        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            filas = []
            for r in cur.fetchall():
                ha = float(r[6]) if r[6] is not None else 0.0
                filas.append(LoteFila(
                    r[0], r[1], r[2], r[3], r[4], r[5],
                    ha, r[7], r[8], r[9], r[10],
                ))
            return filas

    def obtener(self, id_lote: int) -> Optional[dict]:
        sql = """
            SELECT id_lote, id_fundo, codigo, nombre,
                   id_tipo_cultivo, id_variedad, id_patron,
                   hectareas, fecha_siembra, fecha_inicio_produccion,
                   densidad_plantas, total_plantas,
                   distancia_entre_plantas, distancia_entre_filas,
                   COALESCE(sistema_riego,''), estado,
                   COALESCE(observaciones,'')
              FROM agricola.lote WHERE id_lote = %s
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_lote,))
            r = cur.fetchone()
        if r is None:
            return None
        campos = ["id_lote","id_fundo","codigo","nombre",
                  "id_tipo_cultivo","id_variedad","id_patron",
                  "hectareas","fecha_siembra","fecha_inicio_produccion",
                  "densidad_plantas","total_plantas",
                  "distancia_entre_plantas","distancia_entre_filas",
                  "sistema_riego","estado","observaciones"]
        return dict(zip(campos, r))

    def existe_codigo(self, id_fundo: int, codigo: str,
                      excluir_id: Optional[int] = None) -> bool:
        sql = ("SELECT 1 FROM agricola.lote "
               "WHERE id_fundo=%s AND LOWER(codigo)=LOWER(%s) ")
        params: list = [id_fundo, codigo]
        if excluir_id is not None:
            sql += " AND id_lote <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, datos: dict) -> int:
        self._validar(datos)
        if self.existe_codigo(datos["id_fundo"], datos["codigo"]):
            raise ValueError(f"Ya existe un lote con código '{datos['codigo']}'.")
        sql = """
            INSERT INTO agricola.lote
                (id_fundo, codigo, nombre, id_tipo_cultivo, id_variedad, id_patron,
                 hectareas, fecha_siembra, fecha_inicio_produccion,
                 densidad_plantas, total_plantas,
                 distancia_entre_plantas, distancia_entre_filas,
                 sistema_riego, estado, observaciones)
            VALUES (%(id_fundo)s, %(codigo)s, %(nombre)s,
                    %(id_tipo_cultivo)s, %(id_variedad)s, %(id_patron)s,
                    %(hectareas)s, %(fecha_siembra)s, %(fecha_inicio_produccion)s,
                    %(densidad_plantas)s, %(total_plantas)s,
                    %(distancia_entre_plantas)s, %(distancia_entre_filas)s,
                    %(sistema_riego)s, %(estado)s, %(observaciones)s)
            RETURNING id_lote
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, self._normalizar(datos))
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_lote: int, datos: dict) -> None:
        self._validar(datos)
        if self.existe_codigo(datos["id_fundo"], datos["codigo"], excluir_id=id_lote):
            raise ValueError(f"Ya existe un lote con código '{datos['codigo']}'.")
        sql = """
            UPDATE agricola.lote SET
                codigo=%(codigo)s, nombre=%(nombre)s,
                id_tipo_cultivo=%(id_tipo_cultivo)s,
                id_variedad=%(id_variedad)s,
                id_patron=%(id_patron)s,
                hectareas=%(hectareas)s,
                fecha_siembra=%(fecha_siembra)s,
                fecha_inicio_produccion=%(fecha_inicio_produccion)s,
                densidad_plantas=%(densidad_plantas)s,
                total_plantas=%(total_plantas)s,
                distancia_entre_plantas=%(distancia_entre_plantas)s,
                distancia_entre_filas=%(distancia_entre_filas)s,
                sistema_riego=%(sistema_riego)s,
                estado=%(estado)s,
                observaciones=%(observaciones)s,
                actualizado_en=NOW()
            WHERE id_lote=%(id_lote)s
        """
        params = self._normalizar(datos)
        params["id_lote"] = id_lote
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            conn.commit()

    def eliminar(self, id_lote: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM agricola.lote WHERE id_lote=%s", (id_lote,))
            conn.commit()

    # ------------------------------------------------------------------
    @staticmethod
    def _validar(d: dict) -> None:
        if not d.get("codigo"):
            raise ValueError("El código es obligatorio.")
        if not d.get("nombre"):
            raise ValueError("El nombre es obligatorio.")
        try:
            ha = float(d.get("hectareas") or 0)
            if ha < 0:
                raise ValueError("Las hectáreas no pueden ser negativas.")
        except (TypeError, ValueError):
            raise ValueError("Hectáreas inválidas.")

    @staticmethod
    def _normalizar(d: dict) -> dict:
        out = dict(d)
        for k in ("id_tipo_cultivo","id_variedad","id_patron",
                  "fecha_siembra","fecha_inicio_produccion",
                  "densidad_plantas","total_plantas",
                  "distancia_entre_plantas","distancia_entre_filas",
                  "sistema_riego","observaciones"):
            if out.get(k) in ("", None):
                out[k] = None
        return out
