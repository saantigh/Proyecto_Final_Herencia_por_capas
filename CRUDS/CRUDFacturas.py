from Modelo.factura import Factura 
from CRUDS.CRUDAntibiotico import CRUDAntibiotico
from CRUDS.CRUDCliente import CRUDCLiente
from CRUDS.CRUDFertilizante import CRUDFertilizantes
from CRUDS.CRUDPlagas import CRUDPlagas

class CRUDfacturas:
    @staticmethod
    def create():
        plagas_disponibles = CRUDPlagas()
        fertilizantes_disponibles = CRUDFertilizantes()
        antibioticos_disponibles = CRUDAntibiotico()

        # Llamado al método 'create' de cada CRUD para obtener listas de productos disponibles
        # en el inventario para cada tipo de producto.
        stock_plagas = plagas_disponibles.create()
        stock_fertilizantes = fertilizantes_disponibles.create()
        stock_antibioticos = antibioticos_disponibles.create()

        #Se crean 5 objetos tipo factura y se le asocian diferentes productos que hay en el stock. 
        factura1=Factura()
        factura1.asociar_antibiotico(stock_antibioticos[0])
        factura1.asociar_producto_control(stock_plagas[0])
        factura1.asociar_producto_control(stock_fertilizantes[0])

        factura2=Factura()
        factura2.asociar_antibiotico(stock_antibioticos[0])
        factura2.asociar_producto_control(stock_plagas[1])
        factura2.asociar_producto_control(stock_fertilizantes[2])

        factura3=Factura()
        factura3.asociar_antibiotico(stock_antibioticos[4])
        factura3.asociar_producto_control(stock_plagas[3])
        factura3.asociar_producto_control(stock_fertilizantes[1])

        factura4=Factura()
        factura4.asociar_antibiotico(stock_antibioticos[4])
        factura4.asociar_antibiotico(stock_antibioticos[3])
        factura4.asociar_producto_control(stock_plagas[3])
        factura4.asociar_producto_control(stock_fertilizantes[3])

        factura5=Factura()
        factura5.asociar_producto_control(stock_plagas[4])

        return [factura1,factura2,factura3,factura4,factura5]
