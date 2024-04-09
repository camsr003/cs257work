DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime timestamp with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  id text,
  place text
);
