# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(65, 126, 99, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TituloClientes = QtWidgets.QLabel(self.centralwidget)
        self.TituloClientes.setGeometry(QtCore.QRect(360, 0, 121, 31))
        self.TituloClientes.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.TituloClientes.setObjectName("TituloClientes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 341, 16))
        self.label.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.label.setObjectName("label")
        self.BotonVolverMenuPrincipal = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVolverMenuPrincipal.setGeometry(QtCore.QRect(10, 10, 161, 23))
        self.BotonVolverMenuPrincipal.setObjectName("BotonVolverMenuPrincipal")
        self.TituloClientes_2 = QtWidgets.QLabel(self.centralwidget)
        self.TituloClientes_2.setGeometry(QtCore.QRect(90, 80, 131, 21))
        self.TituloClientes_2.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.TituloClientes_2.setObjectName("TituloClientes_2")
        self.CampoIngresarNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoIngresarNombre.setGeometry(QtCore.QRect(220, 80, 221, 20))
        self.CampoIngresarNombre.setText("")
        self.CampoIngresarNombre.setObjectName("CampoIngresarNombre")
        self.TituloClientes_3 = QtWidgets.QLabel(self.centralwidget)
        self.TituloClientes_3.setGeometry(QtCore.QRect(90, 110, 121, 21))
        self.TituloClientes_3.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.TituloClientes_3.setObjectName("TituloClientes_3")
        self.CampoAgregarCedula = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoAgregarCedula.setGeometry(QtCore.QRect(220, 110, 221, 20))
        self.CampoAgregarCedula.setObjectName("CampoAgregarCedula")
        self.BotonAgragarCliente = QtWidgets.QPushButton(self.centralwidget)
        self.BotonAgragarCliente.setGeometry(QtCore.QRect(490, 90, 131, 23))
        self.BotonAgragarCliente.setObjectName("BotonAgragarCliente")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 351, 18))
        self.label_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.label_2.setObjectName("label_2")
        self.TituloClientes_4 = QtWidgets.QLabel(self.centralwidget)
        self.TituloClientes_4.setGeometry(QtCore.QRect(100, 190, 161, 21))
        self.TituloClientes_4.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.TituloClientes_4.setObjectName("TituloClientes_4")
        self.CampoBuscarCedula = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoBuscarCedula.setGeometry(QtCore.QRect(280, 190, 221, 20))
        self.CampoBuscarCedula.setObjectName("CampoBuscarCedula")
        self.BotonBuscarCliente = QtWidgets.QPushButton(self.centralwidget)
        self.BotonBuscarCliente.setGeometry(QtCore.QRect(520, 190, 101, 23))
        self.BotonBuscarCliente.setObjectName("BotonBuscarCliente")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 230, 781, 321))
        self.scrollArea.setStyleSheet("background-color: rgb(193, 222, 209);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaFacturas = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.TablaFacturas.setGeometry(QtCore.QRect(17, 10, 751, 301))
        self.TablaFacturas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TablaFacturas.setObjectName("TablaFacturas")
        self.TablaFacturas.setColumnCount(3)
        self.TablaFacturas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.TablaFacturas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        self.TablaFacturas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        self.TablaFacturas.setHorizontalHeaderItem(2, item)
        self.TablaFacturas.horizontalHeader().setVisible(True)
        self.TablaFacturas.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaFacturas.horizontalHeader().setDefaultSectionSize(200)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 170, 61, 51))
        self.label_3.setStyleSheet("image: url(:/iconos/factura.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clientes"))
        self.TituloClientes.setText(_translate("MainWindow", "CLIENTES"))
        self.label.setText(_translate("MainWindow", "FORMULARIO PARA AGREGAR NUEVO CLIENTE"))
        self.BotonVolverMenuPrincipal.setText(_translate("MainWindow", "VOLVER AL MENÚ PRINCIPAL"))
        self.TituloClientes_2.setText(_translate("MainWindow", "NOMBRE COMPLETO"))
        self.CampoIngresarNombre.setPlaceholderText(_translate("MainWindow", "Ingrese el nombre del nuevo cliente.."))
        self.TituloClientes_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">CEDULA</p></body></html>"))
        self.CampoAgregarCedula.setPlaceholderText(_translate("MainWindow", "Ingrese cedula del nuevo cliente.."))
        self.BotonAgragarCliente.setText(_translate("MainWindow", "AGREGAR CLIENTE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">INFORMACION DE CLIENTES EXISTENTES</p></body></html>"))
        self.TituloClientes_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">BUSQUEDA POR CEDULA</p></body></html>"))
        self.CampoBuscarCedula.setPlaceholderText(_translate("MainWindow", "Ingrese la cedula del cliente.."))
        self.BotonBuscarCliente.setText(_translate("MainWindow", "BUSCAR CLIENTE"))
        item = self.TablaFacturas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Indice Factura"))
        item = self.TablaFacturas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre Producto"))
        item = self.TablaFacturas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Valor Producto"))
from iconos import iconos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())