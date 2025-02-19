--In 9.sql, write a SQL query to list the names of all people who
--starred in a movie released in 2004, ordered by birth year.

SELECT name FROM people, stars, movies
WHERE people.id = stars.person_id
AND movies.id = stars.movie_id
AND year = 2004
ORDER BY birth ASC;
