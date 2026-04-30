"""
Lógica de roles. Multi-tenant: siempre filtra por id_fundo.
"""
from __future__ import annotations

from dataclasses import dataclass

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Rol:
    id_rol: int
    nombre: str
    descripcion: str
    activo: bool


class ClRol:

    def listar(self, id_fundo: int, solo_activos: bool = True) -> list[Rol]:
        sql = ("SELECT id_rol, nombre, COALESCE(descripcion,''), activo "
               "  FROM seguridad.rol WHERE id_fundo = %s ")
        if solo_activos:
            sql += " AND activo = TRUE "
        sql += " ORDER BY nombre "
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_fundo,))
                return [Rol(*r) for r in cur.fetchall()]

    def existe_nombre(self, id_fundo: int, nombre: str,
                      excluir_id: int | None = None) -> bool:
        sql = ("SELECT 1 FROM seguridad.rol "
               "WHERE id_fundo=%s AND LOWER(nombre)=LOWER(%s) ")
        params: list = [id_fundo, nombre]
        if excluir_id is not None:
            sql += " AND id_rol <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchone() is not None

    def crear(self, id_fundo: int, nombre: str, descripcion: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del rol es obligatorio.")
        if self.existe_nombre(id_fundo, nombre):
            raise ValueError(f"Ya existe un rol llamado '{nombre}'.")
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO seguridad.rol (id_fundo, nombre, descripcion) "
                    "VALUES (%s,%s,%s) RETURNING id_rol",
                    (id_fundo, nombre, descripcion or None),
                )
                nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def renombrar(self, id_rol: int, id_fundo: int, nombre_nuevo: str) -> None:
        nombre_nuevo = nombre_nuevo.strip()
        if not nombre_nuevo:
            raise ValueError("El nombre no puede estar vacío.")
        if self.existe_nombre(id_fundo, nombre_nuevo, excluir_id=id_rol):
            raise ValueError(f"Ya existe un rol llamado '{nombre_nuevo}'.")
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE seguridad.rol SET nombre=%s WHERE id_rol=%s",
                    (nombre_nuevo, id_rol),
                )
            conn.commit()

    def eliminar(self, id_rol: int) -> None:
        """Borra el rol (en cascada caen permisos y asignaciones)."""
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) FROM seguridad.usuario_rol WHERE id_rol=%s",
                    (id_rol,),
                )
                en_uso = cur.fetchone()[0]
                if en_uso:
                    raise ValueError(
                        f"No se puede eliminar: el rol está asignado a "
                        f"{en_uso} usuario(s). Primero retira el rol de esos usuarios."
                    )
                cur.execute("DELETE FROM seguridad.rol WHERE id_rol=%s",
                            (id_rol,))
            conn.commit()
