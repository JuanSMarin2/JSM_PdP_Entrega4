import unittest


def calcular_factorial(numero):
    factorial = 1

    for i in range(1, numero + 1):
        factorial = factorial * i

    return factorial



numero = int(input("Ingrese un número: "))
resultado = calcular_factorial(numero)

print("El factorial de", numero, "es:", resultado)


class TestFactorial(unittest.TestCase):

    def test_factorial_cero(self):
        self.assertEqual(calcular_factorial(0), 1)

    def test_factorial_uno(self):
        self.assertEqual(calcular_factorial(1), 1)

    def test_factorial_cinco(self):
        self.assertEqual(calcular_factorial(5), 120)

    def test_factorial_diez(self):
        self.assertEqual(calcular_factorial(10), 3628800)


if __name__ == "__main__":
    unittest.main()