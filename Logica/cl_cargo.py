"""Lógica de cargos del personal."""
from __future__ import annotations
from dataclasses import dataclass
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Cargo:
    id_cargo: int
    nombre: str
    descripcion: str
    activo: bool


class ClCargo:
    def listar(self, id_fundo: int, solo_activos: bool = True) -> list[Cargo]:
        sql = ("SELECT id_cargo, nombre, COALESCE(descripcion,''), activo "
               "  FROM personal.cargo WHERE id_fundo = %s ")
        if solo_activos:
            sql += " AND activo = TRUE "
        sql += " ORDER BY nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return [Cargo(*r) for r in cur.fetchall()]
