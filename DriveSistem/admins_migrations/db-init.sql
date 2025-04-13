CREATE TABLE IF NOT EXISTS admins (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);
COMMENT ON TABLE admins IS 'Админестраторы';

COMMENT ON COLUMN admins.first_name IS 'Имя';
COMMENT ON COLUMN admins.last_name IS 'Фамилия';
COMMENT ON COLUMN admins.patronymic IS 'Отчество';
COMMENT ON COLUMN admins.email IS 'Email';
COMMENT ON COLUMN admins.pass IS 'Пароль';
COMMENT ON COLUMN admins.phone IS 'Номер телефона';
-- admin:12w/m81itNBaKxNG/AZzaB5lMPiIWPq
INSERT INTO admins (first_name, last_name, patronymic, email, pass, phone) VALUES
('Админ', 'Админов', 'Админович', 'admin@admin.com', '12w/m81itNBaKxNG/AZzaB5lMPiIWPq', '+79990001122');
CREATE INDEX IF NOT EXISTS idx_admins_email ON admins (email);