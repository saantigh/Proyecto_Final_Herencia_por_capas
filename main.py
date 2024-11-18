from Controller.VentanaPrincipalController import VentanaPrincipalControlador
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipalControlador()
    ventana.show()
    sys.exit(app.exec_())
