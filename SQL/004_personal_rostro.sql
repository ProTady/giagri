-- ============================================================
-- GIAGRI - Reconocimiento facial de empleados (asistencias)
-- ============================================================

CREATE TABLE IF NOT EXISTS personal.empleado_rostro (
    id_rostro      SERIAL PRIMARY KEY,
    id_empleado    INT NOT NULL REFERENCES personal.empleado(id_empleado)
                   ON DELETE CASCADE,
    embedding      BYTEA NOT NULL,            -- vector 512 floats (numpy.tobytes)
    foto_thumb     BYTEA,                     -- JPEG ~100x100
    angulo         VARCHAR(20),               -- 'frente','izquierda','derecha','arriba','abajo'
    calidad        REAL,                      -- score detección (det_score) 0..1
    activo         BOOLEAN NOT NULL DEFAULT TRUE,
    registrado_en  TIMESTAMP NOT NULL DEFAULT NOW(),
    registrado_por INT REFERENCES seguridad.usuario(id_usuario)
);

CREATE INDEX IF NOT EXISTS idx_rostro_empleado
    ON personal.empleado_rostro(id_empleado);

-- Módulo del menú
INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_RECONOCIMIENTO', 'Reconocimiento Facial',
       m.id_modulo, 4
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;
