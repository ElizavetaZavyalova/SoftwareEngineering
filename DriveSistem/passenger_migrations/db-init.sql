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
-- # pass1:dDuRt/dOoJ.ZPEcMZupLxt/4uE0iQWi
-- # pass2:5Cj1aWZw9FBxFK1jP2A.M7d45tHq2Eq
-- # pass3:HBq9Yr4q65m9HZXaUmUkeqDZ8lFzkWm
-- # pass4:ywSUrIlF1S1x6c0MHo3JWZPnEuhZVRG
-- # pass5:gL04niB8snn46iisH1aS/VJWP6R4VPW
INSERT INTO passengers (first_name, last_name, patronymic, email, pass, home_address, phone) VALUES
('Иван', 'Иванов', 'Иванович', 'ivanov@example.com', 'dDuRt/dOoJ.ZPEcMZupLxt/4uE0iQWi', 'г. Москва, ул. Ленина, д. 10', '+79161234567'),
('Мария', 'Петрова', 'Алексеевна', 'petrova@example.com', '5Cj1aWZw9FBxFK1jP2A.M7d45tHq2Eq', 'г. Санкт-Петербург, ул. Невский, д. 45', '+79261234567'),
('Алексей', 'Сидоров', 'Викторович', 'sidorov@example.com', 'HBq9Yr4q65m9HZXaUmUkeqDZ8lFzkWm', 'г. Казань, ул. Кремлёвская, д. 7', '+79031234567'),
('Елена', 'Смирнова', 'Викторовна', 'smirnova@example.com', 'ywSUrIlF1S1x6c0MHo3JWZPnEuhZVRG', 'г. Казань, ул. Кружик, д. 7', '+79051234567'),
('Дмитрий', 'Кузнецов', 'Павлович', 'kuznetsov@example.com', 'gL04niB8snn46iisH1aS/VJWP6R4VPW', 'г. Екатеринбург, ул. Мира, д. 20', '+79061234567');
CREATE INDEX IF NOT EXISTS idx_passengers_email ON passengers (email);

