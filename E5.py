import unittest


def mostrar_resultado(funcion):
    def decorador(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        print("Resultado de la operación:", resultado)
        return resultado
    return decorador


@mostrar_resultado
def sumar(a, b):
    return a + b


class TestSuma(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(sumar(5, 3), 8)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-5, -3), -8)

    def test_suma_cero(self):
        self.assertEqual(sumar(10, 0), 10)


if __name__ == "__main__":
    resultado = sumar(5, 3)
    print("Resultado directo:", resultado)

    unittest.main(argv=[''], exit=False, verbosity=2)