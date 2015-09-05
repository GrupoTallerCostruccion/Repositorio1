#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
"manejo_bd para el modulo de clientes"

def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con

def datos_clientes(rut):
    """Obtiene la fila  "rut" en la tabla de clientes."""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM cliente WHERE rut=?"""
        resultado = c.execute(query,[rut])
        print query
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def agregar_cliente(rut,nombre,apellido,telefono,correo):
    """
    Agrega una fila en la tabla clientes con los valores entregados
    """
    con = conectar()
    c = con.cursor()
    try:
        query = """INSERT INTO cliente(rut,
            nombres,apellidos,telefono,correo) VALUES (?,?,?,?,?)"""
        resultado = c.execute(query,[rut,nombre,apellido,telefono,correo])
        print "se agrego un cliente"
    except sqlite3.Error as e:
        exito = False
        print "Error agregar cliente:", e.args[0]
    index = c.fetchall()
    con.commit()
    con.close()
    return index



def editar_cliente(rutID,nombre,apellido,telefono,correo,rut):
    """Edita una fila en la tabla productos con los valores entregados."""
    con = conectar()
    c = con.cursor()
    try:
        print "en el try editar_cliente"
        query = """UPDATE cliente SET  rut = '{}', nombres = '{}',
            apellidos = '{}',telefono = '{}', correo = '{}'
            WHERE rut = '{}' """.format(
                rut,nombre,apellido,telefono,correo,rutID)
        resultado = c.execute(query)
        con.commit()
    except sqlite3.Error as e:
        exito = False
        print "Error editar cliente:", e.args[0]
    index = c.fetchall()
    #con.commit()
    con.close()
    return True

def obtener_clientes():
    """
    Devuelve tablaa de clientes
    """
    con = conectar()
    c = con.cursor()
    prod = None
    query = """SELECT  rut,nombres,apellidos,telefono,correo, 
        COUNT(auto.cliente_rut)  AS "Autos Comprados" 
        FROM cliente
        JOIN auto ON auto.cliente_rut = cliente.rut AND rut>0
        GROUP BY cliente.rut HAVING rut>0"""
    #CREO K EL HAVING ESTA DEMAS
    try:
        resultado = c.execute(query)
        prod = resultado.fetchall()
    except sqlite3.Error as e:
        exito = False
        print "Error obtener cliente:", e.args[0]

    con.close()
    return prod

def obtener_autos():
    """devuelve tablaa de autos"""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM auto"""
        resultado = c.execute(query)
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod


"""
def obtener_clientes():
   
    retorna tabla con datos de cada cliente y suma de autos comprados
  
    con = conectar()
    c = con.cursor()
    query = SELECT cliente.rut,cliente.nombres,cliente.apellidos,
    cliente.telefono,cliente.correo FROM cliente JOIN auto ON 
    
    resultado = c.execute(query)
    cliente = resultado.fetchall()
    con.close()
    return cliente

def obtener_cliente():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM cliente WHERE nombre = ?"
    resultado = c.execute(query)
    clientes = resultado.fetchone()
    con.close()
    return clientes

"""

def crear_cliente(rut,nombres,apellidos,telefono,correo):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO cliente (rut,nombres,apellidos,telefono,correo)"
        "VALUES (?,?,?,?,?)")
    c.execute(sql, (rut, nombres, apellidos, telefono, correo))
    con.commit()
    #msje.showinfo(title="Crear cliente", message="cliente registrada en la bd!")

def eliminar_cliente(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM cliente WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


def buscar_modelos(parametro):
    """
    Retorna tabla con los resultados de busqueda de
    marcas de modelos. Parametro ingresado desde el lineedit de busqueda
    """

    query="""SELECT modelo, marca.nombre AS 'Marca', motor, peso,
    rendimiendo, COUNT(modelo.id) AS "Ventas",  
    fecha_creacion AS Fecha, descripcion, precio_lista
    FROM modelo
    
    LEFT JOIN auto ON modelo.id  = auto.modelo_id 
    LEFT JOIN  marca ON  modelo.marca_id = marca.id WHERE
    
    modelo LIKE '%{}%'  OR Marca LIKE '%{}%'
    OR motor LIKE '%{}%' or peso LIKE '%{}%'
    or Fecha LIKE '%{}%' or precio_lista LIKE '%{}%'
    or descripcion LIKE '%{}%' or rendimiendo LIKE '%{}%'
    
    GROUP BY modelo.id""".format(
        parametro,parametro,parametro,parametro,parametro,parametro,
        parametro,parametro)
    return obtener_query(query)    



def obtener_modelo(nombre):
    """Obtiene la fila en la tabla de  modelos."""
    con = conectar()
    c = con.cursor()
    prod,resultado=None
    try:
        query = """SELECT modelo, marca.nombre AS Marca, motor,
        peso, rendimiendo, COUNT(modelo.id) AS "Ventas",  
        fecha_creacion AS Fecha, descripcion, precio_lista
        FROM modelo WHERE  modelo = ?"""
        resultado = c.execute(query,[nombre])
        
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    prod = resultado.fetchall()
    return prod

    

def obtener_modelos():
    query="""SELECT modelo, marca.nombre AS Marca, motor, peso, rendimiendo, 
    COUNT(modelo.id) AS "Ventas",  
    fecha_creacion AS Fecha, descripcion, precio_lista
    FROM modelo
    LEFT JOIN auto ON auto.modelo_id = modelo.id 
    LEFT JOIN marca ON  modelo.marca_id = marca.id
    GROUP BY modelo.id"""
    return obtener_query(query)

def obtener_query(consulta_sql):
    """
    Genera la tabla deseada ingresando la consulta
    """
    con = conectar()
    c = con.cursor()
    resultado = c.execute(consulta_sql)
    tabla = resultado.fetchall()
    con.close()
    return tabla

def realizar_venta(color,patente,modelo,rut):
    print "hasta aqui todo bien"
    





