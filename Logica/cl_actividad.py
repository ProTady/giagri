"""Lógica de actividades (clasificación amplia de labores)."""
from __future__ import annotations
from dataclasses import dataclass
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Actividad:
    id_actividad: int
    nombre: str
    descripcion: str
    activo: bool


class ClActividad:
    def listar(self, id_fundo: int, solo_activos: bool = True) -> list[Actividad]:
        sql = ("SELECT id_actividad, nombre, COALESCE(descripcion,''), activo "
               "  FROM personal.actividad WHERE id_fundo=%s ")
        if solo_activos:
            sql += " AND activo=TRUE "
        sql += " ORDER BY nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return [Actividad(*r) for r in cur.fetchall()]

    def existe(self, id_fundo: int, nombre: str,
               excluir_id: int | None = None) -> bool:
        sql = ("SELECT 1 FROM personal.actividad "
               "WHERE id_fundo=%s AND LOWER(nombre)=LOWER(%s) ")
        params: list = [id_fundo, nombre]
        if excluir_id is not None:
            sql += " AND id_actividad <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, id_fundo: int, nombre: str, descripcion: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe(id_fundo, nombre):
            raise ValueError(f"Ya existe la actividad '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO personal.actividad (id_fundo, nombre, descripcion) "
                "VALUES (%s,%s,%s) RETURNING id_actividad",
                (id_fundo, nombre, descripcion.strip() or None),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_actividad: int, id_fundo: int,
                   nombre: str, descripcion: str, activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe(id_fundo, nombre, excluir_id=id_actividad):
            raise ValueError(f"Ya existe la actividad '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE personal.actividad "
                "SET nombre=%s, descripcion=%s, activo=%s "
                "WHERE id_actividad=%s",
                (nombre, descripcion.strip() or None, activo, id_actividad),
            )
            conn.commit()

    def eliminar(self, id_actividad: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM personal.labor WHERE id_actividad=%s",
                (id_actividad,),
            )
            if cur.fetchone()[0]:
                raise ValueError(
                    "No se puede eliminar: hay labores asociadas a esta actividad."
                )
            cur.execute(
                "SELECT COUNT(*) FROM personal.tareo WHERE id_actividad=%s",
                (id_actividad,),
            )
            if cur.fetchone()[0]:
                raise ValueError("La actividad tiene tareos registrados.")
            cur.execute(
                "DELETE FROM personal.actividad WHERE id_actividad=%s",
                (id_actividad,),
            )
            conn.commit()
