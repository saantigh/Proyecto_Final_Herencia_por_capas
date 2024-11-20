from PyQt5.QtWidgets import QMainWindow, QMessageBox
from DesignVentanas.VentanaVentas import Ui_MainWindow  # Importa tu diseño generado por Qt Designer
from Modelo.factura import Factura  # Supongamos que tienes una clase Factura en tu modelo
from CRUDS.CRUDutilities import CRUD  # Supongamos que esta es la clase CRUD que ya tienes

class VentanaVentasControlador(QMainWindow):
    def __init__(self, crud, parent=None):
        super(VentanaVentasControlador, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.crud = crud  # Instancia del CRUD (pasada al controlador)
        self.factura_actual = None  # Para manejar la factura actual

        # Configuración inicial
        self.ui.frameAgregarProductos.setEnabled(False)  # Deshabilita el frame al inicio
        self.configurar_eventos()
        self.cargar_lista_stock()

    def configurar_eventos(self):
        """Conecta los botones con sus acciones."""
        self.ui.BotonInstanciarFactura.clicked.connect(self.empezar_facturacion)
        self.ui.BotonAsociarProductoFactura.clicked.connect(self.agregar_producto_a_factura)
        self.ui.BotonAsociar.clicked.connect(self.finalizar_factura)
        self.ui.BotonVolverMenuPrincipal.clicked.connect(self.volver_al_menu)

    def cargar_lista_stock(self):
        """Llena el ComboBox con los nombres de los productos disponibles en el stock."""
        self.ui.comboBoxListaStock.clear()  # Limpia la lista
        for antibiotico in self.crud.stock_disponible_antibioticos:
            self.ui.comboBoxListaStock.addItem(antibiotico.nombre_antibiotico, (antibiotico, "antibiotico"))
        for fertilizante in self.crud.stock_disponible_fertilizantes:
            self.ui.comboBoxListaStock.addItem(fertilizante.nombre_producto, (fertilizante, "fertilizante"))
        for plaga in self.crud.stock_disponible_plagas:
            self.ui.comboBoxListaStock.addItem(plaga.nombre_producto, (plaga, "plaga"))

    def empezar_facturacion(self):
        """Habilita el frame para agregar productos y crea una nueva factura."""
        cedula_cliente = self.ui.CampoIngresarCedula.text().strip()
        cliente = self.crud.buscar_por_cedula(cedula_cliente)

        if not cliente:
            QMessageBox.warning(self, "Error", "El cliente con la cédula ingresada no existe.")
            return

        # Crea una nueva factura
        self.factura_actual = Factura()
        self.ui.frameAgregarProductos.setEnabled(True)
        self.ui.BotonInstanciarFactura.setEnabled(False)
        QMessageBox.information(self, "Facturación iniciada", "Se ha creado una nueva factura para el cliente.")

    def agregar_producto_a_factura(self):
        """Agrega un producto seleccionado a la factura actual."""
        if not self.factura_actual:
            QMessageBox.warning(self, "Error", "Debes iniciar la facturación primero.")
            return

        producto_seleccionado = self.ui.comboBoxListaStock.currentData()
        if not producto_seleccionado:
            QMessageBox.warning(self, "Error", "Debes seleccionar un producto.")
            return

        producto, tipo = producto_seleccionado

        # Asocia el producto a la factura según su tipo
        if tipo == "antibiotico":
            self.factura_actual.realizar_venta(antibiotico=producto)
        else:
            self.factura_actual.realizar_venta(producto_control=producto)

        QMessageBox.information(self, "Producto agregado", f"Se ha agregado {producto.nombre_producto} a la factura.")

    def finalizar_factura(self):
        """Asocia la factura al cliente y finaliza el proceso de facturación."""
        if not self.factura_actual:
            QMessageBox.warning(self, "Error", "No hay ninguna factura en proceso.")
            return

        cedula_cliente = self.ui.CampoIngresarCedula.text().strip()
        cliente = self.crud.buscar_por_cedula(cedula_cliente)

        if not cliente:
            QMessageBox.warning(self, "Error", "El cliente con la cédula ingresada no existe.")
            return

        # Asocia la factura al cliente
        self.crud.asociar_factura(cliente, self.factura_actual)
        self.factura_actual = None  # Resetea la factura actual

        # Resetea la UI
        self.ui.frameAgregarProductos.setEnabled(False)
        self.ui.BotonInstanciarFactura.setEnabled(True)
        QMessageBox.information(self, "Facturación finalizada", "La factura se ha asociado al cliente correctamente.")

    def volver_al_menu(self):
        from Controller.VentanaPrincipalController import VentanaPrincipalControlador
        self.ventana_principal = VentanaPrincipalControlador()
        self.ventana_principal.crud=self.crud
        self.ventana_principal.show()
        self.close()
