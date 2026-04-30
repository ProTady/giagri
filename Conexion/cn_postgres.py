"""
Conexión a PostgreSQL con pool de conexiones.
Carga credenciales desde .env.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from psycopg_pool import ConnectionPool

# Cargar .env desde la raíz del proyecto
_RAIZ = Path(__file__).resolve().parent.parent
load_dotenv(_RAIZ / ".env")


class ConexionPostgres:
    """Singleton del pool de conexiones a PostgreSQL."""

    _instancia: Optional["ConexionPostgres"] = None
    _pool: Optional[ConnectionPool] = None

    def __new__(cls) -> "ConexionPostgres":
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar_pool()
        return cls._instancia

    def _inicializar_pool(self) -> None:
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        nombre = os.getenv("DB_NAME", "giagri")
        usuario = os.getenv("DB_USER", "postgres")
        clave = os.getenv("DB_PASSWORD", "")
        min_size = int(os.getenv("DB_POOL_MIN", "1"))
        max_size = int(os.getenv("DB_POOL_MAX", "10"))

        conninfo = (
            f"host={host} port={port} dbname={nombre} "
            f"user={usuario} password={clave}"
        )

        self._pool = ConnectionPool(
            conninfo=conninfo,
            min_size=min_size,
            max_size=max_size,
            open=True,
            kwargs={"autocommit": False},
        )

    @property
    def pool(self) -> ConnectionPool:
        if self._pool is None:
            raise RuntimeError("El pool no fue inicializado.")
        return self._pool

    def conexion(self):
        """Devuelve un context manager con una conexión del pool.

        Uso:
            with ConexionPostgres().conexion() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT ...")
        """
        return self.pool.connection()

    def cerrar(self) -> None:
        if self._pool is not None:
            self._pool.close()
            self._pool = None
            ConexionPostgres._instancia = None


def probar_conexion() -> bool:
    """Prueba rápida de conexión. Devuelve True si conecta."""
    try:
        with ConexionPostgres().conexion() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                return cur.fetchone()[0] == 1
    except Exception as e:
        print(f"[ERROR conexión] {e}")
        return False
