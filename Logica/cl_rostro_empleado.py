"""
Lógica de rostros de empleados (CRUD sobre personal.empleado_rostro).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import numpy as np

from Conexion.cn_postgres import ConexionPostgres
from Logica.svc_rostro import SvcRostro


@dataclass
class RostroRegistrado:
    id_rostro: int
    id_empleado: int
    angulo: str
    calidad: float
    activo: bool
    registrado_en: datetime
    foto_thumb: bytes
    embedding: np.ndarray  # ya deserializado


@dataclass
class RostroParaReconocer:
    id_empleado: int
    nombre_completo: str
    codigo: str
    embedding: np.ndarray


class ClRostroEmpleado:

    def registrar(self, id_empleado: int, embedding: np.ndarray,
                  thumb_jpeg: bytes, angulo: str, calidad: float,
                  registrado_por: Optional[int]) -> int:
        sql = """
            INSERT INTO personal.empleado_rostro
                (id_empleado, embedding, foto_thumb, angulo, calidad, registrado_por)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_rostro
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (
                id_empleado,
                SvcRostro.serializar(embedding),
                thumb_jpeg or None,
                angulo or None,
                float(calidad),
                registrado_por,
            ))
            nuevo = cur.fetchone()[0]
            conn.commit()
        return nuevo

    def listar_de_empleado(self, id_empleado: int) -> list[RostroRegistrado]:
        sql = """
            SELECT id_rostro, id_empleado,
                   COALESCE(angulo,''), COALESCE(calidad, 0),
                   activo, registrado_en, foto_thumb, embedding
              FROM personal.empleado_rostro
             WHERE id_empleado = %s
             ORDER BY registrado_en DESC
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_empleado,))
            filas = cur.fetchall()
        out = []
        for r in filas:
            out.append(RostroRegistrado(
                id_rostro=r[0], id_empleado=r[1],
                angulo=r[2], calidad=r[3],
                activo=r[4], registrado_en=r[5],
                foto_thumb=bytes(r[6]) if r[6] else b"",
                embedding=SvcRostro.deserializar(bytes(r[7])),
            ))
        return out

    def contar_por_empleado(self, id_fundo: int) -> dict[int, int]:
        sql = """
            SELECT er.id_empleado, COUNT(*)
              FROM personal.empleado_rostro er
              JOIN personal.empleado e ON e.id_empleado = er.id_empleado
             WHERE e.id_fundo = %s AND er.activo = TRUE
             GROUP BY er.id_empleado
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return {r[0]: r[1] for r in cur.fetchall()}

    def cargar_todos_para_reconocer(self, id_fundo: int
                                    ) -> list[RostroParaReconocer]:
        """Devuelve todos los embeddings del fundo + datos del empleado.
        Se usa para el reconocimiento en vivo (cache en memoria)."""
        sql = """
            SELECT e.id_empleado,
                   e.apellido_paterno || ' ' || COALESCE(e.apellido_materno,'') ||
                       ' ' || e.nombres,
                   e.codigo,
                   er.embedding
              FROM personal.empleado_rostro er
              JOIN personal.empleado e ON e.id_empleado = er.id_empleado
             WHERE e.id_fundo = %s
               AND er.activo = TRUE
               AND e.estado = 'Activo'
        """
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(sql, (id_fundo,))
            return [
                RostroParaReconocer(
                    id_empleado=r[0],
                    nombre_completo=r[1].strip(),
                    codigo=r[2],
                    embedding=SvcRostro.deserializar(bytes(r[3])),
                )
                for r in cur.fetchall()
            ]

    def eliminar(self, id_rostro: int) -> None:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "DELETE FROM personal.empleado_rostro WHERE id_rostro=%s",
                (id_rostro,),
            )
            conn.commit()

    def eliminar_todos_de_empleado(self, id_empleado: int) -> int:
        with ConexionPostgres().conexion() as conn, conn.cursor() as cur:
            cur.execute(
                "DELETE FROM personal.empleado_rostro WHERE id_empleado=%s",
                (id_empleado,),
            )
            count = cur.rowcount
            conn.commit()
        return count
