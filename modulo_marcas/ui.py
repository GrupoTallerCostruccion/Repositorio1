# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_marcas.ui'
#
# Created: Tue Aug 25 13:47:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 10, 264, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.agregar_marca = QtGui.QPushButton(self.widget)
        self.agregar_marca.setObjectName("agregar_marca")
        self.horizontalLayout.addWidget(self.agregar_marca)
        self.eliminar_marca = QtGui.QPushButton(self.widget)
        self.eliminar_marca.setObjectName("eliminar_marca")
        self.horizontalLayout.addWidget(self.eliminar_marca)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 601, 311))
        self.widget_2.setObjectName("widget_2")
        self.tabla_marcas = QtGui.QTableView(self.widget_2)
        self.tabla_marcas.setGeometry(QtCore.QRect(10, 10, 571, 291))
        self.tabla_marcas.setObjectName("tabla_marcas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar_marca.setText(QtGui.QApplication.translate("MainWindow", "Agregar/Editar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_marca.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Marca", None, QtGui.QApplication.UnicodeUTF8))

