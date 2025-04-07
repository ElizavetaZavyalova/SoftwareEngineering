CREATE TABLE IF NOT EXISTS passengers_table (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    home_address VARCHAR(255),
    phone VARCHAR(255) NOT NULL
);
