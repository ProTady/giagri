"""Lógica de empleados (personal.empleado)."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional

from Conexion.cn_postgres import ConexionPostgres


@dataclass
class EmpleadoFila:
    id_empleado: int
    codigo: str
    dni: str
    apellidos: str
    nombres: str
    cargo: str
    area: str
    fecha_ingreso: Optional[date]
    estado: str


class ClEmpleado:

    def listar(self, id_fundo: int, filtro: str = "",
               estado: str = "todos") -> list[EmpleadoFila]:
        sql = """
            SELECT e.id_empleado, e.codigo, e.dni,
                   e.apellido_paterno || ' ' || COALESCE(e.apellido_materno,''),
                   e.nombres,
                   COALESCE(c.nombre,''), COALESCE(a.nombre,''),
                   e.fecha_ingreso, e.estado
              FROM personal.empleado e
              LEFT JOIN personal.cargo         c ON c.id_cargo = e.id_cargo
              LEFT JOIN personal.area_trabajo  a ON a.id_area  = e.id_area
             WHERE e.id_fundo = %s
        """
        params: list = [id_fundo]
        if filtro:
            sql += (" AND (e.codigo ILIKE %s OR e.dni ILIKE %s "
                    "      OR e.apellido_paterno ILIKE %s "
                    "      OR e.apellido_materno ILIKE %s "
                    "      OR e.nombres ILIKE %s) ")
            patron = f"%{filtro}%"
            params += [patron, patron, patron, patron, patron]
        if estado != "todos":
            sql += " AND e.estado = %s "
            params.append(estado)
        sql += " ORDER BY e.apellido_paterno, e.apellido_materno, e.nombres "

        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return [EmpleadoFila(*r) for r in cur.fetchall()]

    def obtener(self, id_empleado: int) -> Optional[dict]:
        sql = """
            SELECT id_empleado, id_fundo, codigo, dni,
                   apellido_paterno, COALESCE(apellido_materno,''), nombres,
                   fecha_nacimiento, sexo, COALESCE(estado_civil,''),
                   COALESCE(direccion,''), COALESCE(telefono,''),
                   COALESCE(correo,''),
                   fecha_ingreso, fecha_cese, estado,
                   id_cargo, id_area, sueldo_base,
                   COALESCE(cuenta_banco,''), COALESCE(banco,''),
                   COALESCE(observaciones,''), regimen
              FROM personal.empleado WHERE id_empleado = %s
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_empleado,))
            r = cur.fetchone()
        if r is None:
            return None
        campos = ["id_empleado","id_fundo","codigo","dni",
                  "apellido_paterno","apellido_materno","nombres",
                  "fecha_nacimiento","sexo","estado_civil",
                  "direccion","telefono","correo",
                  "fecha_ingreso","fecha_cese","estado",
                  "id_cargo","id_area","sueldo_base",
                  "cuenta_banco","banco","observaciones","regimen"]
        return dict(zip(campos, r))

    def siguiente_codigo(self, id_fundo: int, prefijo: str = "EMP-") -> str:
        """Genera el próximo código auto-incrementable.

        Busca el MÁXIMO sufijo numérico entre todos los códigos existentes
        del fundo (sin importar el prefijo) y devuelve <prefijo><N+1>.
        Mantiene el ancho de zero-padding (3 dígitos por defecto).
        """
        import re
        sql = "SELECT codigo FROM personal.empleado WHERE id_fundo = %s"
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            codigos = [r[0] for r in cur.fetchall()]

        max_n = 0
        ancho = 3
        for c in codigos:
            m = re.search(r"(\d+)$", c or "")
            if m:
                n = int(m.group(1))
                if n > max_n:
                    max_n = n
                    ancho = max(ancho, len(m.group(1)))

        return f"{prefijo}{max_n + 1:0{ancho}d}"

    def existe(self, id_fundo: int, campo: str, valor: str,
               excluir_id: Optional[int] = None) -> bool:
        if campo not in ("codigo", "dni"):
            raise ValueError("campo debe ser 'codigo' o 'dni'")
        sql = (f"SELECT 1 FROM personal.empleado "
               f"WHERE id_fundo=%s AND LOWER({campo})=LOWER(%s) ")
        params: list = [id_fundo, valor]
        if excluir_id is not None:
            sql += " AND id_empleado <> %s "
            params.append(excluir_id)
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None

    def crear(self, datos: dict) -> int:
        self._validar(datos)
        if self.existe(datos["id_fundo"], "codigo", datos["codigo"]):
            raise ValueError(f"Ya existe un empleado con código '{datos['codigo']}'.")
        if self.existe(datos["id_fundo"], "dni", datos["dni"]):
            raise ValueError(f"Ya existe un empleado con DNI '{datos['dni']}'.")

        sql = """
            INSERT INTO personal.empleado
                (id_fundo, codigo, dni, apellido_paterno, apellido_materno,
                 nombres, fecha_nacimiento, sexo, estado_civil,
                 direccion, telefono, correo,
                 fecha_ingreso, fecha_cese, estado, regimen,
                 id_cargo, id_area, sueldo_base,
                 cuenta_banco, banco, observaciones)
            VALUES (%(id_fundo)s, %(codigo)s, %(dni)s,
                    %(apellido_paterno)s, %(apellido_materno)s,
                    %(nombres)s, %(fecha_nacimiento)s, %(sexo)s, %(estado_civil)s,
                    %(direccion)s, %(telefono)s, %(correo)s,
                    %(fecha_ingreso)s, %(fecha_cese)s, %(estado)s, %(regimen)s,
                    %(id_cargo)s, %(id_area)s, %(sueldo_base)s,
                    %(cuenta_banco)s, %(banco)s, %(observaciones)s)
            RETURNING id_empleado
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, self._normalizar(datos))
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def actualizar(self, id_empleado: int, datos: dict) -> None:
        self._validar(datos)
        if self.existe(datos["id_fundo"], "codigo", datos["codigo"], excluir_id=id_empleado):
            raise ValueError(f"Ya existe un empleado con código '{datos['codigo']}'.")
        if self.existe(datos["id_fundo"], "dni", datos["dni"], excluir_id=id_empleado):
            raise ValueError(f"Ya existe un empleado con DNI '{datos['dni']}'.")

        sql = """
            UPDATE personal.empleado SET
                codigo = %(codigo)s, dni = %(dni)s,
                apellido_paterno = %(apellido_paterno)s,
                apellido_materno = %(apellido_materno)s,
                nombres = %(nombres)s,
                fecha_nacimiento = %(fecha_nacimiento)s,
                sexo = %(sexo)s, estado_civil = %(estado_civil)s,
                direccion = %(direccion)s, telefono = %(telefono)s,
                correo = %(correo)s,
                fecha_ingreso = %(fecha_ingreso)s, fecha_cese = %(fecha_cese)s,
                estado = %(estado)s, regimen = %(regimen)s,
                id_cargo = %(id_cargo)s, id_area = %(id_area)s,
                sueldo_base = %(sueldo_base)s,
                cuenta_banco = %(cuenta_banco)s, banco = %(banco)s,
                observaciones = %(observaciones)s,
                actualizado_en = NOW()
            WHERE id_empleado = %(id_empleado)s
        """
        params = self._normalizar(datos)
        params["id_empleado"] = id_empleado
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            conn.commit()

    def eliminar(self, id_empleado: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM personal.empleado WHERE id_empleado=%s",
                        (id_empleado,))
            conn.commit()

    # ------------------------------------------------------------------
    @staticmethod
    def _validar(d: dict) -> None:
        if not d.get("codigo"):
            raise ValueError("El código es obligatorio.")
        if not d.get("dni"):
            raise ValueError("El DNI es obligatorio.")
        if len(d["dni"]) < 8:
            raise ValueError("El DNI debe tener al menos 8 dígitos.")
        if not d.get("apellido_paterno") or not d.get("nombres"):
            raise ValueError("Apellido paterno y nombres son obligatorios.")
        if not d.get("fecha_ingreso"):
            raise ValueError("La fecha de ingreso es obligatoria.")

    @staticmethod
    def _normalizar(d: dict) -> dict:
        """Convierte cadenas vacías a None para columnas opcionales."""
        out = dict(d)
        for k in ("apellido_materno","estado_civil","direccion","telefono",
                  "correo","cuenta_banco","banco","observaciones",
                  "fecha_nacimiento","fecha_cese","sexo",
                  "id_cargo","id_area","sueldo_base"):
            if out.get(k) in ("", None):
                out[k] = None
        return out
