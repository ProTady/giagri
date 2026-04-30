"""Lógica del fundo (datos generales)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Fundo:
    id_fundo: int
    codigo: str
    nombre: str
    ruc: str
    direccion: str
    telefono: str
    activo: bool


class ClFundo:

    def obtener(self, id_fundo: int) -> Optional[Fundo]:
        sql = """
            SELECT id_fundo, codigo, nombre,
                   COALESCE(ruc,''), COALESCE(direccion,''),
                   COALESCE(telefono,''), activo
              FROM seguridad.fundo
             WHERE id_fundo = %s
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            r = cur.fetchone()
        return Fundo(*r) if r else None

    def actualizar(self, id_fundo: int, nombre: str, ruc: str,
                   direccion: str, telefono: str) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del fundo es obligatorio.")
        if ruc and len(ruc.strip()) != 11:
            raise ValueError("El RUC debe tener 11 dígitos.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                """
                UPDATE seguridad.fundo
                   SET nombre=%s, ruc=%s, direccion=%s, telefono=%s
                 WHERE id_fundo=%s
                """,
                (nombre,
                 ruc.strip() or None,
                 direccion.strip() or None,
                 telefono.strip() or None,
                 id_fundo),
            )
            conn.commit()
