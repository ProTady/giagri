"""
Sesión del usuario logueado.
Mantiene en memoria el usuario actual, fundo activo y permisos.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id_usuario: int
    username: str
    nombre_completo: str
    id_fundo: int
    es_admin: bool = False


class Sesion:
    """Singleton con el estado de la sesión activa."""

    _instancia: Optional["Sesion"] = None

    def __new__(cls) -> "Sesion":
        if cls._instancia is None:
            inst = super().__new__(cls)
            inst.usuario = None
            inst.nombre_fundo = ""
            inst.modulos_permitidos = set()
            inst.permisos = {}
            cls._instancia = inst
        return cls._instancia

    def iniciar(self, usuario: Usuario, nombre_fundo: str,
                permisos: dict[str, set[str]]) -> None:
        self.usuario = usuario
        self.nombre_fundo = nombre_fundo
        self.permisos = permisos
        self.modulos_permitidos = {
            cod for cod, acciones in permisos.items() if "ver" in acciones
        }

    def cerrar(self) -> None:
        self.usuario = None
        self.nombre_fundo = ""
        self.modulos_permitidos = set()
        self.permisos = {}

    def puede(self, codigo_modulo: str, accion: str = "ver") -> bool:
        if self.usuario and self.usuario.es_admin:
            return True
        return accion in self.permisos.get(codigo_modulo, set())

    @property
    def activa(self) -> bool:
        return self.usuario is not None
