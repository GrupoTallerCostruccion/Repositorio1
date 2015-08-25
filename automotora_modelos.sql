



INSERT INTO marca VALUES(48, "DAIHATSU", "Japon")
INSERT INTO modelo VALUES(121,48, "MODEL X9..","motor ABC1", 1231,"sd","12km/l","imagen","fecha","lista")

DELETE FROM marca WHERE marca.id = 48
DELETE FROM modelo WHERE modelo.marca_id=48
DELETE FROM imagen WHERE imagen.modelo_marca_id =48
DELETE FROM auto WHERE auto.modelo_marca_id = 48