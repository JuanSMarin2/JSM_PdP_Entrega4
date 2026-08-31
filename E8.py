import unittest
import re


def email_valido(email):
    """
    Valida que el email tenga al menos:
    - caracteres antes del @
    - un símbolo @
    - caracteres después del @
    - un punto después del @
    """
    if not email or "@" not in email:
        return False

    partes = email.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio = partes
    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    return True


class TestEmailValido(unittest.TestCase):

    def test_email_valido(self):
        self.assertTrue(email_valido("juan@gmail.com"))

    def test_email_sin_arroba(self):
        self.assertFalse(email_valido("juangmail.com"))

    def test_email_con_arroba(self):
        self.assertTrue(email_valido("juan@upb.edu.co"))

    def test_email_vacio(self):
        self.assertFalse(email_valido(""))

    def test_email_solo_arroba(self):
        self.assertFalse(email_valido("@"))

    def test_email_sin_punto_dominio(self):
        self.assertFalse(email_valido("juan@gmail"))

    def test_email_doble_arroba(self):
        self.assertFalse(email_valido("juan@@gmail.com"))


if __name__ == "__main__":
    email = input("Ingrese su dirección de email: ")
    if email_valido(email):
        print("La dirección de email es válida.")
    else:
        print("La dirección de email no es válida.")

    unittest.main(argv=[''], exit=False, verbosity=2)