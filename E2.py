import unittest


def calcular_area(altura, ancho):
    return altura * ancho



altura = int(input("Ingrese la altura del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))

area = calcular_area(altura, ancho)

print("El área del rectangulo es:", area)


class TestArea(unittest.TestCase):

    def test_area_rectangulo(self):
        self.assertEqual(calcular_area(5, 10), 50)

    def test_area_cuadrado(self):
        self.assertEqual(calcular_area(5, 5), 25)

    def test_area_cero(self):
        self.assertEqual(calcular_area(0, 10), 0)

    def test_area_diferente(self):
        self.assertEqual(calcular_area(7, 3), 21)


if __name__ == "__main__":
    unittest.main()