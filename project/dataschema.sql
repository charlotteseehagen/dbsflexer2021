
CREATE TABLE country (
	country_code INTEGER NOT NULL,
	population_total INTEGER,
	population_relative INTEGER,
      year INTEGER NOT NULL,
      PRIMARY KEY (country_code),
	
)

CREATE TABLE co2_emission (
	country_code_co2 INTEGER NOT NULL,
	tonnes INTEGER,
      year INTEGER NOT NULL,
      PRIMARY KEY (country_code_co2), 
		
)

CREATE TABLE gdp (
	country_code_gdp INTEGER NOT NULL,
	expenses INTEGER,
      education_expenses INTEGER,
      military_expenses INTEGER,
      PRIMARY KEY (country_code_gdp),
	
)
