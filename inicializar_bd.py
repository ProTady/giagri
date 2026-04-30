"""
Script de inicialización de la base de datos.
Ejecuta los archivos .sql de la carpeta SQL/ en orden.

Uso:
    python inicializar_bd.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import bcrypt

from Conexion.cn_postgres import ConexionPostgres

RAIZ = Path(__file__).resolve().parent
CARPETA_SQL = RAIZ / "SQL"


def ejecutar_sql(ruta: Path) -> None:
    print(f"  -> Ejecutando {ruta.name} ...")
    sql = ruta.read_text(encoding="utf-8")
    with ConexionPostgres().conexion() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()


def actualizar_hash_admin() -> None:
    """Reemplaza el hash placeholder del admin con un bcrypt real de 'admin123'."""
    nuevo_hash = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode("utf-8")
    with ConexionPostgres().conexion() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE seguridad.usuario
                   SET password_hash = %s
                 WHERE username = 'admin'
                   AND password_hash LIKE '$2b$12$LQv3c1yqBwEHFl5aGQH3fO%%'
                """,
                (nuevo_hash,),
            )
            filas = cur.rowcount
        conn.commit()
    if filas:
        print(f"  -> Hash del usuario admin actualizado ({filas} fila/s).")


def main() -> int:
    archivos = sorted(CARPETA_SQL.glob("*.sql"))
    if not archivos:
        print("[ERROR] No hay archivos .sql en SQL/")
        return 1

    print("Inicializando base de datos GIAGRI...")
    for sql in archivos:
        try:
            ejecutar_sql(sql)
        except Exception as e:
            print(f"[ERROR] {sql.name}: {e}")
            return 2

    actualizar_hash_admin()

    print("\n[OK] Base de datos lista.")
    print("Usuario inicial: admin / admin123 (cambiar en primer login)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
