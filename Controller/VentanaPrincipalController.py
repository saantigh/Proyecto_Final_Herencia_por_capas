import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from DesignVentanas.VentanaPrincipal import Ui_MainWindow
from DesignVentanas.iconos import iconos_rc
from Controller.VentanaClienteController import VentanaClientesControlador
from CRUDS.CRUDutilities import CRUD

class VentanaPrincipalControlador(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.crud = CRUD() # Instancia única del CRUD compartida
        self.ui.BotonCliente.clicked.connect(self.abrir_ventana_clientes)
        self.ui.BotonSalir.clicked.connect(self.salir_programa)

    def abrir_ventana_clientes(self):
        self.ventana_clientes = VentanaClientesControlador(self.crud)
        self.ventana_clientes.show()
        self.close()

    def salir_programa(self):
        QCoreApplication.quit()