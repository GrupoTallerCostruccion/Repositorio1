#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import tkMessageBox as msje


def conectar():
    con = sqlite3.connect('Automotora.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_marcas():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca"
    resultado = c.execute(query)
    marcas = resultado.fetchall()
    con.close()
    return marcas


def obtener_marca_nombre(nombre):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marca WHERE nombre = ?"
    resultado = c.execute(query, [marca])
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


def crear_marca(marca,pais):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO marca (marca,pais)"
        "VALUES (?, ?)")
    c.execute(sql, (rut, nombres, apellidos, correo))
    con.commit()
    msje.showinfo(title="Crear Marca", message="Marca registrada en la bd!")


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















