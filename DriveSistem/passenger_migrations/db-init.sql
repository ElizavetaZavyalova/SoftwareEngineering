CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL COMMENT 'Имя',
    last_name VARCHAR(255) NOT NULL COMMENT 'Фамилия',
    patronymic VARCHAR(255) COMMENT 'Отчество',
    email VARCHAR(255) UNIQUE NOT NULL COMMENT 'Email',
    pass VARCHAR(255) NOT NULL COMMENT 'Пароль',
    home_address VARCHAR(255) COMMENT 'Домашний адрес',
    phone VARCHAR(255) NOT NULL COMMENT 'Номер телефона'
);
COMMENT ON TABLE passengers IS 'Пассажиры';

INSERT INTO passengers (first_name, last_name, patronymic, email, pass, home_address, phone) VALUES
('Иван', 'Иванов', 'Иванович', 'ivanov@example.com', 'pass1234', 'г. Москва, ул. Ленина, д. 10', '+79161234567'),
('Мария', 'Петрова', 'Алексеевна', 'petrova@example.com', 'maria2024', 'г. Санкт-Петербург, ул. Невский, д. 45', '+79261234567'),
('Алексей', 'Сидоров', '-', 'sidorov@example.com', 'qwerty', 'г. Казань, ул. Кремлёвская, д. 7', '+79031234567'),
('Елена', 'Смирнова', 'Викторовна', 'smirnova@example.com', 'elena_pass', '-', '+79051234567'),
('Дмитрий', 'Кузнецов', 'Павлович', 'kuznetsov@example.com', 'securepass', 'г. Екатеринбург, ул. Мира, д. 20', '+79061234567');
CREATE INDEX IF NOT EXISTS idx_passengers_email ON passengers (email);

