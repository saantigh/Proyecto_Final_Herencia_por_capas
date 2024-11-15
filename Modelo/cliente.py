
class Cliente:
    def __init__(self, nombre_cliente: str, cedula: str):
        self.__nombre_cliente = nombre_cliente  
        self.__cedula = cedula                  
        self.__facturas = []                    

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        if len(nombre_cliente) >= 3:
            self.__nombre_cliente = nombre_cliente
        else:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        if cedula.isdigit() and len(cedula) >= 7:
            self.__cedula = cedula
        else:
            raise ValueError("La cédula debe ser numérica y tener al menos 7 dígitos.")
    
    @property
    def facturas(self):
        return self.__facturas
    
    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)
