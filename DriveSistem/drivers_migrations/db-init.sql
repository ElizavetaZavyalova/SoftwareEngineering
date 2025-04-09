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

INSERT INTO drivers (first_name, last_name, patronymic, email, pass, requisites, car_number, phone) VALUES
('Сергей', 'Михайлов', 'Анатольевич', 'mihailov@example.com', 'driver123', 'Счет №40817810099910004312', 'А123ВС77', '+79991234567'),
('Анна', 'Козлова', 'Игоревна', 'kozlova@example.com', 'passanna', 'Счет №40817810444420005566', 'В456ЕР78', '+79992223344'),
('Павел', 'Фёдоров', 'Михайлович', 'fedorov@example.com', 'securepavel', 'Счет №40817810888830006677', 'С789КН99', '+79993334455'),
('Ольга', 'Соколова', 'Владимировна', 'sokolova@example.com', 'olgapass', 'Счет №408178108888304444', 'М321ОР77', '+79994445566'),
('Игорь', 'Никитин', 'Дмитриевич', 'nikitin@example.com', 'password2024', 'Счет №40817810123450007890', 'М301ОР77' , '+79995556677');

CREATE INDEX IF NOT EXISTS idx_drivers_email ON drivers (email);