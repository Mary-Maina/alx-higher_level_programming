-- Lists all records where score is above 10
-- Ensure records are in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
