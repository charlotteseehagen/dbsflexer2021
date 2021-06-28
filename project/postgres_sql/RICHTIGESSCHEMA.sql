--MEGA DATABASESCHEMA 420 69

DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS co2_emission;
DROP TABLE IF EXISTS gdp;


CREATE TABLE country (
    country_id INT GENERATED ALWAYS AS IDENTITY,
	country_code VARCHAR(3),
	population_total FLOAT,
	population_relative FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (country_id)
);

CREATE TABLE co2_emission (
    co2_id INT GENERATED ALWAYS AS IDENTITY,
	country_code_co2 VARCHAR(3),
	tonnes FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (co2_id),
    CONSTRAINT fk_country
        FOREIGN KEY (country_id)
        REFERENCES country(country_id)
);

CREATE TABLE gdp (
    gdp_id INT GENERATED ALWAYS AS IDENTITY,
	country_code_gdp VARCHAR(3),
	expenses FLOAT,
    education_expenses FLOAT,
    military_expenses FLOAT,
    PRIMARY KEY (gdp_id),
	CONSTRAINT fk_country
        FOREIGN KEY (country_id)
        REFERENCES country(country_id)
);



