CREATE TABLE IF NOT EXISTS radar_index ( 
    id SERIAL PRIMARY KEY,
    datetime timestamp NOT NULL UNIQUE,
    filename VARCHAR NOT NULL
);
SELECT AddGeometryColumn('public', 'radar_index', 'geom', 3857, 'POLYGON', 2);
