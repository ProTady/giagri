"""Lógica de áreas de trabajo del personal."""
from __future__ import annotations
from dataclasses import dataclass
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class AreaTrabajo:
    id_area: int
    nombre: str
    descripcion: str
    activo: bool


class ClAreaTrabajo:
    def listar(self, id_fundo: int, solo_activos: bool = True) -> list[AreaTrabajo]:
        sql = ("SELECT id_area, nombre, COALESCE(descripcion,''), activo "
               "  FROM personal.area_trabajo WHERE id_fundo = %s ")
        if solo_activos:
            sql += " AND activo = TRUE "
        sql += " ORDER BY nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return [AreaTrabajo(*r) for r in cur.fetchall()]
