import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from DesignVentanas.VentanaClientes import Ui_MainWindow as MainClientes
from CRUDS.CRUDutilities import CRUD
from Modelo.cliente import Cliente

class VentanaClientesControlador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainClientes()
        self.ui.setupUi(self)
        self.ui.BotonVolverMenuPrincipal.clicked.connect(self.volver_menu_principal)
        self.ui.BotonAgragarCliente.clicked.connect(self.agregar_cliente)
        self.ui.BotonBuscarCliente.clicked.connect(self.buscar_cliente)
        # Lista temporal para almacenar clientes
        self.CrudClientes = CRUD()

    def volver_menu_principal(self):
        from Controller.VentanaPrincipalController import VentanaPrincipalControlador
        self.ventana_principal = VentanaPrincipalControlador()
        self.ventana_principal.show()
        self.close()

    def agregar_cliente(self):
        nombre = self.ui.CampoIngresarNombre.text().strip()
        cedula = self.ui.CampoAgregarCedula.text().strip()

        if not nombre or not cedula:
            self.ui.statusbar.showMessage("Por favor complete ambos campos.", 5000)
            return

        # Verificar si la cédula ya existe en el CRUD
        cliente_existente = self.CrudClientes.buscar_por_cedula(cedula)
        if cliente_existente:
            self.ui.statusbar.showMessage("La cédula ya existe.", 5000)
            return

        # Crear un nuevo cliente
        nuevo_cliente = Cliente(nombre_cliente=nombre, cedula=cedula)
        self.CrudClientes.agregar_cliente(nuevo_cliente)  # Agregar cliente al CRUD
        self.ui.statusbar.showMessage("Cliente agregado con éxito.", 5000)
        self.ui.CampoIngresarNombre.clear()
        self.ui.CampoAgregarCedula.clear()

    def buscar_cliente(self):
        cedula_buscar = self.ui.CampoBuscarCedula.text().strip()
        if not cedula_buscar:
            self.ui.statusbar.showMessage("Por favor ingrese una cédula para buscar.", 5000)
            return

        cliente_encontrado = self.CrudClientes.buscar_por_cedula(cedula_buscar)

        if cliente_encontrado:
            self.ui.statusbar.showMessage(f"Cliente encontrado: {cliente_encontrado.nombre_cliente}.", 5000)
        else:
            self.ui.statusbar.showMessage("Cliente no encontrado.", 5000)