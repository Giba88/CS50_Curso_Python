
/* --POSTGRESS
CREATE TABLE flights(
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

--CREATE INDEX 
-- HAVING ... LIMIT 10 => TOP 10
*/

/*--SQL Server
CREATE TABLE voos(
    id INT IDENTITY(1, 1) PRIMARY KEY,
    origem VARCHAR(255) NOT NULL,
    destino VARCHAR(255) NOT NULL,
    duracao INTEGER NOT NULL
);
*/

/*
INSERT INTO voos(origem, destino, duracao) VALUES ('New York', 'London', 415)
INSERT INTO voos(origem, destino, duracao) VALUES ('Shanghai', 'Paris', 760)
INSERT INTO voos(origem, destino, duracao) VALUES ('Istanbul', 'Tokyo', 700)
INSERT INTO voos(origem, destino, duracao) VALUES ('New York', 'Paris', 435)
INSERT INTO voos(origem, destino, duracao) VALUES ('Moscow', 'Paris', 245)
INSERT INTO voos(origem, destino, duracao) VALUES ('Lima', 'New York', 455)
*/
SELECT * FROM VOOS
SELECT AVG(DURACAO) MEDIA_TEMPO, ORIGEM FROM VOOS WHERE ORIGEM LIKE '%O%' GROUP BY ORIGEM
