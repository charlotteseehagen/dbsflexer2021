SELECT data.country_code, country_name, year, max(gdp) AS gdp
	FROM data, country
	WHERE year = 2000 AND gdp IS NOT NULL 
	AND data.country_code = country.country_code
		GROUP BY data.country_code, country_name, year, gdp
		ORDER BY gdp DESC
		LIMIT 10;

SELECT foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name
	FROM (
	SELECT data.country_code,country_name, year, max(gdp) AS gdp
		FROM data, country
		WHERE year = 2000 AND gdp IS NOT NULL 
		AND data.country_code = country.country_code
			GROUP BY data.country_code, country_name,year, gdp
			ORDER BY gdp DESC
			LIMIT 10
	) as foo, data, country 
	WHERE foo.country_code = data.country_code AND data.year >= 2000
		GROUP BY foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name
		ORDER BY foo.country_code DESC,
			 data.year DESC;

SELECT foo.country_code, data.year, data.electricity_production_renewable, data.gdp, foo.country_name
	FROM (
	SELECT data.country_code,country_name, year, max(gdp) AS gdp
		FROM data, country
		WHERE year = 2000 AND gdp IS NOT NULL 
		AND data.country_code = country.country_code
			GROUP BY data.country_code, country_name,year, gdp
			ORDER BY gdp DESC
			LIMIT 10
	) as foo, data, country 
	WHERE foo.country_code = data.country_code AND data.year >= 2000
		GROUP BY foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name,data.electricity_production_renewable
		ORDER BY foo.country_code DESC,
			 data.year DESC;
