--In 7.sql, write a SQL query to list all movies released in 2010 and their ratings,
--in descending order by rating. For movies with the same rating, order them alphabetically by title.

SELECT title, rating
FROM movies, ratings
WHERE movies.id = ratings.movie_id
AND year = 2010
ORDER BY rating DESC, title;
