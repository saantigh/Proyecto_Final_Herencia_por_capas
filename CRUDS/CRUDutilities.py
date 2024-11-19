from CRUDS.CRUDCliente import CRUDCLiente
from CRUDS.CRUDFacturas import CRUDfacturas
from CRUDS.CRUDAntibiotico import CRUDAntibiotico
from CRUDS.CRUDFertilizante import CRUDFertilizantes
from CRUDS.CRUDPlagas import CRUDPlagas

class CRUD:
    def __init__(self):
        clientes_por_defecto = CRUDCLiente()
        facturas_por_defecto = CRUDfacturas()
        stock_antibioticos = CRUDAntibiotico()
        stock_fertilizantes = CRUDFertilizantes()
        stock_plagas = CRUDPlagas()
        self.clientes = clientes_por_defecto.create() #Inicializa la lista de clientes en el sistema
        self.facturas = facturas_por_defecto.create() # Inicializa la lista de facturas en el sistema
        self.asociar_factura(self.clientes[0],self.facturas[0])
        self.asociar_factura(self.clientes[0],self.facturas[3]) # Asocia algunas facturas por defecto
        self.asociar_factura(self.clientes[0],self.facturas[2])
        self.stock_disponible_antibioticos = stock_antibioticos.create() # Inicializa la lista del stock de antibioticos
        self.stock_disponible_fertilizantes = stock_fertilizantes.create() # Inicializa la lista del stock de fertilizantes
        self.stock_disponible_plagas = stock_plagas.create() # Inicializa la lista del stock de plagas en el sistema

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente) 

    def buscar_por_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return False

    def eliminar_cliente(self, cedula):
        cliente = self.buscar_por_cedula(cedula)
        if cliente is False:
            raise ValueError("No se puede eliminar, el cliente no existe.")
        self.clientes.remove(cliente)

    def asociar_factura(self, cliente, factura):
        if cliente not in self.clientes:
            raise ValueError("El cliente no existe.") 
        cliente.facturas.append(factura)


