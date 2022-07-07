/*Your company hired an intern database engineer, who immediately started updating the data in the system. Unfortunately, he hasn't fully grasped the concept of NULL values yet and he performed some incorrect 
inserts and updates to the departments table, which has the following structure:

id: the unique department ID;
name: the name of the department;
description: the description of the department.
Now you have a table where the description column holds values such as '  NULL   ', NULL, 'nil' and ' - '. You need to find out exactly how many records 
in the table should have NULL in the description column, regardless of whether the intern input the value correctly or not.

He used the following values to indicate NULL:

NULL: just a regular NULL value;
'<spaces>NULL<spaces>': NULL as a case insensitive (i.e. NuLl is also OK) string with an arbitrary number of spaces at the beginning and at the end;
'<spaces>nil<spaces>': nil as a case insensitive (i.e. niL is also OK) string with an arbitrary number of spaces at the beginning and at the end;
'<spaces>-<spaces>': a single dash with an arbitrary number of spaces at the beginning and at the end.
Given the departments table, compose the resulting table with the single column number_of_nulls containing a single value: the number of rows in the 
departments table that are supposed to have NULL in the description.*/

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	select count(id) as number_of_nulls
	from departments
	where description is null
	or trim(description) in ('nil','-','null');
END
