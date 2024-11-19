import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QMessageBox
from DesignVentanas.VentanaClientes import Ui_MainWindow as MainClientes
from CRUDS.CRUDutilities import CRUD
from Modelo.cliente import Cliente

class VentanaClientesControlador(QMainWindow):
    def __init__(self,CrudClientes):
        super().__init__()
        self.ui = MainClientes()
        self.ui.setupUi(self)
        self.ui.BotonVolverMenuPrincipal.clicked.connect(self.volver_menu_principal)
        self.ui.BotonAgragarCliente.clicked.connect(self.agregar_cliente)
        self.ui.BotonBuscarCliente.clicked.connect(self.buscar_cliente)
        # Lista temporal para almacenar clientes
        self.CrudClientes = CrudClientes

    def volver_menu_principal(self):
        from Controller.VentanaPrincipalController import VentanaPrincipalControlador
        self.ventana_principal = VentanaPrincipalControlador()
        self.ventana_principal.crud=self.CrudClientes
        self.ventana_principal.show()
        self.close()

    def agregar_cliente(self):
        nombre = self.ui.CampoIngresarNombre.text().strip()
        cedula = self.ui.CampoAgregarCedula.text().strip()

        if not nombre or not cedula:
            # Crear mensaje de error
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)  # Ícono de error
            msg_box.setWindowTitle("Error")
            msg_box.setText("Por favor complete ambos campos.")
            msg_box.setStandardButtons(QMessageBox.Ok)  # Botón OK
            msg_box.exec_()  # Mostrar el mensaje
            return

        # Verificar si la cédula ya existe en el CRUD
        cliente_existente = self.CrudClientes.buscar_por_cedula(cedula)
        if cliente_existente:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)  # Ícono de advertencia
            msg_box.setWindowTitle("Advertencia")
            msg_box.setText("La cédula ya existe.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
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
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)  # Ícono de error
            msg_box.setWindowTitle("Error")
            msg_box.setText("Por favor ingrese una cedula")
            msg_box.setStandardButtons(QMessageBox.Ok)  # Botón OK
            msg_box.exec_()  # Mostrar el mensaje
            return

        cliente_encontrado = self.CrudClientes.buscar_por_cedula(cedula_buscar)

        # Limpiar la tabla antes de llenarla
        self.ui.TablaFacturas.setRowCount(0)

        if cliente_encontrado:
            self.ui.statusbar.showMessage(f"Cliente encontrado: {cliente_encontrado.nombre_cliente}.")

            # Recorremos las facturas del cliente
            for indice_factura, factura in enumerate(cliente_encontrado.facturas):
            # Recorremos productos de la lista `antibiotico`
                for antibiotico in factura.antibiotico:
                    self.agregar_fila_tabla(indice_factura, antibiotico.nombre_antibiotico, antibiotico.precio_antibiotico)

            # Recorremos productos de la lista `producto_control`
                for producto in factura.producto_control:
                    self.agregar_fila_tabla(indice_factura, producto.nombre_producto, producto.precio_producto)
        else:
            self.ui.statusbar.showMessage("Cliente no encontrado.", 5000)

    def agregar_fila_tabla(self, indice_factura, nombre_producto, valor_producto):
        # Agregar una nueva fila a la tabla
        row_position = self.ui.TablaFacturas.rowCount()
        self.ui.TablaFacturas.insertRow(row_position)

        # Insertar datos en las columnas
        self.ui.TablaFacturas.setItem(row_position, 0, QTableWidgetItem(str(indice_factura)))
        self.ui.TablaFacturas.setItem(row_position, 1, QTableWidgetItem(nombre_producto))
        self.ui.TablaFacturas.setItem(row_position, 2, QTableWidgetItem(str(valor_producto)))