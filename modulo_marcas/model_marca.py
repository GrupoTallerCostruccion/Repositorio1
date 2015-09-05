#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje


def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_marcas():
    """
    Función que carga la información de marcas en una tabla,
    incluyendo la cantidad de modelos asociados a la marca
    """
    con = conectar()
    c = con.cursor()
    query = """SELECT marca.nombre AS 'Nombre de Marca', 
    marca.pais AS 'Pais de Origen',COUNT(marca.id)   
    AS 'Cantidad de Modelos'   
    FROM marca LEFT JOIN modelo 
    ON  marca.id =  modelo.marca_id 
    GROUP BY marca.id"""
    resultado = c.execute(query)
    marcas = resultado.fetchall()
    con.close()
    return marcas

def obtener_marca(nombre):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca WHERE nombre = ?"
    resultado = c.execute(query, [nombre])
    marcas = resultado.fetchone()
    con.close()
    return marcas

def obtener_marca_pais(pais):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca WHERE pais = ?"
    resultado = c.execute(query, [pais])
    marcas = resultado.fetchone()
    con.close()
    return marcas

def editar_marca(marca_orig,marca_editada,pais):
    con = conectar()
    c = con.cursor()
    #query = "UPDATE marca SET nombre = ",marca_inicial,
    #" , pais = ",pais," WHERE nombre = ",marca_inicial
    query = (
        "UPDATE marca SET nombre = ? ,pais = ? "
        "WHERE nombre = ? ")
    c.execute(query, (marca_editada,pais,marca_orig))
    con.commit()

    
def crear_marca(marca,pais):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO marca (nombre,pais) "
        "VALUES (?, ?)")
    c.execute(sql, (marca,pais))
    con.commit()
    

def borrar(nombre_marca):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM marca WHERE nombre = ?"
    try:
        resultado = c.execute(query, [nombre_marca])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito















