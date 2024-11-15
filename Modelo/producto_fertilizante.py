from Modelo.productos_de_control import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, nombre_producto: str, registro_ica: str, frecuencia_aplicacion: int, precio_producto: float, fecha_ultima_aplicacion: str):
        super().__init__(nombre_producto, registro_ica, frecuencia_aplicacion, precio_producto)
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion

    # Propiedad para fecha de última aplicación
    @property
    def fecha_ultima_aplicacion(self):
        return self.__fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, fecha_ultima_aplicacion):
        # Validación básica para asegurarse de que la fecha no esté vacía
        if fecha_ultima_aplicacion.strip():
            self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion
        else:
            raise ValueError("La fecha de la última aplicación no puede estar vacía.")
