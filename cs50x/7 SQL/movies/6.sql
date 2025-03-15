--In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.

SELECT AVG(rating) FROM ratings, movies WHERE ratings.movie_id = movies.id AND year = 2012;
