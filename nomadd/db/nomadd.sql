DROP TABLE countries;
DROP TABLE cities;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)
);




