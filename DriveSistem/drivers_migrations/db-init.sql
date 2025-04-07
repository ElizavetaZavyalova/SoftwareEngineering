CREATE TABLE IF NOT EXISTS drivers_table (
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
