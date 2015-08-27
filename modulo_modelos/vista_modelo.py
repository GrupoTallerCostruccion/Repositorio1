#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from tabla_modelos import Ui_Form
import modelo_conector as db
#from python -m Repositorio1 import modelo_conector as db
#from ctrl_form import FormModelos


class Main(QtGui.QMainWindow):
    """
    Esta es una grilla
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.btn_agregar.clicked.connect(self.add)
        #self.ui.btn_borrar.connect(self.delete)
        #self.ui.buscar.connect(self.filtrar_modelos)

    def add(self):
        #self.ui.form = FormMarca(self)
        #self.ui.form.accepted.connect(self.load_data)
        #self.ui.form.show()
        pass
    def filtrar_modelos(self):
        pass

    def load_data(self):
        """
        Función que carga la información de modelos en la grilla
        incluyendo la cantidad de modelos asociados a la marca
        """
        modelos = db.obtener_modelos()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(modelos)+1, 10)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"marca_id"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Modelo"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Motor"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"Peso"))
        self.data.setHorizontalHeaderItem(
            4, QtGui.QStandardItem(u"Descripcion"))
        self.data.setHorizontalHeaderItem(
            5, QtGui.QStandardItem(u"Rendimiento"))
        self.data.setHorizontalHeaderItem(
            6, QtGui.QStandardItem(u"Imagen"))
        self.data.setHorizontalHeaderItem(
            7, QtGui.QStandardItem(u"Fecha"))
        self.data.setHorizontalHeaderItem(
            8, QtGui.QStandardItem(u"Precio"))
        self.data.setHorizontalHeaderItem(
            9, QtGui.QStandardItem(u"Ventas"))

        for r, row in enumerate(modelos):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['marca_id'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['Modelo'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['Motor'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['Peso'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['Descripcion'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['Rendimiento'])
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row['Imagen'])
            index = self.data.index(r, 7, QtCore.QModelIndex())
            self.data.setData(index, row['Fecha'])
            index = self.data.index(r, 8, QtCore.QModelIndex())
            self.data.setData(index, row['Precio'])
            index = self.data.index(r, 9, QtCore.QModelIndex())
            self.data.setData(index, row['Ventas'])

        self.ui.tabla_modelos.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.tabla_modelos.horizontalHeader().setResizeMode(
            0, self.ui.tabla_modelos.horizontalHeader().Stretch)
        self.ui.tabla_modelos.horizontalHeader().setResizeMode(
            1, self.ui.tabla_modelos.horizontalHeader().Stretch)

        self.ui.tabla_modelos.setColumnWidth(0, 100)
        self.ui.tabla_modelos.setColumnWidth(1, 210)
        self.ui.tabla_modelos.setColumnWidth(2, 210)

    def delete(self):
        """
        Función que intenta borrar un alumno de la base de datos e
        indica el resultado de la operación
        """

        # ANTES DE REALIZAR LA ACCIÓN SE DEBERÍA PREGUNTAR
        # AL USUARIO CONFIRMAR LA OPERACIÓN !!!!!!!!!!!!!!
        data = self.ui.tabla_modelos.model()
        index = self.ui.tabla_modelos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            if tkMessageBox.askyesno(
                "Borrar Marca", "Deseas borrar esta marca?"):
                marca = data.index(
                    index.row(), 0, QtCore.QModelIndex()).data()
                if (db.borrar(marca)):
                    self.load_data()
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText(u"EL registro fue eliminado.")
                    msgBox.exec_()
                    return True
                else:
                    self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                    self.ui.errorMessageDialog.showMessage(
                        u"Error al eliminar el registro")
                    return False

    ########### rehacer..
    def edit(self):
        """
        Función obtiene el alumno seleccionado en la grilla
        para poner sus datos en el formulario para su edición
        """
        data = self.ui.tabla_modelos.model()
        index = self.ui.tabla_modelos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            nom_marca = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormMarca(self, nom_marca)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
