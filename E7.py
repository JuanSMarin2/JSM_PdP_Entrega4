import unittest


def generar_identificador(nombre, dni):
    partes = nombre.split()
    primer_nombre = partes[0]
    apellido = partes[-1]
    cantidad_apellido = len(apellido)
    return primer_nombre + str(cantidad_apellido) + dni[:3]


class TestGenerarIdentificador(unittest.TestCase):

    def test_nombre_unico(self):
        self.assertEqual(
            generar_identificador("Alba Linares", "25834910"),
            "Alba7258"
        )

    def test_nombre_compuesto(self):
        self.assertEqual(
            generar_identificador("Alba María Linares", "25834910"),
            "Alba7258"
        )

    def test_apellido_corto(self):
        self.assertEqual(
            generar_identificador("Juan Perez", "1234567"),
            "Juan5123"
        )

    def test_dni_de_siete_digitos(self):
        self.assertEqual(
            generar_identificador("Pedro Lopez", "1234567"),
            "Pedro5123"
        )


if __name__ == "__main__":
    while True:
        nombre = input("Ingrese el nombre completo del socio (vacío para finalizar): ")
        if nombre == "":
            break

        while True:
            dni = input("Ingrese el DNI: ")
            if dni.isdigit() and 7 <= len(dni) <= 8:
                break
            print("El DNI debe tener 7 u 8 dígitos.")

        identificador = generar_identificador(nombre, dni)
        print("Identificador:", identificador)

    unittest.main(argv=[''], exit=False, verbosity=2)