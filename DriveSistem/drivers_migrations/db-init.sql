CREATE TABLE IF NOT EXISTS drivers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL COMMENT 'Имя',
    last_name VARCHAR(255) NOT NULL COMMENT 'Фамилия',
    patronymic VARCHAR(255) COMMENT 'Отчество',
    email VARCHAR(255) UNIQUE NOT NULL COMMENT 'Email',
    pass VARCHAR(255) NOT NULL COMMENT 'Пароль',
    requisites VARCHAR(255) COMMENT 'Счет оплаты',
    car_number VARCHAR(255) COMMENT 'Номер машины',
    phone VARCHAR(255) NOT NULL COMMENT 'Номер телефона'
);
COMMENT ON TABLE drivers IS 'Водители';

INSERT INTO drivers (first_name, last_name, patronymic, email, pass, requisites, car_number, phone) VALUES
('Сергей', 'Михайлов', 'Анатольевич', 'mihailov@example.com', 'driver123', 'Счет №40817810099910004312', 'А123ВС77', '+79991234567'),
('Анна', 'Козлова', 'Игоревна', 'kozlova@example.com', 'passanna', 'Счет №40817810444420005566', 'В456ЕР78', '+79992223344'),
('Павел', 'Фёдоров', '-', 'fedorov@example.com', 'securepavel', 'Счет №40817810888830006677', 'С789КН99', '+79993334455'),
('Ольга', 'Соколова', 'Владимировна', 'sokolova@example.com', 'olgapass', '-', 'М321ОР77', '+79994445566'),
('Игорь', 'Никитин', 'Дмитриевич', 'nikitin@example.com', 'password2024', 'Счет №40817810123450007890', 'М301ОР77' , '+79995556677');

CREATE INDEX IF NOT EXISTS idx_drivers_email ON drivers (email);