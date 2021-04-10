SELECT SUM(city.population) FROM city INNER JOIN country ON city.countrycode=country.code
WHERE CONTINENT ='Asia' ; 