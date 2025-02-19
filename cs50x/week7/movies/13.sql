--In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT name FROM people JOIN stars ON stars.person_id = people.id
WHERE movie_id IN (
    SELECT movie_id FROM stars WHERE person_id = (
        SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958
        )
    )
AND id != (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958);
