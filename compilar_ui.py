"""
Compila todos los archivos .ui de Vistas/ a ui_*.py usando pyside6-uic.

Uso:
    python compilar_ui.py

Convención:
    Vistas/login/v_login.ui  ->  Vistas/login/ui_login.py
    Vistas/main/v_main.ui    ->  Vistas/main/ui_main.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CARPETA_VISTAS = RAIZ / "Vistas"


def _ruta_uic() -> str:
    """Localiza pyside6-uic.exe dentro del venv si está disponible."""
    exe = Path(sys.executable).parent / "pyside6-uic.exe"
    if exe.exists():
        return str(exe)
    return "pyside6-uic"


def compilar(ui: Path) -> tuple[bool, str]:
    # v_login.ui -> ui_login.py
    nombre = ui.stem
    if nombre.startswith("v_"):
        nombre = nombre[2:]
    salida = ui.parent / f"ui_{nombre}.py"

    try:
        r = subprocess.run([_ruta_uic(), str(ui), "-o", str(salida)],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return True, str(salida.relative_to(RAIZ))
        return False, (r.stderr or r.stdout).strip()
    except FileNotFoundError as e:
        return False, str(e)


def main() -> int:
    if not CARPETA_VISTAS.exists():
        print(f"[ERROR] No existe la carpeta {CARPETA_VISTAS}")
        return 1

    archivos = list(CARPETA_VISTAS.rglob("v_*.ui"))
    if not archivos:
        print("[INFO] No hay archivos .ui para compilar todavía.")
        return 0

    ok = err = 0
    for ui in archivos:
        exitoso, msg = compilar(ui)
        marca = "OK " if exitoso else "ERR"
        print(f"[{marca}] {ui.relative_to(RAIZ)}  ->  {msg}")
        if exitoso:
            ok += 1
        else:
            err += 1

    print(f"\nResumen: {ok} compilados, {err} errores.")
    return 0 if err == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
