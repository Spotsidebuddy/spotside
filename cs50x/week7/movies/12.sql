--In 12.sql, write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.

SELECT title FROM movies WHERE id IN
(SELECT movie_id FROM stars WHERE movie_id IN
(SELECT DISTINCT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Bradley Cooper'))
AND person_id = (SELECT id FROM people WHERE name = 'Jennifer Lawrence'));
