-- Group bands based on country of origin and number of fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY 2 DESC;

