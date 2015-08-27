#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje


def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    c = con.cursor()
    return c

def obtener_query(consulta_sql):
    """
    Genera la tabla deseada ingresando la consulta
    """
    c = conectar()
    resultado = c.execute(consulta_sql)
    tabla = resultado.fetchall()
    c.close()
    return tabla

def borrar_elemento(tabla, nombre_columna, parametro):
    """
    Borra una celda de una tabla, ingresando
    el nombre de la tabla, columna y parametro a buscar y borrar
    """
    exito = False
    cursor = conectar()
    query = "DELETE FROM ", tabla," WHERE ",nombre_columna," = ?"
    print (query)
    try:
        resultado = c.execute(query, [parametro])
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
    query = """SELECT *, COUNT(cliente.rut)  AS "Autos Comprados" FROM cliente
    JOIN auto ON auto.cliente_rut = cliente.rut
    GROUP BY cliente.rut"""
    return obtener_query(query)

def obtener_modelos():
    query="""SELECT *, COUNT(*) AS "Ventas" FROM modelo
    JOIN auto ON  auto.modelo_id = modelo.id
    GROUP BY modelo.id"""
    return obtener_query(query)

#####################################
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


















