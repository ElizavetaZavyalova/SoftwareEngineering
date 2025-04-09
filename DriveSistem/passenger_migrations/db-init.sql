CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    patronymic TEXT,
    email TEXT UNIQUE NOT NULL,
    pass TEXT NOT NULL,
    home_address TEXT,
    phone TEXT NOT NULL
);
COMMENT ON TABLE passengers IS 'Пассажиры';

COMMENT ON COLUMN passengers.first_name IS 'Имя';
COMMENT ON COLUMN passengers.last_name IS 'Фамилия';
COMMENT ON COLUMN passengers.patronymic IS 'Отчество';
COMMENT ON COLUMN passengers.email IS 'Email';
COMMENT ON COLUMN passengers.pass IS 'Пароль';
COMMENT ON COLUMN passengers.home_address IS 'Домашний адрес';
COMMENT ON COLUMN passengers.phone IS 'Номер телефона';

INSERT INTO passengers (first_name, last_name, patronymic, email, pass, home_address, phone) VALUES
('Иван', 'Иванов', 'Иванович', 'ivanov@example.com', 'pass1234', 'г. Москва, ул. Ленина, д. 10', '+79161234567'),
('Мария', 'Петрова', 'Алексеевна', 'petrova@example.com', 'maria2024', 'г. Санкт-Петербург, ул. Невский, д. 45', '+79261234567'),
('Алексей', 'Сидоров', '-', 'sidorov@example.com', 'qwerty', 'г. Казань, ул. Кремлёвская, д. 7', '+79031234567'),
('Елена', 'Смирнова', 'Викторовна', 'smirnova@example.com', 'elena_pass', '-', '+79051234567'),
('Дмитрий', 'Кузнецов', 'Павлович', 'kuznetsov@example.com', 'securepass', 'г. Екатеринбург, ул. Мира, д. 20', '+79061234567');
CREATE INDEX IF NOT EXISTS idx_passengers_email ON passengers (email);

