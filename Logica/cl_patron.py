"""Lógica de patrones de injerto."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Patron:
    id_patron: int
    id_tipo_cultivo: int
    nombre: str
    descripcion: str
    activo: bool


class ClPatron:
    def listar(self, id_fundo: int,
               id_tipo_cultivo: Optional[int] = None,
               solo_activos: bool = True) -> list[Patron]:
        sql = """
            SELECT p.id_patron, p.id_tipo_cultivo, p.nombre,
                   COALESCE(p.descripcion,''), p.activo
              FROM agricola.patron p
              JOIN agricola.tipo_cultivo t ON t.id_tipo_cultivo = p.id_tipo_cultivo
             WHERE t.id_fundo = %s
        """
        params: list = [id_fundo]
        if id_tipo_cultivo:
            sql += " AND p.id_tipo_cultivo = %s "
            params.append(id_tipo_cultivo)
        if solo_activos:
            sql += " AND p.activo = TRUE "
        sql += " ORDER BY p.nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return [Patron(*r) for r in cur.fetchall()]

    def crear(self, id_tipo_cultivo: int, nombre: str,
              descripcion: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM agricola.patron "
                "WHERE id_tipo_cultivo=%s AND LOWER(nombre)=LOWER(%s)",
                (id_tipo_cultivo, nombre),
            )
            if cur.fetchone():
                raise ValueError(f"Ya existe el patrón '{nombre}' para ese cultivo.")
            cur.execute(
                "INSERT INTO agricola.patron "
                "(id_tipo_cultivo, nombre, descripcion) "
                "VALUES (%s,%s,%s) RETURNING id_patron",
                (id_tipo_cultivo, nombre, descripcion.strip() or None),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_patron: int, nombre: str,
                   descripcion: str, activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE agricola.patron "
                "SET nombre=%s, descripcion=%s, activo=%s "
                "WHERE id_patron=%s",
                (nombre, descripcion.strip() or None, activo, id_patron),
            )
            conn.commit()

    def eliminar(self, id_patron: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM agricola.lote WHERE id_patron=%s",
                (id_patron,),
            )
            if cur.fetchone()[0]:
                raise ValueError(
                    "No se puede eliminar: el patrón está usado en lotes."
                )
            cur.execute(
                "DELETE FROM agricola.patron WHERE id_patron=%s",
                (id_patron,),
            )
            conn.commit()
