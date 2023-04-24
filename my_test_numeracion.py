import unittest
from function_B2d_D2b import decimal2binario
from function_B2d_D2b import decimal2octal
from function_B2d_D2b import decimal2Hexa
from function_B2d_D2b import binario2decimal
from function_B2d_D2b import binario2octal
from function_B2d_D2b import binario2hexa
from function_B2d_D2b import hexa2bin
from function_B2d_D2b import octal2bin
from function_B2d_D2b import octal2hexa
from function_B2d_D2b import hexa2octal

class TestNumeracion (unittest.TestCase):
#TEST DECIMAL A BINARIO
    def test_decimal2binario_1(self):
        resultado = (decimal2binario(650))
        self.assertEqual (resultado, '1010001010')
    def test_decimal2binario_2(self):
        resultado = (decimal2binario(92))
        self.assertEqual (resultado,'1011100')
    def test_decimal2binario_3(self):
        resultado = (decimal2binario(985))
        self.assertEqual (resultado, '1111011001')

#TEST BINARIO A DECIMAL
    def test_binario2decimal_1(self):
        resultado = (binario2decimal('1011100'))
        self.assertEqual (resultado, 92)
    def test_binario2deimal1_2(self):
        resultado = (binario2decimal('1111001011'))
        self.assertEqual (resultado, 971)  
#TEST BINARIO A OCTAL
    def test_binario2octal_1(self):
        resultado = (binario2octal('100111010'))
        self.assertEqual (resultado, '472')
    def test_binario2octal_2(self):
        resultado = (binario2octal('101011110101'))
        self.assertEqual (resultado, '5365')
#TEST BINARIO A HEXADECIMAL
    def test_binario2hexa_1 (self):
        resultado = (binario2hexa('100111010'))
        self.assertEqual (resultado, '13A')
    def test_binario2hexa_2 (self):
        resultado = (binario2hexa('101011110101'))
        self.assertEqual (resultado, 'AF5') 

#TEST DECIMAL A OCTAL
    def test_decimal2octal_1(self):
        resultado = (decimal2octal(87))
        self.assertEqual (resultado,'127')
    def test_decimal2octal_2(self):
        resultado = (decimal2octal(652))
        self.assertEqual (resultado, '1214')
    def test_decimal2_octal_3(self):
        resultado = (decimal2octal(1769))
        self.assertEqual (resultado, '3351')
#TEST OCTAL A BINARIO
    def test_octal2bin_1(self):
        resultado = octal2bin ('6351')
        self.assertEqual (resultado, '110011101001')
    def test_octal2bin_2(self):
        resultado = octal2bin('1356')
        self.assertEqual (resultado, '1011101110')
#TEST OCTAL A HEXADECIMAL
    def test_octal2hexa_1(self):
        resultado = octal2hexa(6351)
        self.assertEqual (resultado, 'CE9')
    def test_octal2hexa_2(self):
        resultado = octal2hexa(1356)
        self.assertEqual(resultado, '2EE')

#TEST DECIMAL A HEXADECIAML
    def test_decimal2hexa_1(self):
        resultado = (decimal2Hexa(712))
        self.assertEqual (resultado, '2C8')
    def test_decimal2hexa_2(self):
        resultado = (decimal2Hexa(6987))
        self.assertEqual (resultado, '1B4B')
    def test_decimal2hexa_2(self):
        resultado = (decimal2Hexa(65732))
        self.assertEqual (resultado, '100C4')
#TEST HEXADECIMAL A BINARIO
    def test_hexa2bin_1(self):
        resultado = hexa2bin ('BC10')
        self.assertEqual (resultado, '1011110000010000')
    def test_hexa2bin_2(self):
        resultado = hexa2bin ('72F')
        self.assertEqual (resultado, '11100101111')
#TEST HEXADECIMAL A OCTAL
    def test_hexa2octal_1(self):
        resultado = hexa2bin ('BC10')
        self.assertEqual (resultado, '1011110000010000')
    def test_hexa2octal_2(self):
        resultado = hexa2bin ('72F')
        self.assertEqual (resultado, '11100101111')
#TEST BINARIO TO OCTAL
    def test_hexa2octal_1(self):
        resultado = hexa2octal ('94B')
        self.assertEqual (resultado, '4513')
    def test_hexa2octal_1(self):
        resultado = hexa2octal ('B546')
        self.assertEqual (resultado, '132506')

if __name__ == '__main__':
    unittest.main()