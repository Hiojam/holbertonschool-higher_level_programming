-- Lists all shows contained in "hbtn_0d_tvshows" that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE EXISTS (
    SELECT 1
    FROM tv_show_genres AS sg
    WHERE sg.tv_show_id = tv_shows.id
)
ORDER BY tv_shows.title, tv_show_genres.genre_id;