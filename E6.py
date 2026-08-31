import unittest


def suma_numeros(n):
    if n <= 0:
        return 0
    return n + suma_numeros(n - 1)


class TestSumaNumeros(unittest.TestCase):

    def test_suma_cero(self):
        self.assertEqual(suma_numeros(0), 0)

    def test_suma_uno(self):
        self.assertEqual(suma_numeros(1), 1)

    def test_suma_cinco(self):
        self.assertEqual(suma_numeros(5), 15)

    def test_suma_diez(self):
        self.assertEqual(suma_numeros(10), 55)


if __name__ == "__main__":
    n = 5
    resultado = suma_numeros(n)
    print("La suma de los números de 1 a", n, "es:", resultado)

    unittest.main(argv=[''], exit=False, verbosity=2)