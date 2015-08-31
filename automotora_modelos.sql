INSERT INTO imagen (archivo,modelo_id,modelo_marca_id)VALUES("imgVehiculos/bmw3.png","10","1")





INSERT INTO imagen VALUES (3,"imagen/yaris.png", 5,5)

SELECT *, COUNT(*) AS "Ventas" FROM modelo
JOIN auto ON  auto.modelo_id = modelo.id GROUP BY modelo.id

SELECT marca.nombre,marca.pais, COUNT(marca.id) AS "Cantidad de Modelos" FROM marca 
JOIN modelo ON modelo.marca_id = marca.id GROUP BY marca.id


-------DUDA: la columna imágen de la tabla modelos debecontener la direccion de la imagen  o el id a la "imagen" de la tabla imagen??------------
UPDATE modelo SET imagen="3" WHERE id = 5
--------------------------------------
INSERT INTO marca VALUES(48, "DAIHATSU", "Japon")
INSERT INTO modelo VALUES(121,48, "MODEL X9..","motor ABC1", 1231,"sd","12km/l","imagen","fecha","lista")

SELECT *, COUNT(*) AS "Ventas" FROM modelo
JOIN auto ON  auto.modelo_id = modelo.id GROUP BY modelo.id JOIN marcas ON 

SELECT modelo, marca.nombre, motor, peso, COUNT(modelo.id) AS "Ventas" FROM modelo, auto, marca
WHERE auto.modelo_id = modelo.id AND
modelo.marca_id = marca.id
GROUP BY modelo.id

DELETE FROM marca WHERE marca.id = 48
DELETE FROM modelo WHERE modelo.marca_id=48
DELETE FROM imagen WHERE imagen.modelo_marca_id =48
DELETE FROM auto WHERE auto.modelo_marca_id = 48