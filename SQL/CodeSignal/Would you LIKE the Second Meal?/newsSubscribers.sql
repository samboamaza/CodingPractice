CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT DISTINCT subscriber
    FROM
    (
        SELECT *
        FROM full_year
            UNION
        SELECT *
        FROM half_year
    ) x
    WHERE newspaper LIKE "%Daily%"
    ORDER BY subscriber ASC;
END
