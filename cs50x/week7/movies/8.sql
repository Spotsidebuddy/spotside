--In 8.sql, write a SQL query to list the names of all people who starred in Toy Story.

SELECT name FROM people, stars, movies
WHERE people.id = stars.person_id
AND movies.id = stars.movie_id
AND title = 'Toy Story';
