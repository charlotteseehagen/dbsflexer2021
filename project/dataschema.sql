CREATE TABLE CO2 emission (
	Country Code(Co2) INTEGER NOT NULL,
	Tonnes INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (Country Code(Co2)), 
);

CREATE TABLE country (
	Country Code INTEGER NOT NULL,
	Population_Total INTEGER,
	Population_Relative INTEGER,
      Year INTEGER NOT NULL,
      PRIMARY KEY (Country Code),
);

CREATE TABLE gdp (
	Country Code(gdp) INTEGER NOT NULL,
	Expenses INTEGER,
	Energy imports INTEGER,
      Education Expenses INTEGER,
      Military Expenses INTEGER,
      PRIMARY KEY (Country Code(gdp)),
);
