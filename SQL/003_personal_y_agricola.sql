-- ============================================================
-- GIAGRI - Schema: personal y agricola
-- Empleados (Personal) y Lotes (Agrícola)
-- ============================================================

CREATE SCHEMA IF NOT EXISTS personal;
CREATE SCHEMA IF NOT EXISTS agricola;

-- ============================================================
-- PERSONAL
-- ============================================================

CREATE TABLE IF NOT EXISTS personal.cargo (
    id_cargo    SERIAL PRIMARY KEY,
    id_fundo    INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    nombre      VARCHAR(80) NOT NULL,
    descripcion VARCHAR(250),
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);

CREATE TABLE IF NOT EXISTS personal.area_trabajo (
    id_area     SERIAL PRIMARY KEY,
    id_fundo    INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    nombre      VARCHAR(80) NOT NULL,
    descripcion VARCHAR(250),
    activo      BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);

CREATE TABLE IF NOT EXISTS personal.empleado (
    id_empleado       SERIAL PRIMARY KEY,
    id_fundo          INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    codigo            VARCHAR(20)  NOT NULL,
    dni               VARCHAR(15)  NOT NULL,
    apellido_paterno  VARCHAR(80)  NOT NULL,
    apellido_materno  VARCHAR(80),
    nombres           VARCHAR(120) NOT NULL,
    fecha_nacimiento  DATE,
    sexo              CHAR(1)      CHECK (sexo IN ('M','F')),
    estado_civil      VARCHAR(20),
    direccion         VARCHAR(250),
    telefono          VARCHAR(20),
    correo            VARCHAR(150),
    fecha_ingreso     DATE         NOT NULL,
    fecha_cese        DATE,
    estado            VARCHAR(20)  NOT NULL DEFAULT 'Activo'
                      CHECK (estado IN ('Activo','Cesado','Vacaciones','Suspendido')),
    id_cargo          INT REFERENCES personal.cargo(id_cargo),
    id_area           INT REFERENCES personal.area_trabajo(id_area),
    sueldo_base       NUMERIC(10,2),
    cuenta_banco      VARCHAR(30),
    banco             VARCHAR(50),
    foto              VARCHAR(250),
    observaciones     TEXT,
    creado_en         TIMESTAMP NOT NULL DEFAULT NOW(),
    actualizado_en    TIMESTAMP,
    UNIQUE (id_fundo, codigo),
    UNIQUE (id_fundo, dni)
);

CREATE INDEX IF NOT EXISTS idx_empleado_fundo  ON personal.empleado(id_fundo);
CREATE INDEX IF NOT EXISTS idx_empleado_estado ON personal.empleado(estado);
CREATE INDEX IF NOT EXISTS idx_empleado_apels  ON personal.empleado(apellido_paterno, apellido_materno);


-- ============================================================
-- AGRICOLA
-- ============================================================

CREATE TABLE IF NOT EXISTS agricola.tipo_cultivo (
    id_tipo_cultivo  SERIAL PRIMARY KEY,
    id_fundo         INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    nombre           VARCHAR(80) NOT NULL,
    nombre_cientifico VARCHAR(120),
    activo           BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);

CREATE TABLE IF NOT EXISTS agricola.variedad (
    id_variedad      SERIAL PRIMARY KEY,
    id_tipo_cultivo  INT NOT NULL REFERENCES agricola.tipo_cultivo(id_tipo_cultivo),
    nombre           VARCHAR(80) NOT NULL,
    descripcion      VARCHAR(250),
    activo           BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_tipo_cultivo, nombre)
);

CREATE TABLE IF NOT EXISTS agricola.patron (
    id_patron        SERIAL PRIMARY KEY,
    id_tipo_cultivo  INT NOT NULL REFERENCES agricola.tipo_cultivo(id_tipo_cultivo),
    nombre           VARCHAR(80) NOT NULL,
    descripcion      VARCHAR(250),
    activo           BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (id_tipo_cultivo, nombre)
);

CREATE TABLE IF NOT EXISTS agricola.lote (
    id_lote                  SERIAL PRIMARY KEY,
    id_fundo                 INT NOT NULL REFERENCES seguridad.fundo(id_fundo),
    codigo                   VARCHAR(30)  NOT NULL,
    nombre                   VARCHAR(100) NOT NULL,
    id_tipo_cultivo          INT REFERENCES agricola.tipo_cultivo(id_tipo_cultivo),
    id_variedad              INT REFERENCES agricola.variedad(id_variedad),
    id_patron                INT REFERENCES agricola.patron(id_patron),
    hectareas                NUMERIC(10,4) NOT NULL DEFAULT 0,
    fecha_siembra            DATE,
    fecha_inicio_produccion  DATE,
    densidad_plantas         INT,
    total_plantas            INT,
    distancia_entre_plantas  NUMERIC(5,2),
    distancia_entre_filas    NUMERIC(5,2),
    sistema_riego            VARCHAR(50)
                             CHECK (sistema_riego IS NULL
                                    OR sistema_riego IN ('Goteo','Aspersion','Gravedad','Microaspersion')),
    estado                   VARCHAR(30) NOT NULL DEFAULT 'Activo'
                             CHECK (estado IN ('Activo','Inactivo','Erradicado','En desarrollo')),
    observaciones            TEXT,
    creado_en                TIMESTAMP NOT NULL DEFAULT NOW(),
    actualizado_en           TIMESTAMP,
    UNIQUE (id_fundo, codigo)
);

