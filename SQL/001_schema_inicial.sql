-- ============================================================
-- GIAGRI - Esquema inicial
-- Multi-fundo, usuarios, roles y permisos por módulo
-- ============================================================

CREATE SCHEMA IF NOT EXISTS seguridad;

-- ----- Fundo (multi-tenant) -----
CREATE TABLE IF NOT EXISTS seguridad.fundo (
    id_fundo        SERIAL PRIMARY KEY,
    codigo          VARCHAR(20)  UNIQUE NOT NULL,
    nombre          VARCHAR(150) NOT NULL,
    ruc             VARCHAR(20),
    direccion       VARCHAR(250),
    telefono        VARCHAR(30),
    activo          BOOLEAN      NOT NULL DEFAULT TRUE,
    creado_en       TIMESTAMP    NOT NULL DEFAULT NOW()
);

-- ----- Usuario -----
CREATE TABLE IF NOT EXISTS seguridad.usuario (
    id_usuario      SERIAL PRIMARY KEY,
    id_fundo        INT          NOT NULL REFERENCES seguridad.fundo(id_fundo),
    username        VARCHAR(50)  NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,         -- bcrypt
    nombre_completo VARCHAR(150) NOT NULL,
    correo          VARCHAR(150),
    es_admin        BOOLEAN      NOT NULL DEFAULT FALSE,
    activo          BOOLEAN      NOT NULL DEFAULT TRUE,
    creado_en       TIMESTAMP    NOT NULL DEFAULT NOW(),
    ultimo_acceso   TIMESTAMP,
    UNIQUE (id_fundo, username)
);

-- ----- Rol -----
CREATE TABLE IF NOT EXISTS seguridad.rol (
    id_rol      SERIAL PRIMARY KEY,
    id_fundo    INT          NOT NULL REFERENCES seguridad.fundo(id_fundo),
    nombre      VARCHAR(80)  NOT NULL,
    descripcion VARCHAR(250),
    activo      BOOLEAN      NOT NULL DEFAULT TRUE,
    UNIQUE (id_fundo, nombre)
);

-- ----- Módulo (árbol del menú) -----
CREATE TABLE IF NOT EXISTS seguridad.modulo (
    id_modulo   SERIAL PRIMARY KEY,
    codigo      VARCHAR(60)  UNIQUE NOT NULL,      -- p.ej. 'RIEGO_CAUDAL'
    nombre      VARCHAR(120) NOT NULL,
    icono       VARCHAR(120),
    padre_id    INT REFERENCES seguridad.modulo(id_modulo) ON DELETE CASCADE,
    orden       INT          NOT NULL DEFAULT 0,
    activo      BOOLEAN      NOT NULL DEFAULT TRUE
);

-- ----- Permiso (rol x módulo) -----
CREATE TABLE IF NOT EXISTS seguridad.permiso (
    id_rol      INT NOT NULL REFERENCES seguridad.rol(id_rol)       ON DELETE CASCADE,
    id_modulo   INT NOT NULL REFERENCES seguridad.modulo(id_modulo) ON DELETE CASCADE,
    ver         BOOLEAN NOT NULL DEFAULT FALSE,
    crear       BOOLEAN NOT NULL DEFAULT FALSE,
    editar      BOOLEAN NOT NULL DEFAULT FALSE,
    eliminar    BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id_rol, id_modulo)
);

-- ----- Usuario x Rol -----
CREATE TABLE IF NOT EXISTS seguridad.usuario_rol (
    id_usuario  INT NOT NULL REFERENCES seguridad.usuario(id_usuario) ON DELETE CASCADE,
    id_rol      INT NOT NULL REFERENCES seguridad.rol(id_rol)         ON DELETE CASCADE,
    PRIMARY KEY (id_usuario, id_rol)
);

-- ----- Auditoría de accesos -----
CREATE TABLE IF NOT EXISTS seguridad.acceso_log (
    id_acceso   BIGSERIAL PRIMARY KEY,
    id_usuario  INT REFERENCES seguridad.usuario(id_usuario),
    accion      VARCHAR(40) NOT NULL,    -- LOGIN_OK, LOGIN_FAIL, LOGOUT
    ip          VARCHAR(45),
    detalle     VARCHAR(250),
    fecha       TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_usuario_fundo  ON seguridad.usuario(id_fundo);
CREATE INDEX IF NOT EXISTS idx_modulo_padre   ON seguridad.modulo(padre_id);
CREATE INDEX IF NOT EXISTS idx_acceso_fecha   ON seguridad.acceso_log(fecha);
