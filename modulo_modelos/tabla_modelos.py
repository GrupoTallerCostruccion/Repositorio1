# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_modelos.ui'
#
# Created: Thu Aug 27 05:38:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 388)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName("label")
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(150, 330, 223, 43))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtGui.QPushButton(self.frame)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_borrar = QtGui.QPushButton(self.frame)
        self.btn_borrar.setObjectName("btn_borrar")
        self.horizontalLayout.addWidget(self.btn_borrar)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 511, 281))
        self.tableView.setObjectName("tableView")
        self.buscar = QtGui.QLineEdit(Form)
        self.buscar.setGeometry(QtCore.QRect(420, 10, 113, 20))
        self.buscar.setInputMask("")
        self.buscar.setReadOnly(False)
        self.buscar.setObjectName("buscar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Tabla de Modelos de Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Form", "Agregar/Editar Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_borrar.setText(QtGui.QApplication.translate("Form", "Eliminar Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar.setPlaceholderText(QtGui.QApplication.translate("Form", "Búsqueda por Marca", None, QtGui.QApplication.UnicodeUTF8))

