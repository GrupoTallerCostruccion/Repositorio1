#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje


def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_clientes():
    """
    retorna tabla con datos de cada cliente y suma de autos comprados
    """
    con = conectar()
    c = con.cursor()
    query = """SELECT cliente.rut,cliente.nombres,cliente.apellidos,
    cliente.telefono,cliente.correo FROM cliente JOIN auto ON """
    resultado = c.execute(query)
    cliente = resultado.fetchall()
    con.close()
    return cliente

"""
def obtener_cliente(nombre):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM cliente WHERE nombre = ?"
    resultado = c.execute(query, [cliente])
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
    c.execute(sql, (rut, nombres, apellidos, correo))
    con.commit()
    msje.showinfo(title="Crear cliente", message="cliente registrada en la bd!")

def borrar(rut):
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















