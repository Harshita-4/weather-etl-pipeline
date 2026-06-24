CREATE TABLE IF NOT EXISTS weather_data (
    id          SERIAL PRIMARY KEY,
    city        VARCHAR(100),
    country     VARCHAR(10),
    temperature FLOAT,
    feels_like  FLOAT,
    humidity    INT,
    pressure    INT,
    weather     VARCHAR(200),
    wind_speed  FLOAT,
    fetched_at  TIMESTAMP
);
