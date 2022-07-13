--
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;