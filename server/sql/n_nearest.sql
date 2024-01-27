-- Parameters for the target coordinates and the number of nearest locations (customize as needed)
DECLARE @Privacy_lat FLOAT = ...; -- Replace with the target latitude
DECLARE @Privacy_lon FLOAT = ...; -- Replace with the target longitude
DECLARE @n INT = ...; -- Replace with the number of nearest locations you want

-- Query to find the n nearest locations
SELECT TOP (@n) uf.id, uf.Privacy_lat, uf.Privacy_lon
FROM Ufarms uf
ORDER BY (
    (uf.Lat - @target_lat) * (uf.Lat - @target_lat) +
    (uf.Lon - @target_lon) * (uf.Lon - @target_lon)
);
