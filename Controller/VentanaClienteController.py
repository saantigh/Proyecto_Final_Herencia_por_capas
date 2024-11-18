import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from DesignVentanas.VentanaClientes import Ui_MainWindow as MainClientes
from GUI import VentanaPrincipalControlador

class VentanaClientesControlador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainClientes()
        self.ui.setupUi(self)
        self.ui.BotonVolverMenuPrincipal.clicked.connect(self.volver_menu_principal)
        self.ui.BotonAgragarCliente.clicked.connect(self.agregar_cliente)
        self.ui.BotonBuscarCliente.clicked.connect(self.buscar_cliente)
        # Lista temporal para almacenar clientes
        self.clientes = []

    def volver_menu_principal(self):
        self.ventana_principal = VentanaPrincipalControlador()
        self.ventana_principal.show()
        self.close()

    def agregar_cliente(self):
        nombre = self.ui.CampoIngresarNombre.text().strip()
        cedula = self.ui.CampoAgregarCedula.text().strip()

        if not nombre or not cedula:
            self.ui.statusbar.showMessage("Por favor complete ambos campos.", 5000)
            return

        for cliente in self.clientes:
            if cliente['cedula'] == cedula:
                self.ui.statusbar.showMessage("La cédula ya existe.", 5000)
                return

        # Agregar cliente
        self.clientes.append({"nombre": nombre, "cedula": cedula})
        self.ui.statusbar.showMessage("Cliente agregado con éxito.", 5000)
        self.ui.CampoIngresarNombre.clear()
        self.ui.CampoAgregarCedula.clear()

    def buscar_cliente(self):
        cedula_buscar = self.ui.CampoBuscarCedula.text().strip()
        if not cedula_buscar:
            self.ui.statusbar.showMessage("Por favor ingrese una cédula para buscar.", 5000)
            return

        cliente_encontrado = None
        for cliente in self.clientes:
            if cliente['cedula'] == cedula_buscar:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            self.ui.statusbar.showMessage(f"Cliente encontrado: {cliente_encontrado['nombre']}.", 5000)
        else:
            self.ui.statusbar.showMessage("Cliente no encontrado.", 5000)