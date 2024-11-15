import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import unittest
from Modelo.factura import Factura as factura
from Modelo.antibioticos import Antibiotico as antibiotico
from Modelo.producto_fertilizante import ControlFertilizantes as producto_fertilizante
from Modelo.producto_plagas import ControlPlagas as producto_plaga
from Modelo.productos_de_control import ProductoControl as pc
from Modelo.cliente import Cliente as cliente     
from CRUD.CRUDutilities import CRUD  

class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.crud = CRUD() 
        self.cliente_1 = cliente("Juan Perez", "12345678")
        self.cliente_2 = cliente("Maria Lopez", "87654321")

        self.factura_1 = factura()
        self.factura_2 = factura()
        
        self.pc_plaga = producto_plaga("Plaga X", "ICA124", 8, 20000, 20)
        self.pc_fertilizante = producto_fertilizante("UREA", "ICA7028", 15, 60000, 10)
       
        self.antibiotico_1 = antibiotico("anti_1", "10", "bovino", 120000)
        self.antibiotico_2 = antibiotico("anti_2", "8", "caprino", 100000)

    def test_agregar_cliente(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.agregar_cliente(self.cliente_2)
        self.assertEqual(len(self.crud.clientes), 2, "No se agregaron los clientes correctamente.")

    def test_buscar_por_cedula(self):
        self.crud.agregar_cliente(self.cliente_1)
        cliente_encontrado = self.crud.buscar_por_cedula("12345678")
        self.assertIsNotNone(cliente_encontrado, "El cliente no fue encontrado.")
        self.assertEqual(cliente_encontrado.nombre_cliente, "Juan Perez", "El nombre del cliente no coincide.")

    def test_eliminar_cliente(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.eliminar_cliente("12345678")
        cliente_eliminado = self.crud.buscar_por_cedula("12345678")
        self.assertIsNone(cliente_eliminado, "El cliente no fue eliminado correctamente.")

    def test_eliminar_cliente_inexistente(self):
        with self.assertRaises(ValueError, msg="No se generó la excepción adecuada al intentar eliminar un cliente inexistente."):
            self.crud.eliminar_cliente("99999999")

    def test_buscar_cliente_inexistente(self):
        cliente_no_encontrado = self.crud.buscar_por_cedula("99999999")
        self.assertIsNone(cliente_no_encontrado, "No se manejó correctamente la búsqueda de un cliente inexistente.")

    def test_asociar_factura(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.asociar_factura(self.cliente_1, [self.factura_1, self.factura_2])
        self.assertEqual(len(self.cliente_1.facturas), 2, "Las facturas no fueron asociadas correctamente al cliente.")

    def test_asociar_factura_cliente_inexistente(self):
        cliente_falso = cliente("Falso Cliente", "00000000")
        with self.assertRaises(ValueError, msg="No se generó la excepción adecuada al intentar asociar facturas a un cliente inexistente."):
            self.crud.asociar_factura(cliente_falso, [self.factura_1])

    def test_asociar_producto_control_y_antibioticos_a_factura(self):
        self.factura_1.asociar_producto_control(self.pc_plaga)
        self.factura_1.asociar_producto_control(self.pc_fertilizante)
        self.factura_1.asociar_antibiotico(self.antibiotico_1)
        self.factura_1.asociar_antibiotico(self.antibiotico_2)
     
        self.assertEqual(len(self.factura_1.producto_control), 2, "Los productos de control no fueron asociados correctamente.")
        self.assertEqual(len(self.factura_1.antibiotico), 2, "Los antibióticos no fueron asociados correctamente.")

if __name__ == "__main__":
    unittest.main()
  
