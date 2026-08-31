import unittest


def pares(n, m):
    if n <= 0 or m <= 0 or n >= m:
        raise ValueError("No es posible continuar con la operación")

    for numero in range(n, m + 1):
        if numero % 2 == 0:
            yield numero


class TestPares(unittest.TestCase):

    def test_pares_rango(self):
        self.assertEqual(list(pares(2, 10)), [2, 4, 6, 8, 10])

    def test_rango_con_impares_en_extremos(self):
        self.assertEqual(list(pares(3, 9)), [4, 6, 8])

    def test_argumentos_invalidos_n_cero(self):
        with self.assertRaises(ValueError):
            list(pares(0, 10))

    def test_argumentos_invalidos_m_menor_que_n(self):
        with self.assertRaises(ValueError):
            list(pares(10, 5))

    def test_argumentos_invalidos_n_igual_m(self):
        with self.assertRaises(ValueError):
            list(pares(5, 5))

    def test_argumentos_invalidos_negativos(self):
        with self.assertRaises(ValueError):
            list(pares(-2, 5))

    def test_rango_pequeno(self):
        self.assertEqual(list(pares(1, 2)), [2])


if __name__ == "__main__":
    n = 2
    m = 10
    print("Números pares entre", n, "y", m, ":")
    for numero in pares(n, m):
        print(numero)

    unittest.main(argv=[''], exit=False, verbosity=2)