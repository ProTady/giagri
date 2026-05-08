"""Lógica del tareo diario (registro de horas trabajadas por empleado)."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class TareoFila:
    id_tareo: int
    id_empleado: int
    empleado_codigo: str
    empleado_nombre: str
    id_cargo: Optional[int]
    cargo_nombre: str
    id_lote: Optional[int]
    lote_codigo: str
    id_labor: Optional[int]
    labor_nombre: str
    id_actividad: Optional[int]
    actividad_nombre: str
    horas_manana: float
    horas_tarde: float
    horas_extras: float
    horas_total: float
    bono_por_hora: float        # snapshot de la labor (para cálculo)
    bono_total: float            # bono_por_hora × horas_total
    comentario: str


@dataclass
class ResumenEmpleado:
    id_empleado: int
    codigo: str
    nombre: str
    dias_trabajados: int
    horas_normales: float
    horas_extras: float
    horas_total: float
    bono_total: float


class ClTareo:

    # ============================================================
    # CRUD básico
    # ============================================================
    def listar_por_fecha(self, id_fundo: int, fecha: date) -> list[TareoFila]:
        return self._listar_rango(id_fundo, fecha, fecha)

    def listar_rango(self, id_fundo: int, desde: date,
                     hasta: date) -> list[TareoFila]:
        return self._listar_rango(id_fundo, desde, hasta)

    def _listar_rango(self, id_fundo: int, desde: date,
                      hasta: date) -> list[TareoFila]:
        sql = """
            SELECT t.id_tareo, t.id_empleado, e.codigo,
                   e.apellido_paterno || ' ' || COALESCE(e.apellido_materno,'') ||
                       ' ' || e.nombres,
                   t.id_cargo, COALESCE(c.nombre,''),
                   t.id_lote, COALESCE(lo.codigo,''),
                   t.id_labor, COALESCE(la.nombre,''),
                   t.id_actividad, COALESCE(ac.nombre,''),
                   t.horas_manana, t.horas_tarde, t.horas_extras, t.horas_total,
                   COALESCE(la.bono_por_hora, 0),
                   COALESCE(t.comentario, '')
              FROM personal.tareo t
              JOIN personal.empleado e ON e.id_empleado = t.id_empleado
              LEFT JOIN personal.cargo     c  ON c.id_cargo     = t.id_cargo
              LEFT JOIN agricola.lote      lo ON lo.id_lote     = t.id_lote
              LEFT JOIN personal.labor     la ON la.id_labor    = t.id_labor
              LEFT JOIN personal.actividad ac ON ac.id_actividad = t.id_actividad
             WHERE t.id_fundo = %s
               AND t.fecha BETWEEN %s AND %s
             ORDER BY t.fecha, e.apellido_paterno, e.nombres
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo, desde, hasta))
            filas = []
            for r in cur.fetchall():
                horas_total = float(r[15])
                bono_h = float(r[16])
                filas.append(TareoFila(
                    id_tareo=r[0], id_empleado=r[1],
                    empleado_codigo=r[2], empleado_nombre=r[3].strip(),
                    id_cargo=r[4], cargo_nombre=r[5],
                    id_lote=r[6], lote_codigo=r[7],
                    id_labor=r[8], labor_nombre=r[9],
                    id_actividad=r[10], actividad_nombre=r[11],
                    horas_manana=float(r[12]), horas_tarde=float(r[13]),
                    horas_extras=float(r[14]), horas_total=horas_total,
                    bono_por_hora=bono_h,
                    bono_total=round(bono_h * horas_total, 2),
                    comentario=r[17],
                ))
            return filas

    def crear(self, datos: dict) -> int:
        self._validar(datos)
        sql = """
            INSERT INTO personal.tareo
                (id_fundo, id_empleado, fecha, id_cargo, id_lote,
                 id_labor, id_actividad,
                 horas_manana, horas_tarde, horas_extras,
                 comentario, creado_por)
            VALUES (%(id_fundo)s, %(id_empleado)s, %(fecha)s,
                    %(id_cargo)s, %(id_lote)s,
                    %(id_labor)s, %(id_actividad)s,
                    %(horas_manana)s, %(horas_tarde)s, %(horas_extras)s,
                    %(comentario)s, %(creado_por)s)
            RETURNING id_tareo
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, self._normalizar(datos))
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def crear_masivo(self, filas: list[dict]) -> int:
        """Crea N filas en una transacción. Devuelve cantidad creada.

        Cada fila es un dict con las mismas claves de crear().
        """
        if not filas:
            return 0
        for f in filas:
            self._validar(f)
        sql = """
            INSERT INTO personal.tareo
                (id_fundo, id_empleado, fecha, id_cargo, id_lote,
                 id_labor, id_actividad,
                 horas_manana, horas_tarde, horas_extras,
                 comentario, creado_por)
            VALUES (%(id_fundo)s, %(id_empleado)s, %(fecha)s,
                    %(id_cargo)s, %(id_lote)s,
                    %(id_labor)s, %(id_actividad)s,
                    %(horas_manana)s, %(horas_tarde)s, %(horas_extras)s,
                    %(comentario)s, %(creado_por)s)
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            for f in filas:
                cur.execute(sql, self._normalizar(f))
            conn.commit()
        return len(filas)

    def actualizar(self, id_tareo: int, datos: dict) -> None:
        self._validar(datos)
        sql = """
            UPDATE personal.tareo SET
                id_empleado=%(id_empleado)s, fecha=%(fecha)s,
                id_cargo=%(id_cargo)s, id_lote=%(id_lote)s,
                id_labor=%(id_labor)s, id_actividad=%(id_actividad)s,
                horas_manana=%(horas_manana)s,
                horas_tarde=%(horas_tarde)s,
                horas_extras=%(horas_extras)s,
                comentario=%(comentario)s,
                actualizado_en=NOW()
            WHERE id_tareo=%(id_tareo)s
        """
        params = self._normalizar(datos)
        params["id_tareo"] = id_tareo
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            conn.commit()

    def eliminar(self, id_tareo: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM personal.tareo WHERE id_tareo=%s",
                        (id_tareo,))
            conn.commit()

    # ============================================================
    # Resúmenes / reportes
    # ============================================================
    def resumen_por_empleado(self, id_fundo: int, desde: date,
                             hasta: date) -> list[ResumenEmpleado]:
        sql = """
            SELECT e.id_empleado, e.codigo,
                   e.apellido_paterno || ' ' || COALESCE(e.apellido_materno,'') ||
                       ' ' || e.nombres,
                   COUNT(DISTINCT t.fecha),
                   SUM(t.horas_manana + t.horas_tarde),
                   SUM(t.horas_extras),
                   SUM(t.horas_total),
                   SUM(t.horas_total * COALESCE(la.bono_por_hora, 0))
              FROM personal.tareo t
              JOIN personal.empleado e ON e.id_empleado = t.id_empleado
              LEFT JOIN personal.labor la ON la.id_labor = t.id_labor
             WHERE t.id_fundo = %s
               AND t.fecha BETWEEN %s AND %s
             GROUP BY e.id_empleado, e.codigo,
                      e.apellido_paterno, e.apellido_materno, e.nombres
             ORDER BY e.apellido_paterno, e.nombres
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo, desde, hasta))
            return [ResumenEmpleado(
                id_empleado=r[0], codigo=r[1], nombre=r[2].strip(),
                dias_trabajados=int(r[3]),
                horas_normales=float(r[4] or 0),
                horas_extras=float(r[5] or 0),
                horas_total=float(r[6] or 0),
                bono_total=float(r[7] or 0),
            ) for r in cur.fetchall()]

    def total_horas_por_lote(self, id_fundo: int, desde: date,
                             hasta: date) -> list[tuple]:
        sql = """
            SELECT COALESCE(lo.codigo, '(sin lote)'),
                   COALESCE(lo.nombre, ''),
                   SUM(t.horas_total)
              FROM personal.tareo t
              LEFT JOIN agricola.lote lo ON lo.id_lote = t.id_lote
             WHERE t.id_fundo = %s
               AND t.fecha BETWEEN %s AND %s
             GROUP BY lo.id_lote, lo.codigo, lo.nombre
             ORDER BY 1
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo, desde, hasta))
            return cur.fetchall()

    # ============================================================
    @staticmethod
    def _validar(d: dict) -> None:
        if not d.get("id_empleado"):
            raise ValueError("Selecciona un empleado.")
        if not d.get("fecha"):
            raise ValueError("La fecha es obligatoria.")
        for k in ("horas_manana", "horas_tarde", "horas_extras"):
            v = d.get(k) or 0
            try:
                v = float(v)
            except (TypeError, ValueError):
                raise ValueError(f"Horas inválidas en {k}.")
            if v < 0:
                raise ValueError(f"Horas no pueden ser negativas ({k}).")
            if v > 24:
                raise ValueError(f"Horas exceden 24 ({k}).")

    @staticmethod
    def _normalizar(d: dict) -> dict:
        out = dict(d)
        for k in ("id_cargo", "id_lote", "id_labor", "id_actividad"):
            if out.get(k) in ("", None, 0):
                out[k] = None
        for k in ("horas_manana", "horas_tarde", "horas_extras"):
            out[k] = float(out.get(k) or 0)
        out["comentario"] = (out.get("comentario") or "").strip() or None
        return out
