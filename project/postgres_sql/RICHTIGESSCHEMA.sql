--MEGA DATABASESCHEMA 420 69

DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS data;


CREATE TABLE country (
	country_code VARCHAR(3),
	country_name VARCHAR(255),
    continent VARCHAR(25),
    PRIMARY KEY (country_code)
);

CREATE TABLE data (
    country_code VARCHAR(3),
    year INT,
    gdp FLOAT,
    co2_emission FLOAT,
    expenses FLOAT,
    population_total FLOAT,
    population_relative FLOAT,
    electricity_production_renewable FLOAT,
    PRIMARY KEY (country_code, year)
);

        
