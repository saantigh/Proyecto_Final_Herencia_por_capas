from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from DesignVentanas.VentanaProductos import Ui_MainWindow  # Importa la clase generada por pyuic5

class VentanaProductosControlador(QMainWindow):
    def __init__(self, crud, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.crud = crud  # Recibimos la instancia del CRUD
        
        # Conectar el botón "Volver al menú principal"
        self.ui.BotonVolverMenuPrincipal.clicked.connect(self.volver_menu_principal)

        # Llenar las tablas al iniciar la ventana
        self.llenar_tabla_antibioticos()
        self.llenar_tabla_fertilizantes()
        self.llenar_tabla_plagas()

    def volver_menu_principal(self):
        from Controller.VentanaPrincipalController import VentanaPrincipalControlador
        self.ventana_principal = VentanaPrincipalControlador()
        self.ventana_principal.crud=self.crud
        self.ventana_principal.show()
        self.close()

    def llenar_tabla_antibioticos(self):
        """Llena la tabla de antibióticos con los datos del CRUD."""
        datos = self.crud.stock_disponible_antibioticos
        self.ui.TablaAntibioticos.setRowCount(len(datos))
        for fila, antibiotico in enumerate(datos):
            self.ui.TablaAntibioticos.setItem(fila, 0, QTableWidgetItem(antibiotico.nombre_antibiotico))
            self.ui.TablaAntibioticos.setItem(fila, 1, QTableWidgetItem(str(antibiotico.dosis)))
            self.ui.TablaAntibioticos.setItem(fila, 2, QTableWidgetItem(antibiotico.tipo_animal))
            self.ui.TablaAntibioticos.setItem(fila, 3, QTableWidgetItem(str(antibiotico.precio_antibiotico)))

    def llenar_tabla_fertilizantes(self):
        """Llena la tabla de fertilizantes con los datos del CRUD."""
        datos = self.crud.stock_disponible_fertilizantes
        self.ui.TablaFertilizantes.setRowCount(len(datos))
        for fila, fertilizante in enumerate(datos):
            self.ui.TablaFertilizantes.setItem(fila, 0, QTableWidgetItem(fertilizante.nombre_producto))
            self.ui.TablaFertilizantes.setItem(fila, 1, QTableWidgetItem(fertilizante.registro_ica))
            self.ui.TablaFertilizantes.setItem(fila, 2, QTableWidgetItem(str(fertilizante.frecuencia_aplicacion)))
            self.ui.TablaFertilizantes.setItem(fila, 3, QTableWidgetItem(str(fertilizante.precio_producto)))
            self.ui.TablaFertilizantes.setItem(fila, 4, QTableWidgetItem(fertilizante.fecha_ultima_aplicacion))

    def llenar_tabla_plagas(self):
        """Llena la tabla de plagas con los datos del CRUD."""
        datos = self.crud.stock_disponible_plagas
        self.ui.TablaPlagas.setRowCount(len(datos))
        for fila, plaga in enumerate(datos):
            self.ui.TablaPlagas.setItem(fila, 0, QTableWidgetItem(plaga.nombre_producto))
            self.ui.TablaPlagas.setItem(fila, 1, QTableWidgetItem(plaga.registro_ica))
            self.ui.TablaPlagas.setItem(fila, 2, QTableWidgetItem(str(plaga.frecuencia_aplicacion)))
            self.ui.TablaPlagas.setItem(fila, 3, QTableWidgetItem(str(plaga.precio_producto)))
            self.ui.TablaPlagas.setItem(fila, 4, QTableWidgetItem(str(plaga.periodo_carencia)))
