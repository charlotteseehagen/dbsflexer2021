--MEGA DATABASESCHEMA 420 69
CREATE TABLE country (
	country_code VARCHAR(3),
	population_total FLOAT,
	population_relative FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (country_code)
    FOREIGN KEY (country_code_co2) REFERENCES co2_emission(country_code_co2)
    FOREIGN KEY (country_code_gdp) REFERENCES gdp(country_code_gdp)
);

CREATE TABLE co2_emission (
	country_code_co2 VARCHAR(3),
	tonnes FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (country_code_co2)	
    FOREIGN KEY (country_code) REFERENCES country(country_code)	
);

CREATE TABLE gdp (
	country_code_gdp VARCHAR(3),
	expenses FLOAT,
    education_expenses FLOAT,
    military_expenses FLOAT,
    PRIMARY KEY (country_code_gdp)
    FOREIGN KEY (country_code) REFERENCES country(country_code)	
);
