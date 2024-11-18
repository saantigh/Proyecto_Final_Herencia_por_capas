import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from DesignVentanas.VentanaPrincipal import Ui_MainWindow
from Controller.VentanaClienteController import VentanaClientesControlador

class VentanaPrincipalControlador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BotonClientes.clicked.connect(self.abrir_ventana_clientes)

    def abrir_ventana_clientes(self):
        self.ventana_clientes = VentanaClientesControlador()
        self.ventana_clientes.show()
        self.close()
