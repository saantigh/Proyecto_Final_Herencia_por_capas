import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.producto_fertilizante import ControlFertilizantes

class TestFertilizante(unittest.TestCase):

    def setUp(self):
        self.fertilizante= ControlFertilizantes("ICA123", "FertiGrow", 30, 100000, "2024-10-01")

    def test_creacion_correcta(self):
        self.assertEqual(self.fertilizante.registro_ica, "ICA123")
        self.assertEqual(self.fertilizante.nombre_producto, "FertiGrow")
        self.assertEqual(self.fertilizante.frecuencia_aplicacion, 30)
        self.assertEqual(self.fertilizante.precio_producto, 100000)
        self.assertEqual(self.fertilizante.fecha_ultima_aplicacion, "2024-10-01")

    def test_registro_ica_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.registro_ica = ""
        self.assertEqual(str(context.exception), "El registro ICA no puede estar vacío.")

    def test_frecuencia_aplicacion_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.frecuencia_aplicacion = -10
        self.assertEqual(str(context.exception), "La frecuencia de aplicación debe ser un valor positivo.")

    def test_fecha_ultima_aplicacion_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.fecha_ultima_aplicacion = "fecha-invalida"
        self.assertEqual(str(context.exception), "La fecha de última aplicación no es válida.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.precio_producto = -5000
        self.assertEqual(str(context.exception), "El precio del producto debe ser un valor positivo.")

if __name__ == "__main__":
    unittest.main()
