import unittest


def numeros_positivos(numeros):
    es_positivo = lambda x: x > 0
    return list(filter(es_positivo, numeros))



numeros = [-5, 3, -2, 8, 0, 10, -7]
positivos = numeros_positivos(numeros)

print("Números originales:", numeros)
print("Números positivos:", positivos)


class TestNumerosPositivos(unittest.TestCase):

    def test_numeros_positivos_y_negativos(self):
        self.assertEqual(
            numeros_positivos([-5, 3, -2, 8, 10]),
            [3, 8, 10]
        )

    def test_lista_solo_positivos(self):
        self.assertEqual(
            numeros_positivos([1, 2, 3, 4]),
            [1, 2, 3, 4]
        )

    def test_lista_sin_positivos(self):
        self.assertEqual(
            numeros_positivos([-1, -2, 0]),
            []
        )

    def test_cero_no_es_positivo(self):
        self.assertEqual(
            numeros_positivos([0, 5, -3]),
            [5]
        )


if __name__ == "__main__":
    unittest.main()