CREATE TABLE CO2emission (
	CountryCode(Co2) INTEGER NOT NULL,
	Tonnes INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (CountryCode(Co2)), 
	FOREIGN KEY (CountryCode) REFERENCES country(CountryCode)
);

CREATE TABLE country (
	CountryCode INTEGER NOT NULL,
	Population_Total INTEGER,
	Population_Relative INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (Country Code),
	FOREIGN KEY (CountryCode(gdp)) REFERENCES gdp(CountryCode(gdp))
	FOREIGN KEY (CountryCode(Co2)) REFERENCES CO2emission(CountryCode(Co2))
);

CREATE TABLE gdp (
	CountryCode(gdp) INTEGER NOT NULL,
	Expenses INTEGER,
      EducationExpenses INTEGER,
      MilitaryExpenses INTEGER,
      PRIMARY KEY (CountryCode(gdp)),
	FOREIGN KEY (CountryCode) REFERENCES country(CountryCode)
);
