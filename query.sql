--first query

SELECT TOP_SCORER_NAME,
 MAX(GOALS) AS MOST_GOALS
 FROM SEASON
 GROUP BY top_scorer_name;



--second query

select winner_name, round((count(winner_name))/(select count(*) from season)*100, 2) persent
from season
group by winner_name
order by persent DESC , winner_name;




--third query

select season_year, max(goals) as  goals
from season
group by season_year
order by season_year;