-- ============================================================
-- GIAGRI - Tareo diario, actividades, labores y bonos
-- Base para el módulo de Planilla (siguiente sesión)
-- ============================================================

-- Régimen laboral del empleado
ALTER TABLE personal.empleado
    ADD COLUMN IF NOT EXISTS regimen VARCHAR(20) NOT NULL DEFAULT 'Agrario'
    CHECK (regimen IN ('Agrario', 'General', 'Otros'));

-- ----------------------------------------------------------------
-- Catálogos
-- ----------------------------------------------------------------
CREATE TABLE IF NOT EXISTS personal.actividad (
    id_actividad  SERIAL PRIMARY KEY,
    id_fundo      INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    nombre        VARCHAR(80) NOT NULL,
    descripcion   VARCHAR(250),
    activo        BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);

CREATE TABLE IF NOT EXISTS personal.labor (
    id_labor       SERIAL PRIMARY KEY,
    id_fundo       INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    id_actividad   INT REFERENCES personal.actividad(id_actividad),
    codigo         VARCHAR(20),
    nombre         VARCHAR(120) NOT NULL,
    descripcion    VARCHAR(250),
    bono_por_hora  NUMERIC(10,2) NOT NULL DEFAULT 0,
    activo         BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);
CREATE INDEX IF NOT EXISTS idx_labor_actividad ON personal.labor(id_actividad);

-- ----------------------------------------------------------------
-- Tareo diario
-- ----------------------------------------------------------------
CREATE TABLE IF NOT EXISTS personal.tareo (
    id_tareo        SERIAL PRIMARY KEY,
    id_fundo        INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    id_empleado     INT NOT NULL REFERENCES personal.empleado(id_empleado),
    fecha           DATE NOT NULL,
    id_cargo        INT REFERENCES personal.cargo(id_cargo),
    id_lote         INT REFERENCES agricola.lote(id_lote),
    id_labor        INT REFERENCES personal.labor(id_labor),
    id_actividad    INT REFERENCES personal.actividad(id_actividad),
    horas_manana    NUMERIC(4,2) NOT NULL DEFAULT 0,
    horas_tarde     NUMERIC(4,2) NOT NULL DEFAULT 0,
    horas_extras    NUMERIC(4,2) NOT NULL DEFAULT 0,
    horas_total     NUMERIC(4,2) GENERATED ALWAYS AS
                    (horas_manana + horas_tarde + horas_extras) STORED,
    comentario      TEXT,
    creado_por      INT REFERENCES seguridad.usuario(id_usuario),
    creado_en       TIMESTAMP NOT NULL DEFAULT NOW(),
    actualizado_en  TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tareo_fecha
    ON personal.tareo(fecha);
CREATE INDEX IF NOT EXISTS idx_tareo_empleado_fecha
    ON personal.tareo(id_empleado, fecha);
CREATE INDEX IF NOT EXISTS idx_tareo_lote
    ON personal.tareo(id_lote);
CREATE INDEX IF NOT EXISTS idx_tareo_labor
    ON personal.tareo(id_labor);

-- ----------------------------------------------------------------
-- Módulos del menú
-- ----------------------------------------------------------------
INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_TAREO', 'Tareo Diario', m.id_modulo, 5
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_ACTIVIDADES', 'Actividades', m.id_modulo, 6
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_LABORES', 'Labores y Bonos', m.id_modulo, 7
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

-- ----------------------------------------------------------------
-- Catálogos precargados
-- ----------------------------------------------------------------
INSERT INTO personal.actividad (id_fundo, nombre)
SELECT f.id_fundo, a.nombre
  FROM seguridad.fundo f
 CROSS JOIN (VALUES
    ('Riego'),
    ('Sanidad'),
    ('Cosecha'),
    ('Poda'),
    ('Fertilización'),
    ('Mantenimiento'),
    ('Preparación de Terreno'),
    ('Cultural'),
    ('Empaque'),
    ('Otros')
 ) AS a(nombre)
 WHERE f.codigo = 'FUNDO01'
ON CONFLICT (id_fundo, nombre) DO NOTHING;

-- Algunas labores típicas precargadas (sin bono por defecto)
WITH act AS (
  SELECT id_actividad, nombre
    FROM personal.actividad
   WHERE id_fundo = (SELECT id_fundo FROM seguridad.fundo WHERE codigo='FUNDO01')
),
ff AS (SELECT id_fundo FROM seguridad.fundo WHERE codigo='FUNDO01')
INSERT INTO personal.labor (id_fundo, id_actividad, nombre)
SELECT ff.id_fundo, act.id_actividad, l.nombre
  FROM ff
  CROSS JOIN (VALUES
    ('Riego',          'Riego por goteo'),
    ('Riego',          'Riego por gravedad'),
    ('Riego',          'Limpieza de cintas'),
    ('Sanidad',        'Aplicación foliar'),
    ('Sanidad',        'Monitoreo de plagas'),
    ('Cosecha',        'Cosecha manual'),
    ('Cosecha',        'Acopio en campo'),
    ('Poda',           'Poda de formación'),
    ('Poda',           'Poda de fructificación'),
    ('Poda',           'Despunte'),
    ('Fertilización',  'Aplicación al suelo'),
    ('Fertilización',  'Fertirriego'),
    ('Mantenimiento',  'Limpieza de calles'),
    ('Mantenimiento',  'Reparación de cercos'),
    ('Cultural',       'Deshierbo manual'),
    ('Cultural',       'Raleo'),
    ('Cultural',       'Amarre'),
    ('Empaque',        'Selección'),
    ('Empaque',        'Embalaje')
  ) AS l(actividad, nombre)
  JOIN act ON act.nombre = l.actividad
ON CONFLICT (id_fundo, nombre) DO NOTHING;
