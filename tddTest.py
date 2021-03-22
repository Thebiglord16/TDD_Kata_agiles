from statistics import mean
from unittest import TestCase
from tdd import statsSecuence
import random

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

    def test_cantidadNValores(self):
        n= random.sample(range(0,2000),random.randint(5,1000))
        cadena = ""
        i = 0
        while i < len(n)-1:
            cadena += str(i)+" "
            i += 1
        cadena += str(i)

        print(cadena)
        self.assertEqual(statsSecuence(cadena)[0], len(n), "Cantidad cadena de N valores")
        self.assertEqual(statsSecuence(cadena)[1], min(n), "Minimo cadena N valores")
        self.assertEqual(statsSecuence(cadena)[2], max(n), "Maximo cadena N valores")
        self.assertEqual(statsSecuence(cadena)[3], mean(n), "Promedio cadena N valores")