CREATE INDEX IF NOT EXISTS idx_lote_fundo   ON agricola.lote(id_fundo);
CREATE INDEX IF NOT EXISTS idx_lote_estado  ON agricola.lote(estado);
CREATE INDEX IF NOT EXISTS idx_lote_cultivo ON agricola.lote(id_tipo_cultivo);


-- ============================================================
-- MÓDULOS DEL MENÚ (sub-items de PERSONAL y LOTES)
-- ============================================================

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_LISTA', 'Empleados', m.id_modulo, 1
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_CARGOS', 'Cargos', m.id_modulo, 2
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'PERSONAL_AREAS', 'Áreas de Trabajo', m.id_modulo, 3
  FROM seguridad.modulo m WHERE m.codigo = 'PERSONAL'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'LOTES_LISTA', 'Lotes', m.id_modulo, 1
  FROM seguridad.modulo m WHERE m.codigo = 'LOTES'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'LOTES_CULTIVOS', 'Tipos de Cultivo', m.id_modulo, 2
  FROM seguridad.modulo m WHERE m.codigo = 'LOTES'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'LOTES_VARIEDADES', 'Variedades', m.id_modulo, 3
  FROM seguridad.modulo m WHERE m.codigo = 'LOTES'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'LOTES_PATRONES', 'Patrones', m.id_modulo, 4
  FROM seguridad.modulo m WHERE m.codigo = 'LOTES'
ON CONFLICT (codigo) DO NOTHING;


-- ============================================================
-- CATÁLOGOS PRECARGADOS (FUNDO01)
-- ============================================================

-- Cargos
INSERT INTO personal.cargo (id_fundo, nombre)
SELECT f.id_fundo, c.nombre
  FROM seguridad.fundo f
 CROSS JOIN (VALUES
    ('Jefe de Campo'),
    ('Ingeniero Agrónomo'),
    ('Supervisor'),
    ('Caporal'),
    ('Tractorista'),
    ('Operario'),
    ('Almacenero'),
    ('Mecánico'),
    ('Administrativo')
 ) AS c(nombre)
 WHERE f.codigo = 'FUNDO01'
ON CONFLICT (id_fundo, nombre) DO NOTHING;

-- Áreas de trabajo
INSERT INTO personal.area_trabajo (id_fundo, nombre)
SELECT f.id_fundo, a.nombre
  FROM seguridad.fundo f
 CROSS JOIN (VALUES
    ('Campo'),
    ('Oficina'),
    ('Almacén'),
    ('Planta de Empaque'),
    ('Maestranza'),
    ('Riego')
 ) AS a(nombre)
 WHERE f.codigo = 'FUNDO01'
ON CONFLICT (id_fundo, nombre) DO NOTHING;

-- Tipos de cultivo
INSERT INTO agricola.tipo_cultivo (id_fundo, nombre, nombre_cientifico)
SELECT f.id_fundo, t.nombre, t.cientifico
  FROM seguridad.fundo f
 CROSS JOIN (VALUES
    ('Palto',     'Persea americana'),
    ('Uva',       'Vitis vinifera'),
    ('Mango',     'Mangifera indica'),
    ('Espárrago', 'Asparagus officinalis'),
    ('Arándano',  'Vaccinium corymbosum'),
    ('Granado',   'Punica granatum')
 ) AS t(nombre, cientifico)
 WHERE f.codigo = 'FUNDO01'
ON CONFLICT (id_fundo, nombre) DO NOTHING;

-- Variedades por tipo de cultivo
WITH tc AS (
  SELECT id_tipo_cultivo, nombre
    FROM agricola.tipo_cultivo
   WHERE id_fundo = (SELECT id_fundo FROM seguridad.fundo WHERE codigo='FUNDO01')
)
INSERT INTO agricola.variedad (id_tipo_cultivo, nombre)
SELECT tc.id_tipo_cultivo, v.nombre
  FROM tc
  JOIN (VALUES
    ('Palto', 'Hass'), ('Palto', 'Fuerte'), ('Palto', 'Lamb Hass'),
    ('Uva', 'Red Globe'), ('Uva', 'Crimson'), ('Uva', 'Sugraone'), ('Uva', 'Thompson'),
    ('Mango', 'Kent'), ('Mango', 'Edward'), ('Mango', 'Haden'), ('Mango', 'Tommy Atkins'),
    ('Espárrago', 'UC-157'), ('Espárrago', 'Atlas'),
    ('Arándano', 'Biloxi'), ('Arándano', 'Ventura'), ('Arándano', 'Emerald'),
    ('Granado', 'Wonderful')
  ) AS v(cultivo, nombre) ON tc.nombre = v.cultivo
ON CONFLICT (id_tipo_cultivo, nombre) DO NOTHING;

-- Patrones por tipo de cultivo
WITH tc AS (
  SELECT id_tipo_cultivo, nombre
    FROM agricola.tipo_cultivo
   WHERE id_fundo = (SELECT id_fundo FROM seguridad.fundo WHERE codigo='FUNDO01')
)
INSERT INTO agricola.patron (id_tipo_cultivo, nombre)
SELECT tc.id_tipo_cultivo, p.nombre
  FROM tc
  JOIN (VALUES
    ('Palto', 'Zutano'), ('Palto', 'Duke 7'), ('Palto', 'Topa Topa'),
    ('Uva', '110-R'), ('Uva', 'Salt Creek'), ('Uva', 'Freedom'),
    ('Mango', 'Criollo'), ('Mango', 'Manila')
  ) AS p(cultivo, nombre) ON tc.nombre = p.cultivo
ON CONFLICT (id_tipo_cultivo, nombre) DO NOTHING;
