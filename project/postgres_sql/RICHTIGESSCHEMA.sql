--MEGA DATABASESCHEMA 420 69
CREATE TABLE country (
	country_code VARCHAR(3),
	population_total FLOAT,
	population_relative FLOAT,
    year INTEGER NOT NULL,
<<<<<<< HEAD:project/dataschema.sql
    PRIMARY KEY (country_code),
	
=======
    PRIMARY KEY (country_code)
>>>>>>> 1d044c21ab443cbb5fccf3a062db34bfc1d8304a:project/postgres_sql/RICHTIGESSCHEMA.sql
);

CREATE TABLE co2_emission (
	country_code_co2 VARCHAR(3),
	tonnes FLOAT,
    year INTEGER NOT NULL,
<<<<<<< HEAD:project/dataschema.sql
    PRIMARY KEY (country_code_co2),
		
=======
    PRIMARY KEY (country_code_co2)	
>>>>>>> 1d044c21ab443cbb5fccf3a062db34bfc1d8304a:project/postgres_sql/RICHTIGESSCHEMA.sql
);

CREATE TABLE gdp (
	country_code_gdp VARCHAR(3),
	expenses FLOAT,
    education_expenses FLOAT,
    military_expenses FLOAT,
<<<<<<< HEAD:project/dataschema.sql
    PRIMARY KEY (country_code_gdp),
	
);


ALTER TABLE
    co2_emission
ADD CONSTRAINT
    foreign_country_code
FOREIGN KEY (country_code) REFERENCES country

ALTER TABLE
    gdp
ADD CONSTRAINT
    foreign_country_code
FOREIGN KEY (country_code) REFERENCES country
=======
    PRIMARY KEY (country_code_gdp)
);
>>>>>>> 1d044c21ab443cbb5fccf3a062db34bfc1d8304a:project/postgres_sql/RICHTIGESSCHEMA.sql
