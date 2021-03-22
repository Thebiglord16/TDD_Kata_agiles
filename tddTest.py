from unittest import TestCase
from tdd import statsSecuence

class test(TestCase):
    def test_cantidadVacia(self):
        self.assertEqual(statsSecuence("")[0], 0, "Cantidad cadena vacia")
        self.assertEqual(statsSecuence("")[1], 0, "Minimo cadena vacia")
        self.assertEqual(statsSecuence("")[2], 0, "Maximo cadena vacia")
        self.assertEqual(statsSecuence("")[3], 0, "Promedio cadena vacia")

    def test_cantidadUnValor(self):
        self.assertEqual(statsSecuence("7")[0], 1, "Cantidad cadena un valor")
        self.assertEqual(statsSecuence("7")[1], 7, "Minimo cadena (7)")
        self.assertEqual(statsSecuence("7")[2], 7, "Maximo cadena (7)")
        self.assertEqual(statsSecuence("7")[3], 7, "Promedio cadena (7)")

    def test_cantidadDosValores(self):
        self.assertEqual(statsSecuence("3 9")[0], 2, "Cantidad cadena de dos valores")
        self.assertEqual(statsSecuence("3 9")[1], 3, "Minimo cadena (3 9)")
        self.assertEqual(statsSecuence("3 9")[2], 9, "Maximo cadena (3 9)")
        self.assertEqual(statsSecuence("3 9")[3], 6, "Promedio cadena (3 9)")

