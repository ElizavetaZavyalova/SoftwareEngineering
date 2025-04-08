CREATE TABLE IF NOT EXISTS admins(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL COMMENT 'Имя',
    last_name VARCHAR(255) NOT NULL COMMENT 'Фамилия',
    patronymic VARCHAR(255) COMMENT 'Отчество',
    email VARCHAR(255) UNIQUE NOT NULL COMMENT 'Email',
    pass VARCHAR(255) NOT NULL COMMENT 'Пароль',
    phone VARCHAR(255) NOT NULL COMMENT 'Номер телефона'
);
COMMENT ON TABLE admins IS 'Админестраторы';

INSERT INTO admins (first_name, last_name, patronymic, email, pass, phone) VALUES
('Админ', 'Админов', 'Админович', 'admin@admin.com', 'admin', '+79990001122');
CREATE INDEX IF NOT EXISTS idx_admins_email ON admins (email);