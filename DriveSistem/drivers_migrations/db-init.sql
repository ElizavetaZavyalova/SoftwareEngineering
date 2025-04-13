CREATE TABLE IF NOT EXISTS drivers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    requisites VARCHAR(255),
    car_number VARCHAR(255),
    phone VARCHAR(255) NOT NULL
);
COMMENT ON TABLE drivers IS 'Водители';

COMMENT ON COLUMN drivers.first_name IS 'Имя';
COMMENT ON COLUMN drivers.last_name IS 'Фамилия';
COMMENT ON COLUMN drivers.patronymic IS 'Отчество';
COMMENT ON COLUMN drivers.email IS 'Email';
COMMENT ON COLUMN drivers.pass IS 'Пароль';
COMMENT ON COLUMN drivers.requisites IS 'Счет оплаты';
COMMENT ON COLUMN drivers.car_number IS 'Номер машины';
COMMENT ON COLUMN drivers.phone IS 'Номер телефона';
-- # pass1:dDuRt/dOoJ.ZPEcMZupLxt/4uE0iQWi
-- # pass2:5Cj1aWZw9FBxFK1jP2A.M7d45tHq2Eq
-- # pass3:HBq9Yr4q65m9HZXaUmUkeqDZ8lFzkWm
-- # pass4:ywSUrIlF1S1x6c0MHo3JWZPnEuhZVRG
-- # pass5:gL04niB8snn46iisH1aS/VJWP6R4VPW
INSERT INTO drivers (first_name, last_name, patronymic, email, pass, requisites, car_number, phone) VALUES
('Сергей', 'Михайлов', 'Анатольевич', 'mihailov@example.com', 'dDuRt/dOoJ.ZPEcMZupLxt/4uE0iQWi', 'Счет №40817810099910004312', 'А123ВС77', '+79991234567'),
('Анна', 'Козлова', 'Игоревна', 'kozlova@example.com', '5Cj1aWZw9FBxFK1jP2A.M7d45tHq2Eq', 'Счет №40817810444420005566', 'В456ЕР78', '+79992223344'),
('Павел', 'Фёдоров', 'Михайлович', 'fedorov@example.com', 'HBq9Yr4q65m9HZXaUmUkeqDZ8lFzkWm', 'Счет №40817810888830006677', 'С789КН99', '+79993334455'),
('Ольга', 'Соколова', 'Владимировна', 'sokolova@example.com', 'ywSUrIlF1S1x6c0MHo3JWZPnEuhZVRG', 'Счет №408178108888304444', 'М321ОР77', '+79994445566'),
('Игорь', 'Никитин', 'Дмитриевич', 'nikitin@example.com', 'gL04niB8snn46iisH1aS/VJWP6R4VPW', 'Счет №40817810123450007890', 'М301ОР77' , '+79995556677');

CREATE INDEX IF NOT EXISTS idx_drivers_email ON drivers (email);