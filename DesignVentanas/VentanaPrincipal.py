# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
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
        self.BotonCliente = QtWidgets.QPushButton(self.centralwidget)
        self.BotonCliente.setGeometry(QtCore.QRect(340, 260, 141, 51))
        self.BotonCliente.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(198, 216, 208);\n"
"selection-color: rgb(80, 136, 111);")
        self.BotonCliente.setObjectName("BotonCliente")
        self.BotonProductos = QtWidgets.QPushButton(self.centralwidget)
        self.BotonProductos.setGeometry(QtCore.QRect(340, 330, 141, 51))
        self.BotonProductos.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(198, 216, 208);\n"
"selection-color: rgb(80, 136, 111);")
        self.BotonProductos.setObjectName("BotonProductos")
        self.BotonVender = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVender.setGeometry(QtCore.QRect(340, 400, 141, 51))
        self.BotonVender.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(198, 216, 208);\n"
"selection-color: rgb(80, 136, 111);")
        self.BotonVender.setObjectName("BotonVender")
        self.BotonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.BotonSalir.setGeometry(QtCore.QRect(340, 480, 141, 51))
        self.BotonSalir.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(198, 216, 208);\n"
"selection-color: rgb(80, 136, 111);")
        self.BotonSalir.setObjectName("BotonSalir")
        self.labelBienvenida = QtWidgets.QLabel(self.centralwidget)
        self.labelBienvenida.setGeometry(QtCore.QRect(270, 20, 311, 51))
        self.labelBienvenida.setStyleSheet("font: 87 30pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.labelBienvenida.setObjectName("labelBienvenida")
        self.labelBienvenida_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelBienvenida_2.setGeometry(QtCore.QRect(200, 70, 431, 51))
        self.labelBienvenida_2.setStyleSheet("font: 87 30pt \"Arial Black\";\n"
"color: rgb(85, 170, 127);")
        self.labelBienvenida_2.setObjectName("labelBienvenida_2")
        self.imagenuser = QtWidgets.QLabel(self.centralwidget)
        self.imagenuser.setGeometry(QtCore.QRect(240, 260, 71, 51))
        self.imagenuser.setStyleSheet("image: url(:/iconos/user.jpg);")
        self.imagenuser.setText("")
        self.imagenuser.setObjectName("imagenuser")
        self.imagenproductos = QtWidgets.QLabel(self.centralwidget)
        self.imagenproductos.setGeometry(QtCore.QRect(230, 330, 91, 51))
        self.imagenproductos.setStyleSheet("image: url(:/iconos/antibioticos.jpg);")
        self.imagenproductos.setText("")
        self.imagenproductos.setObjectName("imagenproductos")
        self.imagenvender = QtWidgets.QLabel(self.centralwidget)
        self.imagenvender.setGeometry(QtCore.QRect(240, 400, 71, 51))
        self.imagenvender.setStyleSheet("image: url(:/iconos/factura.jpg);")
        self.imagenvender.setText("")
        self.imagenvender.setObjectName("imagenvender")
        self.imagenSalir = QtWidgets.QLabel(self.centralwidget)
        self.imagenSalir.setGeometry(QtCore.QRect(240, 480, 71, 51))
        self.imagenSalir.setStyleSheet("image: url(:/iconos/salir.jpg);")
        self.imagenSalir.setText("")
        self.imagenSalir.setObjectName("imagenSalir")
        self.imagenIconoprincipal = QtWidgets.QLabel(self.centralwidget)
        self.imagenIconoprincipal.setGeometry(QtCore.QRect(360, 130, 91, 61))
        self.imagenIconoprincipal.setStyleSheet("image: url(:/iconos/plagas.jpg);")
        self.imagenIconoprincipal.setText("")
        self.imagenIconoprincipal.setObjectName("imagenIconoprincipal")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Tienda Agricola"))
        self.BotonCliente.setText(_translate("MainWindow", "CLIENTES"))
        self.BotonProductos.setText(_translate("MainWindow", "PRODUCTOS"))
        self.BotonVender.setText(_translate("MainWindow", "VENDER"))
        self.BotonSalir.setText(_translate("MainWindow", "SALIR"))
        self.labelBienvenida.setText(_translate("MainWindow", "BIENVENIDO"))
        self.labelBienvenida_2.setText(_translate("MainWindow", "TIENDA AGRICOLA"))
from DesignVentanas.iconos import iconos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
