-- Delete related records from the players_coaches table
DELETE FROM players_coaches
WHERE player_id IN (
    SELECT id
    FROM players
    WHERE hire_date < '2013-12-13 07:18:46'
);

-- Delete players from the players table
DELETE FROM players
WHERE hire_date < '2013-12-13 07:18:46';
