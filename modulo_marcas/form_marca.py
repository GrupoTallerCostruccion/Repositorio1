# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_marca.ui'
#
# Created: Mon Aug 31 01:13:18 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 216)
        self.frame = QtGui.QFrame(Dialog)
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
        self.btn_guardar = QtGui.QPushButton(Dialog)
        self.btn_guardar.setGeometry(QtCore.QRect(80, 180, 111, 23))
        self.btn_guardar.setObjectName("btn_guardar")
        self.cancelar = QtGui.QPushButton(Dialog)
        self.cancelar.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.cancelar.setObjectName("cancelar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.campo_pais.setStatusTip(QtGui.QApplication.translate("Dialog", "Modifique para agregar/editar el pais de origen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Pais de Origen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre de Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.campo_nombre.setToolTip(QtGui.QApplication.translate("Dialog", "Modifique para agregar/editar una nueva marca", None, QtGui.QApplication.UnicodeUTF8))
        self.info_modo.setText(QtGui.QApplication.translate("Dialog", "Modo Edición de Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_guardar.setText(QtGui.QApplication.translate("Dialog", "Guardar Cambios", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

