-- list all metal bands with Glam rock as their main style, ranked by longevity
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY 2 DESC;
