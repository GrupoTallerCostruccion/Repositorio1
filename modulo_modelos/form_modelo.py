# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_modelo.ui'
#
# Created: Thu Aug 27 05:38:13 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(335, 571)
        self.btn_agregar = QtGui.QPushButton(Form)
        self.btn_agregar.setGeometry(QtCore.QRect(70, 530, 75, 23))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_editar = QtGui.QPushButton(Form)
        self.btn_editar.setGeometry(QtCore.QRect(200, 530, 75, 23))
        self.btn_editar.setObjectName("btn_editar")
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 20, 276, 501))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.mod = QtGui.QLineEdit(self.frame)
        self.mod.setObjectName("mod")
        self.verticalLayout.addWidget(self.mod)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.motor = QtGui.QLineEdit(self.frame)
        self.motor.setObjectName("motor")
        self.verticalLayout.addWidget(self.motor)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.peso = QtGui.QLineEdit(self.frame)
        self.peso.setObjectName("peso")
        self.verticalLayout.addWidget(self.peso)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.rendim = QtGui.QLineEdit(self.frame)
        self.rendim.setObjectName("rendim")
        self.verticalLayout.addWidget(self.rendim)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.fecha = QtGui.QLineEdit(self.frame)
        self.fecha.setObjectName("fecha")
        self.verticalLayout.addWidget(self.fecha)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.precio = QtGui.QLineEdit(self.frame)
        self.precio.setObjectName("precio")
        self.verticalLayout.addWidget(self.precio)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.descripcion = QtGui.QTextEdit(self.frame)
        self.descripcion.setObjectName("descripcion")
        self.verticalLayout.addWidget(self.descripcion)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_selec_img = QtGui.QPushButton(self.frame)
        self.btn_selec_img.setObjectName("btn_selec_img")
        self.verticalLayout.addWidget(self.btn_selec_img)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Motor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Peso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Rendimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Fecha(año) de Creación", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_selec_img.setText(QtGui.QApplication.translate("Form", "Seleccionar Imagen", None, QtGui.QApplication.UnicodeUTF8))
