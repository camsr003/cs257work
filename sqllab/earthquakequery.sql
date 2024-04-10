-- shows all earthquakes that occured near Japan
SELECT * FROM earthquakes WHERE place LIKE '%Japan' ORDER BY mag DESC;

-- shows all earthquakes that occured on the west side of the US
SELECT * FROM earthquakes WHERE longitude BETWEEN -130 AND -110 AND latitude BETWEEN 40 AND 45 ORDER BY mag DESC;

-- shows all earthquakes that occured near Hawaii
SELECT * FROM earthquakes WHERE longitude BETWEEN -160 AND -155 AND latitude between 19 AND 23 ORDER BY mag DESC;
