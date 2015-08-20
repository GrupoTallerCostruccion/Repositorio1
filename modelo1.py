#!/usr/bin/env python
import sys
import sqlite3


con =  sqlite3.connect('C:\\automotora\\bd\\Automotora.db')
cursor = con.cursor()

#MOSTRARA REGISTROS DE TABLAS
cursor.execute('SELECT id, nombre, pais FROM marca')

for i in cursor:
    print("ID:"),i[0]
    print("Nombre: "),i[1]
    print("Pais: "),i[2],'\n'

print("fin")

con.close()
###FIN MOSTRAR REGISTROS...
