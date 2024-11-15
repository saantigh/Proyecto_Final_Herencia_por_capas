import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.producto_plagas import ControlPlagas

class TestPlaga(unittest.TestCase):

    def setUp(self):
        self.plaga = ControlPlagas("ICA789", "PlagaStop", 15, 80000, 7)

    def test_creacion_correcta(self):
        self.assertEqual(self.plaga.registro_ica, "ICA789")
        self.assertEqual(self.plaga.nombre_producto, "PlagaStop")
        self.assertEqual(self.plaga.frecuencia_aplicacion, 15)
        self.assertEqual(self.plaga.precio_producto, 80000)
        self.assertEqual(self.plaga.periodo_carencia, 7)

    def test_periodo_carencia_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.periodo_carencia = -5
        self.assertEqual(str(context.exception), "El periodo de carencia debe ser un valor positivo.")

    def test_registro_ica_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.registro_ica = ""
        self.assertEqual(str(context.exception), "El registro ICA no puede estar vacío.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.precio_producto = -5000
        self.assertEqual(str(context.exception), "El precio del producto debe ser un valor positivo.")

if __name__ == "__main__":
    unittest.main()
