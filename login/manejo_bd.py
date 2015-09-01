#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje
from array import *

def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con


def consulta_clave(nombre):
    """Obtiene la fila  "rut" en la tabla de clientes."""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT pass FROM usuario WHERE id=?"""
        resultado = c.execute(query,[nombre])
        print query
        print resultado
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    print prod 
    return prod