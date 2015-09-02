# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_modelos.ui'
#
# Created: Wed Sep 02 16:28:28 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(692, 401)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(130, 340, 281, 43))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtGui.QPushButton(self.frame)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_editar = QtGui.QPushButton(self.frame)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout.addWidget(self.btn_editar)
        self.btn_borrar = QtGui.QPushButton(self.frame)
        self.btn_borrar.setObjectName("btn_borrar")
        self.horizontalLayout.addWidget(self.btn_borrar)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 431, 281))
        self.tableView.setObjectName("tableView")
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.buscar = QtGui.QLineEdit(Dialog)
        self.buscar.setGeometry(QtCore.QRect(320, 20, 113, 20))
        self.buscar.setInputMask("")
        self.buscar.setReadOnly(False)
        self.buscar.setObjectName("buscar")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(460, 40, 221, 331))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.foto_siguiente = QtGui.QPushButton(self.frame_2)
        self.foto_siguiente.setGeometry(QtCore.QRect(130, 290, 75, 23))
        self.foto_siguiente.setObjectName("foto_siguiente")
        self.foto_anterior = QtGui.QPushButton(self.frame_2)
        self.foto_anterior.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.foto_anterior.setObjectName("foto_anterior")
        self.foto = QtGui.QLabel(self.frame_2)
        self.foto.setGeometry(QtCore.QRect(10, 60, 191, 191))
        self.foto.setObjectName("foto")
        self.galeria = QtGui.QLabel(self.frame_2)
        self.galeria.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.galeria.setObjectName("galeria")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Dialog", "Agregar Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_borrar.setText(QtGui.QApplication.translate("Dialog", "Eliminar Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Búsqueda", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Tabla de Modelos de Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.foto_siguiente.setText(QtGui.QApplication.translate("Dialog", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))
        self.foto_anterior.setText(QtGui.QApplication.translate("Dialog", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.foto.setText(QtGui.QApplication.translate("Dialog", "Seleccione Modelo de auto", None, QtGui.QApplication.UnicodeUTF8))
        self.galeria.setText(QtGui.QApplication.translate("Dialog", "Galeria del Modelo*", None, QtGui.QApplication.UnicodeUTF8))

