"""
Lógica de permisos: lectura del árbol de módulos y permisos por usuario.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class Modulo:
    id_modulo: int
    codigo: str
    nombre: str
    icono: Optional[str]
    padre_id: Optional[int]
    orden: int
    hijos: list["Modulo"] = field(default_factory=list)


class ClPermisos:
    """Consulta el árbol de módulos y los permisos efectivos del usuario."""

    def permisos_por_usuario(self, id_usuario: int,
                             es_admin: bool) -> dict[str, set[str]]:
        """
        Devuelve un dict { codigo_modulo: {"ver","crear","editar","eliminar"} }.
        Si es_admin, incluye TODOS los módulos con todas las acciones.
        """
        if es_admin:
            sql = """
                SELECT m.codigo, TRUE, TRUE, TRUE, TRUE
                  FROM seguridad.modulo m
                 WHERE m.activo = TRUE
            """
            params: tuple = ()
        else:
            sql = """
                SELECT m.codigo,
                       BOOL_OR(p.ver),
                       BOOL_OR(p.crear),
                       BOOL_OR(p.editar),
                       BOOL_OR(p.eliminar)
                  FROM seguridad.usuario_rol ur
                  JOIN seguridad.permiso     p ON p.id_rol    = ur.id_rol
                  JOIN seguridad.modulo      m ON m.id_modulo = p.id_modulo
                 WHERE ur.id_usuario = %s
                   AND m.activo = TRUE
                 GROUP BY m.codigo
            """
            params = (id_usuario,)

        permisos: dict[str, set[str]] = {}
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                for codigo, ver, crear, editar, eliminar in cur.fetchall():
                    acciones: set[str] = set()
                    if ver:      acciones.add("ver")
                    if crear:    acciones.add("crear")
                    if editar:   acciones.add("editar")
                    if eliminar: acciones.add("eliminar")
                    if acciones:
                        permisos[codigo] = acciones
        return permisos

    def arbol_modulos_completo(self) -> list[Modulo]:
        """Devuelve el árbol entero de módulos activos (sin filtrar por permisos)."""
        return self._cargar_arbol(filtrar_visibles=None)

    def permisos_de_rol(self, id_rol: int) -> dict[int, dict[str, bool]]:
        """{ id_modulo: {ver, crear, editar, eliminar} }"""
        sql = ("SELECT id_modulo, ver, crear, editar, eliminar "
               "  FROM seguridad.permiso WHERE id_rol = %s")
        resultado: dict[int, dict[str, bool]] = {}
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_rol,))
                for id_m, v, c, e, d in cur.fetchall():
                    resultado[id_m] = {"ver": v, "crear": c,
                                       "editar": e, "eliminar": d}
        return resultado

    def guardar_permisos_rol(self, id_rol: int,
                             permisos: dict[int, dict[str, bool]]) -> None:
        """Reemplaza todos los permisos del rol con los proporcionados."""
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM seguridad.permiso WHERE id_rol=%s",
                            (id_rol,))
                for id_modulo, p in permisos.items():
                    if not (p.get("ver") or p.get("crear")
                            or p.get("editar") or p.get("eliminar")):
                        continue
                    cur.execute(
                        "INSERT INTO seguridad.permiso "
                        "(id_rol, id_modulo, ver, crear, editar, eliminar) "
                        "VALUES (%s,%s,%s,%s,%s,%s)",
                        (id_rol, id_modulo,
                         p.get("ver", False), p.get("crear", False),
                         p.get("editar", False), p.get("eliminar", False)),
                    )
            conn.commit()

    def arbol_modulos_visibles(self,
                               codigos_visibles: set[str]) -> list[Modulo]:
        """Devuelve el árbol de módulos filtrado a los códigos visibles."""
        return self._cargar_arbol(filtrar_visibles=codigos_visibles)

    def _cargar_arbol(self, filtrar_visibles: set[str] | None
                      ) -> list[Modulo]:
        sql = """
            SELECT id_modulo, codigo, nombre, icono, padre_id, orden
              FROM seguridad.modulo
             WHERE activo = TRUE
             ORDER BY COALESCE(padre_id, 0), orden, nombre
        """
        modulos: dict[int, Modulo] = {}
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                for r in cur.fetchall():
                    m = Modulo(*r)
                    modulos[m.id_modulo] = m

        raices: list[Modulo] = []
        for m in modulos.values():
            if m.padre_id is None:
                raices.append(m)
            else:
                padre = modulos.get(m.padre_id)
                if padre is not None:
                    padre.hijos.append(m)

        if filtrar_visibles is None:
            return raices

        def filtrar(nodos: list[Modulo]) -> list[Modulo]:
            resultado = []
            for n in nodos:
                hijos_visibles = filtrar(n.hijos)
                if n.codigo in filtrar_visibles or hijos_visibles:
                    n.hijos = hijos_visibles
                    resultado.append(n)
            return resultado

        return filtrar(raices)
