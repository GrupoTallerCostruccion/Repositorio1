#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow
import model_marca as db_marcas


class Main(QtGui.QMainWindow):
    """
    Esta es una grilla
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.agregar_marca.clicked.connect(self.add)
        #self.ui.eliminar_marca.connect(self.delete)

    def add(self):
        self.ui.form = FormAlumno(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de marcas en la grilla
        incluyendo la cantidad de modelos asociados a la marca
        """
        marcas = db_marcas.obtener_marcas()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(marcas)+1, 3)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"Nombre de Marca"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"País de Origen"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Cantidad de Modelos"))

        for r, row in enumerate(marcas):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['Nombre de Marca'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['País de Origen'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['Cantidad de Modelos'])

        self.ui.tabla_marcas.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.tabla_marcas.horizontalHeader().setResizeMode(
            0, self.ui.tabla_marcas.horizontalHeader().Stretch)
        self.ui.tabla_marcas.horizontalHeader().setResizeMode(
            1, self.ui.tabla_marcas.horizontalHeader().Stretch)

        self.ui.tabla_marcas.setColumnWidth(0, 100)
        self.ui.tabla_marcas.setColumnWidth(1, 210)
        self.ui.tabla_marcas.setColumnWidth(2, 210)

    def delete(self):
        """
        Función que intenta borrar un alumno de la base de datos e
        indica el resultado de la operación
        """

        # ANTES DE REALIZAR LA ACCIÓN SE DEBERÍA PREGUNTAR
        # AL USUARIO CONFIRMAR LA OPERACIÓN !!!!!!!!!!!!!!
        data = self.ui.tabla_marcas.model()
        index = self.ui.tabla_marcas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            if tkMessageBox.askyesno(
                "Borrar Marca", "Deseas borrar esta marca?"):
                marca = data.index(
                    index.row(), 0, QtCore.QModelIndex()).data()
                if (db_marcas.borrar(marca)):
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
        
        data = self.ui.tabla_marcas.model()
        index = self.ui.tabla_marcas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormAlumno(self, rut)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
        """
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
