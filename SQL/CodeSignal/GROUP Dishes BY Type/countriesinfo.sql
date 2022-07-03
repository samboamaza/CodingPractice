#Your friend wants to become a professional tour guide and travel all around the world. In pursuit of this dream, she enrolled in tour guide school. The professors in this school 
turned out to be very demanding, and one of them gave your friend a difficult assignment that she has to finish over the weekend.

Here's the task: Given a list of countries, your friend should calculate the average population and total population of all the countries in the list.
To help her, you have decided to write a function that will calculate the required values for any number of countries. The countries table in which the 
countries are stored has the following structure:

name: the name of the country;
continent: the continent on which the country is situated;
population: the population of the country.
Your task is to return a new table that contains the number of countries in the given list, along with their average and total population, in columns 
titled number, average and total#


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	select count(name) as number, avg(population) as average, sum(population) as total
	from countries;
END
