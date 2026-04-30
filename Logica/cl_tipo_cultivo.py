"""Lógica de tipos de cultivo."""
from __future__ import annotations
from dataclasses import dataclass
from Conexion.cn_postgres import ConexionPostgres


@dataclass
class TipoCultivo:
    id_tipo_cultivo: int
    nombre: str
    nombre_cientifico: str
    activo: bool


class ClTipoCultivo:
    def listar(self, id_fundo: int, solo_activos: bool = True) -> list[TipoCultivo]:
        sql = ("SELECT id_tipo_cultivo, nombre, COALESCE(nombre_cientifico,''), activo "
               "  FROM agricola.tipo_cultivo WHERE id_fundo=%s ")
        if solo_activos:
            sql += " AND activo = TRUE "
        sql += " ORDER BY nombre "
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return [TipoCultivo(*r) for r in cur.fetchall()]

    def existe_nombre(self, id_fundo: int, nombre: str,
                      excluir_id: int | None = None) -> bool:
        sql = ("SELECT 1 FROM agricola.tipo_cultivo "
               "WHERE id_fundo=%s AND LOWER(nombre)=LOWER(%s) ")
        params: list = [id_fundo, nombre]
        if excluir_id is not None:
            sql += " AND id_tipo_cultivo <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, id_fundo: int, nombre: str,
              nombre_cientifico: str = "") -> int:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe_nombre(id_fundo, nombre):
            raise ValueError(f"Ya existe el cultivo '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO agricola.tipo_cultivo "
                "(id_fundo, nombre, nombre_cientifico) "
                "VALUES (%s,%s,%s) RETURNING id_tipo_cultivo",
                (id_fundo, nombre, nombre_cientifico.strip() or None),
            )
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_tipo: int, id_fundo: int,
                   nombre: str, nombre_cientifico: str,
                   activo: bool) -> None:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if self.existe_nombre(id_fundo, nombre, excluir_id=id_tipo):
            raise ValueError(f"Ya existe el cultivo '{nombre}'.")
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE agricola.tipo_cultivo "
                "SET nombre=%s, nombre_cientifico=%s, activo=%s "
                "WHERE id_tipo_cultivo=%s",
                (nombre, nombre_cientifico.strip() or None, activo, id_tipo),
            )
            conn.commit()

    def eliminar(self, id_tipo: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) FROM agricola.lote WHERE id_tipo_cultivo=%s",
                (id_tipo,),
            )
            en_uso_lote = cur.fetchone()[0]
            cur.execute(
                "SELECT COUNT(*) FROM agricola.variedad WHERE id_tipo_cultivo=%s",
                (id_tipo,),
            )
            en_uso_var = cur.fetchone()[0]
            if en_uso_lote or en_uso_var:
                raise ValueError(
                    f"No se puede eliminar: el cultivo está usado en "
                    f"{en_uso_lote} lote(s) y {en_uso_var} variedad(es). "
                    "Considera desactivarlo en lugar de eliminarlo."
                )
            cur.execute(
                "DELETE FROM agricola.tipo_cultivo WHERE id_tipo_cultivo=%s",
                (id_tipo,),
            )
            conn.commit()
