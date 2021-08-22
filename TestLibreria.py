import Libreria as lc
import unittest

class TestCplxoperations(unittest.TestCase):
    def test_Suma(self):
        self.assertEqual(lc.Suma(11+6j,30-50j), (41.0, -44.0))
    def test_Resta(self):
        self.assertEqual(lc.Resta(10+6j,30-50j), (-20.0, 56.0))
    def test_Multiplicacion(self):
        self.assertEqual(lc.Multiplicacion(10+6j,30-50j), (600.0, -320.0))
    def test_Division(self):
        self.assertEqual(lc.Division(10+6j,30-50j), (0.0, 0.2))
    def test_Modulo(self):
        self.assertEqual(lc.Modulo(8+6j), 10.0)
    def test_Conjugado(self):
        self.assertEqual(lc.Conjugado(8+6j), (8.0, -6.0))
    def test_Car_Pol(self):
        self.assertEqual(lc.Car_Pol(8+6j), (10.0, 36.8885985932456))
    def test_Fase(self):
        self.assertEqual(lc.Fase(8+6j), 36.8885985932456)


if __name__ == "__main__":
    unittest.main()

