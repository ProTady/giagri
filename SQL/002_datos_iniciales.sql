-- ============================================================
-- GIAGRI - Datos iniciales
-- Fundo demo + usuario admin + módulos base del menú
-- ============================================================

-- Fundo demo
INSERT INTO seguridad.fundo (codigo, nombre)
VALUES ('FUNDO01', 'Fundo Demo')
ON CONFLICT (codigo) DO NOTHING;

-- Usuario admin
-- Contraseña inicial: "admin123" (cambiar en primer login)
-- Hash bcrypt generado con: bcrypt.hashpw(b"admin123", bcrypt.gensalt())
INSERT INTO seguridad.usuario
    (id_fundo, username, password_hash, nombre_completo, es_admin)
SELECT
    f.id_fundo,
    'admin',
    '$2b$12$LQv3c1yqBwEHFl5aGQH3fO8Z5uQK1xJj5sH4yN8VZ.4yZ3xH9wWqW',
    'Administrador',
    TRUE
FROM seguridad.fundo f
WHERE f.codigo = 'FUNDO01'
ON CONFLICT (id_fundo, username) DO NOTHING;

-- Módulos base (menú principal)
INSERT INTO seguridad.modulo (codigo, nombre, icono, padre_id, orden) VALUES
    ('ADMIN',         'Administración',   'admin.png',     NULL, 1),
    ('PERSONAL',      'Personal',         'personal.png',  NULL, 2),
    ('LOTES',         'Lotes',            'lote.png',      NULL, 3),
    ('PRODUCCION',    'Producción',       'prod.png',      NULL, 4),
    ('RIEGO',         'Riego',            'riego.png',     NULL, 5),
    ('SANIDAD',       'Sanidad',          'sanidad.png',   NULL, 6),
    ('COSTOS',        'Costos',           'costos.png',    NULL, 7),
    ('MAESTRANZA',    'Maestranza',       'maestr.png',    NULL, 8),
    ('SSOMA',         'SSOMA',            'ssoma.png',     NULL, 9)
ON CONFLICT (codigo) DO NOTHING;

-- Submódulos de Administración
INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'ADMIN_USUARIOS', 'Usuarios', m.id_modulo, 1
FROM seguridad.modulo m WHERE m.codigo = 'ADMIN'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'ADMIN_ROLES', 'Roles y Permisos', m.id_modulo, 2
FROM seguridad.modulo m WHERE m.codigo = 'ADMIN'
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO seguridad.modulo (codigo, nombre, padre_id, orden)
SELECT 'ADMIN_FUNDO', 'Datos del Fundo', m.id_modulo, 3
FROM seguridad.modulo m WHERE m.codigo = 'ADMIN'
ON CONFLICT (codigo) DO NOTHING;
