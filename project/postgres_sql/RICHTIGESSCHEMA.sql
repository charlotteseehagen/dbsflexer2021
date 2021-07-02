--MEGA DATABASESCHEMA 420 69

DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS data;


CREATE TABLE country (
	country_code VARCHAR(3),
	country_name VARCHAR(255),
    PRIMARY KEY (country_code)
);

CREATE TABLE data (
    country_code VARCHAR(3),
    year INT,
    co2_emission FLOAT,
    gdp FLOAT,
    population_relative FLOAT,
    population_total FLOAT,
    electricity_production_renewable FLOAT,
    PRIMARY KEY (country_code, year)
);

        
