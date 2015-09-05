#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje
from array import *

def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    c=[con.cursor(),con]
    return c


def consulta_claves():
    c = conectar()
    query = "SELECT * FROM usuario"
    resultado = c[0].execute(query)
    print query
    print resultado
    prod = resultado.fetchall()
    print prod 
    return prod