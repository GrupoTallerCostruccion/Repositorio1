#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje
from array import *
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
    print rut
    print nombre
    """Agrega una fila en la tabla clientes con los valores entregados."""
    con = conectar()
    c = con.cursor()
    try:
        query = """INSERT INTO cliente(rut,
            nombres,apellidos,telefono,correo) VALUES (?,?,?,?,?)"""
        resultado = c.execute(query,[rut,nombre,apellido,telefono,correo])
        print "se agrego un producto"
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return index



def editar_cliente(nombre,apellido,telefono,correo,rut):
    """Edita una fila en la tabla productos con los valores entregados."""
    con = conectar()
    c = con.cursor()
    try:
        query = """UPDATE cliente SET  nombres = ?, apellidos = ?,
            telefono = ?, correo = ?,  WHERE rut = ?"""
        resultado = c.execute(query,[nombre,apellido,telefono,correo,rut])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return True

def obtener_clientes():
    """devuelve tablaa de clientes"""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM cliente"""
        resultado = c.execute(query)
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
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
    msje.showinfo(title="Crear cliente", message="cliente registrada en la bd!")

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















