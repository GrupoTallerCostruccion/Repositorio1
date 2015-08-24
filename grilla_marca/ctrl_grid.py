#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_grid import Ui_Grid
import model_marca as db_marcas


class Main(QtGui.QWidget):
    """
    Esta es una grilla
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Grid()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_edit.clicked.connect(self.edit)

    def add(self):
        self.ui.form = FormAlumno(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de marcas en la grilla
        """
        marcas = db_marcas.obtener_marcas()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(marcas), 3)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"id"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Nombre de Marca"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"País de Origen"))

        for r, row in enumerate(alumnos):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['id'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['Nombre de Marca'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['País de Origen'])

        self.ui.table.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.table.horizontalHeader().setResizeMode(
            1, self.ui.table.horizontalHeader().Stretch)
        self.ui.table.horizontalHeader().setResizeMode(
            2, self.ui.table.horizontalHeader().Stretch)

        self.ui.table.setColumnWidth(0, 100)
        self.ui.table.setColumnWidth(1, 210)
        self.ui.table.setColumnWidth(2, 210)

    def delete(self):
        """
        Función que intenta borrar un alumno de la base de datos e
        indica el resultado de la operación
        """

        # ANTES DE REALIZAR LA ACCIÓN SE DEBERÍA PREGUNTAR
        # AL USUARIO CONFIRMAR LA OPERACIÓN !!!!!!!!!!!!!!
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
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
        """
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormAlumno(self, rut)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
