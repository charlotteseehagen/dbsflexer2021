CREATE TABLE CO2_emission (
	Country_Code_Co2 INTEGER NOT NULL,
	Tonnes INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (Country_Code_Co2), 
	FOREIGN KEY (Country_Code) REFERENCES country(Country_Code)
);

CREATE TABLE country (
	Country_Code INTEGER NOT NULL,
	Population_Total INTEGER,
	Population_Relative INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (Country_Code),
	FOREIGN KEY (Country_Code_gdp) REFERENCES gdp(CountryCode_gdp)
	FOREIGN KEY (Country_Code_Co2) REFERENCES CO2_emission(Country_Code_Co2)
);

CREATE TABLE gdp (
	Country_Code_gdp INTEGER NOT NULL,
	Expenses INTEGER,
      EducationExpenses INTEGER,
      MilitaryExpenses INTEGER,
      PRIMARY KEY (Country_Code_gdp),
	FOREIGN KEY (Country_Code) REFERENCES country(Country_Code)
);
