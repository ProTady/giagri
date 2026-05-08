"""Lógica de labores (con bono opcional por hora)."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Labor:
    id_labor: int
    id_actividad: Optional[int]
    actividad_nombre: str
    codigo: str
    nombre: str
    descripcion: str
    bono_por_hora: float
    activo: bool


class ClLabor:

    def listar(self, id_fundo: int,
               id_actividad: Optional[int] = None,
               solo_activos: bool = True) -> list[Labor]:
        sql = """
            SELECT l.id_labor, l.id_actividad, COALESCE(a.nombre,''),
                   COALESCE(l.codigo,''), l.nombre, COALESCE(l.descripcion,''),
                   l.bono_por_hora, l.activo
              FROM personal.labor l
              LEFT JOIN personal.actividad a ON a.id_actividad = l.id_actividad
             WHERE l.id_fundo = %s
        """
        params: list = [id_fundo]
        if id_actividad is not None:
            sql += " AND l.id_actividad = %s "
            params.append(id_actividad)
        if solo_activos:
            sql += " AND l.activo = TRUE "
        sql += " ORDER BY a.nombre, l.nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return [Labor(
                id_labor=r[0], id_actividad=r[1], actividad_nombre=r[2],
                codigo=r[3], nombre=r[4], descripcion=r[5],
                bono_por_hora=float(r[6]), activo=r[7],
            ) for r in cur.fetchall()]

    def existe(self, id_fundo: int, nombre: str,
               excluir_id: int | None = None) -> bool:
        sql = ("SELECT 1 FROM personal.labor "
               "WHERE id_fundo=%s AND LOWER(nombre)=LOWER(%s) ")
        params: list = [id_fundo, nombre]
        if excluir_id is not None:
            sql += " AND id_labor <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, id_fundo: int, id_actividad: Optional[int],
              nombre: str, codigo: str = "", descripcion: str = "",
              bono_por_hora: float = 0.0) -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre de la labor es obligatorio.")
        if self.existe(id_fundo, nombre):
            raise ValueError(f"Ya existe la labor '{nombre}'.")
        if bono_por_hora < 0:
            raise ValueError("El bono no puede ser negativo.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO personal.labor "
                "(id_fundo, id_actividad, codigo, nombre, descripcion, bono_por_hora) "
                "VALUES (%s,%s,%s,%s,%s,%s) RETURNING id_labor",
                (id_fundo, id_actividad, codigo.strip() or None,
                 nombre, descripcion.strip() or None, bono_por_hora),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_labor: int, id_fundo: int,
                   id_actividad: Optional[int], nombre: str,
                   codigo: str, descripcion: str,
                   bono_por_hora: float, activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe(id_fundo, nombre, excluir_id=id_labor):
            raise ValueError(f"Ya existe la labor '{nombre}'.")
        if bono_por_hora < 0:
            raise ValueError("El bono no puede ser negativo.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                """
                UPDATE personal.labor SET
                    id_actividad=%s, codigo=%s, nombre=%s,
                    descripcion=%s, bono_por_hora=%s, activo=%s
                WHERE id_labor=%s
                """,
                (id_actividad, codigo.strip() or None, nombre,
                 descripcion.strip() or None, bono_por_hora, activo, id_labor),
            )
            conn.commit()

    def eliminar(self, id_labor: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM personal.tareo WHERE id_labor=%s",
                (id_labor,),
            )
            if cur.fetchone()[0]:
                raise ValueError(
                    "No se puede eliminar: la labor tiene tareos registrados. "
                    "Considera desactivarla."
                )
            cur.execute(
                "DELETE FROM personal.labor WHERE id_labor=%s",
                (id_labor,),
            )
            conn.commit()
