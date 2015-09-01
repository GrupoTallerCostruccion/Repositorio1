# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Sep 01 10:49:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 511)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 20))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtGui.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionModulo_Clientes = QtGui.QAction(MainWindow)
        self.actionModulo_Clientes.setEnabled(False)
        self.actionModulo_Clientes.setObjectName("actionModulo_Clientes")
        self.actionMarcas = QtGui.QAction(MainWindow)
        self.actionMarcas.setEnabled(False)
        self.actionMarcas.setObjectName("actionMarcas")
        self.actionModelosAutos = QtGui.QAction(MainWindow)
        self.actionModelosAutos.setEnabled(False)
        self.actionModelosAutos.setObjectName("actionModelosAutos")
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuOpciones.addAction(self.actionModulo_Clientes)
        self.menuOpciones.addAction(self.actionMarcas)
        self.menuOpciones.addAction(self.actionModelosAutos)
        self.menuOpciones.addSeparator()
        self.menuOpciones.addAction(self.actionLogin)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automotoras Diuca", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpciones.setTitle(QtGui.QApplication.translate("MainWindow", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModulo_Clientes.setText(QtGui.QApplication.translate("MainWindow", "Modulo Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMarcas.setText(QtGui.QApplication.translate("MainWindow", "Modulo Marcas de Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModelosAutos.setText(QtGui.QApplication.translate("MainWindow", "Modulo Modelos de Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogin.setText(QtGui.QApplication.translate("MainWindow", "Iniciar Sesion", None, QtGui.QApplication.UnicodeUTF8))

