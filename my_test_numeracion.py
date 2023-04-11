import unittest
from function_numeracion import binario2decimal


class TestNumeracion (unittest.TestCase):
    def binario2decimal(self):
        resultado = (binario2decimal('01011100', 92))
        self.assertEqual(resultado)
#    def decimal2binario(self):
#        self.assertEqual (decimal2binario(97, '01100001'))


if __name__ == '__main__':
    unittest.main()