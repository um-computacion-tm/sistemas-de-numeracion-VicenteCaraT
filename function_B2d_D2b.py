#Binario a Decimal
#Decimal a binario


#DECIMAL A BINARIO
def decimal2binario(decimal):
    if decimal == 0:
        return '0'
    digitos_bin = []
    while decimal > 0:
        resto = decimal % 2
        digitos_bin.append(str(resto))
        decimal //=2
    resultado = ''.join(digitos_bin[::-1])
    return resultado
#BIANRIO A DECIMAL
def binario2decimal(binario):
    total = 0
    binario = binario [::-1]
    for i in range(0, len(binario)):
        total += int(binario[i]) * 2 ** i
    return total
#BINARIO A OCTAL
def binario2octal(binario):
    while len(binario) % 3 != 0:
        binario = '0' + binario
    group = [binario[i:i+3] for i in range(0, len(binario), 3)]
    binario_2_octal = {'000': '0', '001': '1', '010': '2', '011': '3',
                       '100': '4', '101': '5', '110': '6', '111': '7'}
    octal = ''
    for grupo in group:
        octal += binario_2_octal[grupo]
    return octal
#BINARIO A HEXADECIMAL
def binario2hexa (binario):
    while len(binario) % 4 != 0:
        binario = '0' + binario
    group = [binario[i:i+4] for i in range(0, len(binario), 4)]
    binario_2_hexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    hexa = ''
    for grupo in group:
        hexa += binario_2_hexa[grupo]
    return hexa
#DECIMAL A OCTAL
def decimal2octal(decimal):
    if decimal == 0:
        return '0'
    digitos_octal = []
    while decimal > 0:
        resto = decimal % 8
        digitos_octal.append(str(resto))
        decimal//= 8
    resultado = ''.join(digitos_octal[::-1])
    return resultado
#OCTAL A BINARIO
def octal2bin(octal):
    octal_2_binario = {'0': '000', '1': '001', '2': '010', '3': '011',
                       '4': '100', '5': '101', '6': '110', '7': '111'}
    binario = ''
    for i in octal:
        binario += octal_2_binario[i]
    return binario.lstrip('0') or '0'
#OCTAL A HEXADECIAMAL
def octal2hexa(octal):
    binario = octal2bin(str(octal))
    hexa = binario2hexa(binario)
    return hexa
#DECIMAL A HEXADECIAML
def decimal2Hexa(decimal):
    if decimal == 0:
        return '0'
    digitos_hexa = []
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            digitos_hexa.append(str(resto))
        else:
            digitos_hexa.append(chr(resto + ord('A') - 10))
        decimal//=16
    resultado = ''.join(digitos_hexa[::-1])
    return resultado
#HEXADECIMAL A BINARIO
def hexa2bin(hexa):
    hexa_2_binario = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                      '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                      '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                      'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    binario = ''
    for i in hexa:
        binario += hexa_2_binario[i]
    binario = binario.lstrip('0')
    return binario
#HEXADECIMAL A OCTAL
def hexa2octal(hexa):
    binario = hexa2bin(hexa)
    octal = binario2octal(binario)
    return octal






if __name__ == '__main__':
    pass