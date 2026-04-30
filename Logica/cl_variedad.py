"""Lógica de variedades de cultivo."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Variedad:
    id_variedad: int
    id_tipo_cultivo: int
    nombre: str
    descripcion: str
    activo: bool


class ClVariedad:
    def listar(self, id_fundo: int,
               id_tipo_cultivo: Optional[int] = None,
               solo_activos: bool = True) -> list[Variedad]:
        sql = """
            SELECT v.id_variedad, v.id_tipo_cultivo, v.nombre,
                   COALESCE(v.descripcion,''), v.activo
              FROM agricola.variedad v
              JOIN agricola.tipo_cultivo t ON t.id_tipo_cultivo = v.id_tipo_cultivo
             WHERE t.id_fundo = %s
        """
        params: list = [id_fundo]
        if id_tipo_cultivo:
            sql += " AND v.id_tipo_cultivo = %s "
            params.append(id_tipo_cultivo)
        if solo_activos:
            sql += " AND v.activo = TRUE "
        sql += " ORDER BY v.nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return [Variedad(*r) for r in cur.fetchall()]

    def crear(self, id_tipo_cultivo: int, nombre: str,
              descripcion: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM agricola.variedad "
                "WHERE id_tipo_cultivo=%s AND LOWER(nombre)=LOWER(%s)",
                (id_tipo_cultivo, nombre),
            )
            if cur.fetchone():
                raise ValueError(f"Ya existe la variedad '{nombre}' para ese cultivo.")
            cur.execute(
                "INSERT INTO agricola.variedad "
                "(id_tipo_cultivo, nombre, descripcion) "
                "VALUES (%s,%s,%s) RETURNING id_variedad",
                (id_tipo_cultivo, nombre, descripcion.strip() or None),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_variedad: int, nombre: str,
                   descripcion: str, activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE agricola.variedad "
                "SET nombre=%s, descripcion=%s, activo=%s "
                "WHERE id_variedad=%s",
                (nombre, descripcion.strip() or None, activo, id_variedad),
            )
            conn.commit()

    def eliminar(self, id_variedad: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM agricola.lote WHERE id_variedad=%s",
                (id_variedad,),
            )
            if cur.fetchone()[0]:
                raise ValueError(
                    "No se puede eliminar: la variedad está usada en lotes."
                )
            cur.execute(
                "DELETE FROM agricola.variedad WHERE id_variedad=%s",
                (id_variedad,),
            )
            conn.commit()
