# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_marca.ui'
#
# Created: Thu Aug 27 04:07:30 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 216)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 20, 301, 141))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.campo_pais = QtGui.QLineEdit(self.frame)
        self.campo_pais.setGeometry(QtCore.QRect(130, 70, 131, 20))
        self.campo_pais.setObjectName("campo_pais")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label.setObjectName("label")
        self.campo_nombre = QtGui.QLineEdit(self.frame)
        self.campo_nombre.setGeometry(QtCore.QRect(130, 20, 131, 20))
        self.campo_nombre.setObjectName("campo_nombre")
        self.info_modo = QtGui.QLabel(self.frame)
        self.info_modo.setGeometry(QtCore.QRect(10, 120, 161, 20))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.info_modo.setFont(font)
        self.info_modo.setObjectName("info_modo")
        self.btn_ayuda = QtGui.QPushButton(self.frame)
        self.btn_ayuda.setGeometry(QtCore.QRect(240, 120, 51, 20))
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.btn_nuevo = QtGui.QPushButton(Form)
        self.btn_nuevo.setGeometry(QtCore.QRect(50, 180, 91, 23))
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.btn_editar = QtGui.QPushButton(Form)
        self.btn_editar.setGeometry(QtCore.QRect(150, 180, 81, 23))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_borrar = QtGui.QPushButton(Form)
        self.btn_borrar.setGeometry(QtCore.QRect(240, 180, 91, 23))
        self.btn_borrar.setObjectName("btn_borrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.campo_pais.setStatusTip(QtGui.QApplication.translate("Form", "Modifique para agregar/editar el pais de origen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Pais de Origen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nombre de Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.campo_nombre.setToolTip(QtGui.QApplication.translate("Form", "Modifique para agregar/editar una nueva marca", None, QtGui.QApplication.UnicodeUTF8))
        self.info_modo.setText(QtGui.QApplication.translate("Form", "Modo Edición de Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ayuda.setToolTip(QtGui.QApplication.translate("Form", "AYUDA!", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ayuda.setText(QtGui.QApplication.translate("Form", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo.setText(QtGui.QApplication.translate("Form", "Nueva Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Form", "Editar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_borrar.setText(QtGui.QApplication.translate("Form", "Eliminar Marca", None, QtGui.QApplication.UnicodeUTF8))

