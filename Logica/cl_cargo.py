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

    def existe_nombre(self, id_fundo: int, nombre: str,
                      excluir_id: int | None = None) -> bool:
        sql = ("SELECT 1 FROM personal.cargo "
               "WHERE id_fundo=%s AND LOWER(nombre)=LOWER(%s) ")
        params: list = [id_fundo, nombre]
        if excluir_id is not None:
            sql += " AND id_cargo <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, id_fundo: int, nombre: str, descripcion: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del cargo es obligatorio.")
        if self.existe_nombre(id_fundo, nombre):
            raise ValueError(f"Ya existe un cargo llamado '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO personal.cargo (id_fundo, nombre, descripcion) "
                "VALUES (%s,%s,%s) RETURNING id_cargo",
                (id_fundo, nombre, descripcion.strip() or None),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_cargo: int, id_fundo: int,
                   nombre: str, descripcion: str, activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe_nombre(id_fundo, nombre, excluir_id=id_cargo):
            raise ValueError(f"Ya existe un cargo llamado '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE personal.cargo "
                "SET nombre=%s, descripcion=%s, activo=%s WHERE id_cargo=%s",
                (nombre, descripcion.strip() or None, activo, id_cargo),
            )
            conn.commit()

    def eliminar(self, id_cargo: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM personal.empleado WHERE id_cargo=%s",
                (id_cargo,),
            )
            en_uso = cur.fetchone()[0]
            if en_uso:
                raise ValueError(
                    f"No se puede eliminar: el cargo está asignado a "
                    f"{en_uso} empleado(s). Considera desactivarlo."
                )
            cur.execute("DELETE FROM personal.cargo WHERE id_cargo=%s",
                        (id_cargo,))
            conn.commit()
