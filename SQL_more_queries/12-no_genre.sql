-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT x.name AS genre,COUNT(*) AS number_of_shows
FROM tv_show_genres AS z
INNER JOIN tv_genres AS x
ON x.id =z.genre_id
GROUP BY x.name
ORDER BY number_of_shows DESC;
