DROP TABLE cities;
DROP TABLE countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    visited BOOLEAN
);
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);
