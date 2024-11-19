# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaProductos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 638)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 301, 20))
        self.label.setStyleSheet("color: rgb(85, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.scrollArea_antibioticos = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_antibioticos.setGeometry(QtCore.QRect(10, 20, 781, 181))
        self.scrollArea_antibioticos.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(65, 126, 99, 255), stop:1 rgba(255, 255, 255, 255));")
        self.scrollArea_antibioticos.setWidgetResizable(True)
        self.scrollArea_antibioticos.setObjectName("scrollArea_antibioticos")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TablaAntibioticos = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.TablaAntibioticos.setGeometry(QtCore.QRect(0, 0, 761, 171))
        font = QtGui.QFont()
        font.setItalic(True)
        self.TablaAntibioticos.setFont(font)
        self.TablaAntibioticos.setObjectName("TablaAntibioticos")
        self.TablaAntibioticos.setColumnCount(4)
        self.TablaAntibioticos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaAntibioticos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaAntibioticos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaAntibioticos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaAntibioticos.setHorizontalHeaderItem(3, item)
        self.TablaAntibioticos.horizontalHeader().setDefaultSectionSize(180)
        self.TablaAntibioticos.verticalHeader().setDefaultSectionSize(30)
        self.scrollArea_antibioticos.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 200, 301, 20))
        self.label_2.setStyleSheet("color: rgb(85, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.scrollAreaFertilizantes = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaFertilizantes.setGeometry(QtCore.QRect(10, 220, 781, 181))
        self.scrollAreaFertilizantes.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(65, 126, 99, 255), stop:1 rgba(255, 255, 255, 255));")
        self.scrollAreaFertilizantes.setWidgetResizable(True)
        self.scrollAreaFertilizantes.setObjectName("scrollAreaFertilizantes")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 179))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.TablaFertilizantes = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.TablaFertilizantes.setGeometry(QtCore.QRect(0, 0, 761, 171))
        font = QtGui.QFont()
        font.setItalic(True)
        self.TablaFertilizantes.setFont(font)
        self.TablaFertilizantes.setObjectName("TablaFertilizantes")
        self.TablaFertilizantes.setColumnCount(5)
        self.TablaFertilizantes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFertilizantes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFertilizantes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFertilizantes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFertilizantes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFertilizantes.setHorizontalHeaderItem(4, item)
        self.TablaFertilizantes.horizontalHeader().setDefaultSectionSize(145)
        self.scrollAreaFertilizantes.setWidget(self.scrollAreaWidgetContents_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 400, 261, 20))
        self.label_3.setStyleSheet("color: rgb(85, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.scrollAreaPlagas = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaPlagas.setGeometry(QtCore.QRect(10, 420, 781, 181))
        self.scrollAreaPlagas.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(65, 126, 99, 255), stop:1 rgba(255, 255, 255, 255));")
        self.scrollAreaPlagas.setWidgetResizable(True)
        self.scrollAreaPlagas.setObjectName("scrollAreaPlagas")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 779, 179))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.TablaPlagas = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.TablaPlagas.setGeometry(QtCore.QRect(0, 0, 761, 171))
        font = QtGui.QFont()
        font.setItalic(True)
        self.TablaPlagas.setFont(font)
        self.TablaPlagas.setObjectName("TablaPlagas")
        self.TablaPlagas.setColumnCount(5)
        self.TablaPlagas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPlagas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPlagas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPlagas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPlagas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPlagas.setHorizontalHeaderItem(4, item)
        self.TablaPlagas.horizontalHeader().setDefaultSectionSize(145)
        self.TablaPlagas.horizontalHeader().setMinimumSectionSize(23)
        self.TablaPlagas.verticalHeader().setDefaultSectionSize(30)
        self.scrollAreaPlagas.setWidget(self.scrollAreaWidgetContents_3)
        self.BotonVolverMenuPrincipal = QtWidgets.QPushButton(self.centralwidget)
        self.BotonVolverMenuPrincipal.setGeometry(QtCore.QRect(10, 0, 161, 23))
        self.BotonVolverMenuPrincipal.setObjectName("BotonVolverMenuPrincipal")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Stock disponible en antibioticos"))
        item = self.TablaAntibioticos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaAntibioticos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dosis (ml)"))
        item = self.TablaAntibioticos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo Animal"))
        item = self.TablaAntibioticos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio $"))
        self.label_2.setText(_translate("MainWindow", "Stock disponible en fertilizantes"))
        item = self.TablaFertilizantes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaFertilizantes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reg ICA"))
        item = self.TablaFertilizantes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Freq Aplicacion"))
        item = self.TablaFertilizantes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio $"))
        item = self.TablaFertilizantes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ultima Aplicacion"))
        self.label_3.setText(_translate("MainWindow", "Stock disponible en plagas"))
        item = self.TablaPlagas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaPlagas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reg ICA"))
        item = self.TablaPlagas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Freq Aplicacion"))
        item = self.TablaPlagas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio $"))
        item = self.TablaPlagas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Periodo Carencia"))
        self.BotonVolverMenuPrincipal.setText(_translate("MainWindow", "VOLVER AL MENU PRINCIPAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())