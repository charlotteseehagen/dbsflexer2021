--MEGA DATABASESCHEMA 420 69

CREATE TABLE country (
	country_code VARCHAR(3),
	population_total FLOAT,
	population_relative FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (country_code),
);

CREATE TABLE co2_emission (
	country_code_co2 VARCHAR(3),
	tonnes FLOAT,
    year INTEGER NOT NULL,
    PRIMARY KEY (country_code_co2),
		
);

CREATE TABLE gdp (
	country_code_gdp VARCHAR(3),
	expenses FLOAT,
    education_expenses FLOAT,
    military_expenses FLOAT,
    PRIMARY KEY (country_code_gdp),
	
);


ALTER TABLE co2_emission
    ADD CONSTRAINT foreign_country_code_co2
    FOREIGN KEY (country_code) REFERENCES country


ALTER TABLE gdp
    ADD CONSTRAINT foreign_country_code_gdp
    FOREIGN KEY (country_code) REFERENCES country

)
