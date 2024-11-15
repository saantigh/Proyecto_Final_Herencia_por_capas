import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Modelo.productos_de_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre_producto: str, registro_ica: str, frecuencia_aplicacion: int, precio_producto: float, periodo_carencia: int):
        # Llamada al constructor de la clase base
        super().__init__(nombre_producto, registro_ica, frecuencia_aplicacion, precio_producto)
        
        # Definición del atributo privado
        self.__periodo_carencia = periodo_carencia

    # Propiedad para obtener el periodo de carencia
    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    # Setter para modificar el periodo de carencia con validación
    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        if periodo_carencia > 0:
            self.__periodo_carencia = periodo_carencia
        else:
            raise ValueError("El periodo de carencia debe ser un valor positivo.")

