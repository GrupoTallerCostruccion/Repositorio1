#!/usr/bin/env python
import sys
import sqlite3

def conectar():
    """conecta base de datos"""
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con

con = conectar()
cursor = con.cursor()

def Buscar_Auto(model,marca,ano):
	con=concetar()
	c= con.cursor
	try:
		query="SELECT* FROM"

def Buscar_Usuario(Usiario):
	"debe retornar la contraseña para comparala en el Login."

"""para la ventana Admin_modelos pide agregar, editar,y eliminar
	 un modelo"""
def agregar_modelo(id,marca,modelo,motor,peso,descripcion,rendimiento,imagen,fecha_creacion,preciolista):
	"""debe agregar un modelo de auto a la base de datos"""
	con = conectar()
	c = con.cursor()
	try:
        query = """INSERT INTO modelo(id,marca_id,modelo,motor,
        	peso,descripcion,rendimiento,imagen,fecha_creacion,precio_lista)
            VALUES (?,?,?,?,?,?,?,?,?)"""
        resultado = c.execute(query,[id,marca,modelo,motor,peso,descripcion,rendimiento,imagen,fecha_creacion,preciolista])
        print "se agrego un producto"
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return index
 def eliminar_modelo(id_modelo):
 	"""elimina un modelo de la tabla de modelos 
 		LE PUSE ID PORQUE ERA LA PK PERO IGUAL PODRIA CAMBIARSE POR MODELO
 """
    exito = False
    con = conectar()
    c = con.cursor()
    query = """DELETE FROM modelo WHERE id = ?"""
    try:
        resultado = c.execute(query,[id_modelo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
def editar_modelo(marca,modelo,motor,peso,descripcion,rendimiento,imagen,fecha_creacion,preciolista,id_mod):
	"""edita un modelo de automobile."""
	con = conectar()
    c = con.cursor()
    try:
        query = """UPDATE modelo SET  marca = ?, motor = ?,
            peso = ?, descripcion = ?, rendimiento = ?, imagen = ?,
            fecha_creacion = ?, preciolista = ? WHERE id_mod= ?"""
        resultado = c.execute(query,[marca,modelo,motor,peso,descripcion,rendimiento,imagen,fecha_creacion,preciolista,id_mod])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return True


#MOSTRARA REGISTROS DE TABLAS
cursor.execute('SELECT id, nombre, pais FROM marca')

for i in cursor:
    print("ID:"),i[0]
    print("Nombre: "),i[1]
    print("Pais: "),i[2],'\n'

print("fin")

con.close()
###FIN MOSTRAR REGISTROS...
