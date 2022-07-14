--Import the database dump from hbtn_0d_tvshows to your MySQL server:
SELECT title FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_showss.id    
WHERE tv_genres.name = "Comedy"
GROUP BY title
ORDER BY title ASC;