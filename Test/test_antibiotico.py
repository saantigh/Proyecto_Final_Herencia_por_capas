import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import unittest
from Modelo.antibioticos import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def setUp(self):
        self.antibiotico = Antibiotico("Penicilina", 500, "bovinos", 150000)

    def test_creacion_correcta(self):
        self.assertEqual(self.antibiotico.nombre_antibiotico, "Penicilina")
        self.assertEqual(self.antibiotico.dosis, 500)
        self.assertEqual(self.antibiotico.tipo_animal, "bovinos")
        self.assertEqual(self.antibiotico.precio_antibiotico, 150000)

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.nombre_antibiotico = ""
        self.assertEqual(str(context.exception), "El nombre del antibiótico no puede estar vacío.")

    def test_nombre_invalido_caracteres(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.nombre_antibiotico = "Penicilin@123"
        self.assertEqual(str(context.exception), "El nombre del antibiótico solo puede contener letras y espacios.")

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.dosis = 300
        self.assertEqual(str(context.exception), "La dosis debe estar entre 400Kg y 600Kg.")

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.tipo_animal = "aves"
        self.assertEqual(str(context.exception), "El tipo de animal debe ser 'bovinos', 'caprinos' o 'porcinos'.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.precio_antibiotico = -1000
        self.assertEqual(str(context.exception), "El precio del antibiótico debe ser un valor positivo.")

if __name__ == "__main__":
    unittest.main()
