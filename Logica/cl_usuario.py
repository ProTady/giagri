"""
Lógica de usuario: autenticación + CRUD de usuarios.
Multi-tenant: todas las operaciones de mantenimiento operan dentro de id_fundo.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import bcrypt

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class UsuarioAutenticado:
    id_usuario: int
    username: str
    nombre_completo: str
    id_fundo: int
    nombre_fundo: str
    es_admin: bool


@dataclass
class UsuarioFila:
    id_usuario: int
    username: str
    nombre_completo: str
    correo: str
    es_admin: bool
    activo: bool
    ultimo_acceso: Optional[datetime]
    roles: str  # CSV de nombres de rol


class ClUsuario:
    """Operaciones de autenticación y mantenimiento de usuarios."""

    # ============================================================
    # AUTENTICACIÓN
    # ============================================================
    def autenticar(self, username: str, clave: str) -> Optional[UsuarioAutenticado]:
        if not username or not clave:
            return None

        sql = """
            SELECT u.id_usuario, u.username, u.nombre_completo,
                   u.password_hash, u.es_admin, u.activo,
                   f.id_fundo, f.nombre, f.activo
              FROM seguridad.usuario u
              JOIN seguridad.fundo   f ON f.id_fundo = u.id_fundo
             WHERE u.username = %s
        """
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username,))
                fila = cur.fetchone()

        if fila is None:
            self._log_acceso(None, "LOGIN_FAIL", f"usuario inexistente: {username}")
            return None

        (id_u, uname, nombre, p_hash, es_admin, activo,
         id_f, nombre_f, fundo_activo) = fila

        if not activo:
            self._log_acceso(id_u, "LOGIN_FAIL", "usuario inactivo")
            return None
        if not fundo_activo:
            self._log_acceso(id_u, "LOGIN_FAIL", "fundo inactivo")
            return None
        if not self._verificar_clave(clave, p_hash):
            self._log_acceso(id_u, "LOGIN_FAIL", "clave incorrecta")
            return None

        self._actualizar_ultimo_acceso(id_u)
        self._log_acceso(id_u, "LOGIN_OK", "")

        return UsuarioAutenticado(
            id_usuario=id_u, username=uname, nombre_completo=nombre,
            id_fundo=id_f, nombre_fundo=nombre_f, es_admin=es_admin,
        )

    def _verificar_clave(self, clave: str, hash_almacenado: str) -> bool:
        try:
            return bcrypt.checkpw(clave.encode("utf-8"),
                                  hash_almacenado.encode("utf-8"))
        except Exception:
            return False

    def _actualizar_ultimo_acceso(self, id_usuario: int) -> None:
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE seguridad.usuario SET ultimo_acceso = NOW() "
                    "WHERE id_usuario = %s",
                    (id_usuario,),
                )
            conn.commit()

    def _log_acceso(self, id_usuario: Optional[int], accion: str,
                    detalle: str) -> None:
        try:
            with ConexionPostgres().conexion() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO seguridad.acceso_log "
                        "(id_usuario, accion, detalle) VALUES (%s,%s,%s)",
                        (id_usuario, accion, detalle),
                    )
                conn.commit()
        except Exception:
            pass

    @staticmethod
    def hashear_clave(clave: str) -> str:
        return bcrypt.hashpw(clave.encode("utf-8"),
                             bcrypt.gensalt()).decode("utf-8")

    # ============================================================
    # CRUD
    # ============================================================
    def listar(self, id_fundo: int, filtro: str = "",
               estado: str = "todos") -> list[UsuarioFila]:
        """Lista usuarios del fundo, opcionalmente filtrando."""
        sql = """
            SELECT u.id_usuario, u.username, u.nombre_completo,
                   COALESCE(u.correo, ''),
                   u.es_admin, u.activo, u.ultimo_acceso,
                   COALESCE(STRING_AGG(r.nombre, ', ' ORDER BY r.nombre), '')
              FROM seguridad.usuario u
              LEFT JOIN seguridad.usuario_rol ur ON ur.id_usuario = u.id_usuario
              LEFT JOIN seguridad.rol         r  ON r.id_rol      = ur.id_rol
             WHERE u.id_fundo = %s
        """
        params: list = [id_fundo]

        if filtro:
            sql += (" AND (u.username ILIKE %s OR u.nombre_completo ILIKE %s "
                    "      OR COALESCE(u.correo,'') ILIKE %s) ")
            patron = f"%{filtro}%"
            params += [patron, patron, patron]

        if estado == "activos":
            sql += " AND u.activo = TRUE "
        elif estado == "inactivos":
            sql += " AND u.activo = FALSE "

        sql += " GROUP BY u.id_usuario ORDER BY u.username "

        resultado: list[UsuarioFila] = []
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                for r in cur.fetchall():
                    resultado.append(UsuarioFila(*r))
        return resultado

    def obtener(self, id_usuario: int) -> Optional[dict]:
        sql = """
            SELECT id_usuario, id_fundo, username, nombre_completo,
                   COALESCE(correo,''), es_admin, activo
              FROM seguridad.usuario
             WHERE id_usuario = %s
        """
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario,))
                r = cur.fetchone()
        if r is None:
            return None
        return {
            "id_usuario": r[0], "id_fundo": r[1], "username": r[2],
            "nombre_completo": r[3], "correo": r[4],
            "es_admin": r[5], "activo": r[6],
        }

    def existe_username(self, id_fundo: int, username: str,
                        excluir_id: Optional[int] = None) -> bool:
        sql = ("SELECT 1 FROM seguridad.usuario "
               "WHERE id_fundo = %s AND LOWER(username) = LOWER(%s) ")
        params: list = [id_fundo, username]
        if excluir_id is not None:
            sql += " AND id_usuario <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchone() is not None

    def crear(self, id_fundo: int, username: str, clave: str,
              nombre_completo: str, correo: str, es_admin: bool,
              activo: bool, ids_roles: list[int]) -> int:
        if self.existe_username(id_fundo, username):
            raise ValueError(f"El usuario '{username}' ya existe en este fundo.")
        if len(clave) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")

        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO seguridad.usuario
                        (id_fundo, username, password_hash, nombre_completo,
                         correo, es_admin, activo)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    RETURNING id_usuario
                    """,
                    (id_fundo, username, self.hashear_clave(clave),
                     nombre_completo, correo or None, es_admin, activo),
                )
                id_nuevo = cur.fetchone()[0]
                self._asignar_roles(cur, id_nuevo, ids_roles)
            conn.commit()
        return id_nuevo

    def actualizar(self, id_usuario: int, nombre_completo: str,
                   correo: str, es_admin: bool, activo: bool,
                   ids_roles: list[int]) -> None:
        # Proteger último admin
        actual = self.obtener(id_usuario)
        if actual is None:
            raise ValueError("Usuario no encontrado.")
        if (actual["es_admin"] and (not es_admin or not activo)):
            if self._cuantos_admins_activos(actual["id_fundo"]) <= 1:
                raise ValueError(
                    "No puedes quitar el rol admin ni desactivar al último administrador del fundo.")

        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE seguridad.usuario
                       SET nombre_completo = %s,
                           correo = %s,
                           es_admin = %s,
                           activo = %s
                     WHERE id_usuario = %s
                    """,
                    (nombre_completo, correo or None, es_admin, activo,
                     id_usuario),
                )
                cur.execute("DELETE FROM seguridad.usuario_rol WHERE id_usuario=%s",
                            (id_usuario,))
                self._asignar_roles(cur, id_usuario, ids_roles)
            conn.commit()

    def cambiar_clave(self, id_usuario: int, clave_nueva: str) -> None:
        if len(clave_nueva) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE seguridad.usuario SET password_hash = %s "
                    "WHERE id_usuario = %s",
                    (self.hashear_clave(clave_nueva), id_usuario),
                )
            conn.commit()

    def alternar_activo(self, id_usuario: int, id_usuario_solicitante: int) -> bool:
        if id_usuario == id_usuario_solicitante:
            raise ValueError("No puedes desactivarte a ti mismo.")
        actual = self.obtener(id_usuario)
        if actual is None:
            raise ValueError("Usuario no encontrado.")

        nuevo_estado = not actual["activo"]
        if (actual["es_admin"] and actual["activo"] and
                self._cuantos_admins_activos(actual["id_fundo"]) <= 1):
            raise ValueError(
                "No puedes desactivar al último administrador activo del fundo.")

        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE seguridad.usuario SET activo = %s WHERE id_usuario=%s",
                    (nuevo_estado, id_usuario),
                )
            conn.commit()
        return nuevo_estado

    def roles_de_usuario(self, id_usuario: int) -> set[int]:
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id_rol FROM seguridad.usuario_rol WHERE id_usuario=%s",
                    (id_usuario,),
                )
                return {r[0] for r in cur.fetchall()}

    # ------------------------------------------------------------------
    def _asignar_roles(self, cur, id_usuario: int,
                       ids_roles: list[int]) -> None:
        for id_rol in ids_roles:
            cur.execute(
                "INSERT INTO seguridad.usuario_rol (id_usuario, id_rol) "
                "VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (id_usuario, id_rol),
            )

    def _cuantos_admins_activos(self, id_fundo: int) -> int:
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) FROM seguridad.usuario "
                    "WHERE id_fundo = %s AND es_admin = TRUE AND activo = TRUE",
                    (id_fundo,),
                )
                return cur.fetchone()[0]
