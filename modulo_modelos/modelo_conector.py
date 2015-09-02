#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje


def conectar():
    con = sqlite3.connect('../Automotora.db')
    con.row_factory = sqlite3.Row
    return con

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

def borrar_elemento(tabla, nombre_columna, parametro):
    """
    Borra una celda de una tabla, ingresando
    el nombre de la tabla, columna y parametro a buscar y borrar
    """
    exito = False
    cursor = conectar()
    query = "DELETE FROM {} WHERE {} = '{}'".format(
        tabla,nombre_columna,parametro)
    print (query)
    try:
        resultado = cursor.execute(query)
        cursor.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    cursor.close()
    return exito



def obtener_marcas():
    query = """SELECT marca.nombre AS 'Nombre de Marca',
    marca.pais AS 'País de Origen',COUNT(marca.id)AS 'Cantidad de Modelos'
    FROM marca JOIN modelo
    ON modelo.marca_id = marca.id
    GROUP BY marca.id"""
    return obtener_query(query)

def obtener_clientes():
    query = """SELECT *, COUNT(cliente.rut)  AS"Autos Comprados"
    FROM cliente
    JOIN auto ON auto.cliente_rut = cliente.rut
    GROUP BY cliente.rut"""
    return obtener_query(query)

def obtener_modelos():
    query="""SELECT modelo, marca.nombre AS Marca, motor, peso, rendimiendo, 
    COUNT(modelo.id) AS "Ventas",  
    fecha_creacion AS Fecha, descripcion, precio_lista
    FROM modelo, auto, marca
    WHERE auto.modelo_id = modelo.id AND
    modelo.marca_id = marca.id
    GROUP BY modelo.id"""
    return obtener_query(query)

#####################################

def buscar_modelos(parametro):
    """
    Retorna tabla con los resultados de busqueda de
    marcas de modelos. Parametro ingresado desde el lineedit de busqueda
    """

    query="""SELECT modelo, marca.nombre AS Marca, motor, peso,
    rendimiendo, COUNT(modelo.id) AS "Ventas",  
    fecha_creacion AS Fecha, descripcion, precio_lista
    FROM modelo, auto, marca
    
    WHERE auto.modelo_id = modelo.id AND
    modelo.marca_id = marca.id AND
    
    Marca LIKE '%{}%' OR modelo LIKE '%{}%'
    OR motor LIKE '%{}%' or peso LIKE '%{}%'
    or Fecha LIKE '%{}%' or precio_lista LIKE '%{}%'
    or descripcion LIKE '%{}%' or rendimiendo LIKE '%{}%'
    GROUP BY modelo.id""".format(
        parametro,parametro,parametro,parametro,parametro,parametro,
        parametro,parametro)
    return obtener_query(query)    

def obtener_marca_nombre(nombre):
    c = conectar()
    query = "SELECT * FROM marca WHERE nombre = ?"
    resultado = c.execute(query, [marca])
    marcas = resultado.fetchone()
    con.close()
    return marcas

def obtener_marca_pais(pais):
    c = conectar()
    query = "SELECT * FROM marca WHERE pais = ?"
    resultado = c.execute(query, [pais])
    marcas = resultado.fetchone()
    con.close()
    return marcas

def crear_marca(marca,pais):
    c = conectar()
    sql = (
        "INSERT INTO marca (marca,pais)"
        "VALUES (?, ?)")
    c.execute(sql, (rut, nombres, apellidos, correo))
    con.commit()
    msje.showinfo(title="Crear Marca", message="Marca registrada en la bd!")


















