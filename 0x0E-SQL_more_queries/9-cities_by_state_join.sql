-- Lists all the cities in a database
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s
ON c.`state_id` = s.`id`
ORDER BY c.id;
