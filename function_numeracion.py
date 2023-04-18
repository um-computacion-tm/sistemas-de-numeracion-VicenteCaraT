def binario2decimal (binario):
    total = 0
    for i in range(0, len(binario)):
        total += int(binario[-i-1]) + 2 **i
    return total

def decimal2binario (decimal):
    if decimal == 0:
        return '0'
    digitos_bin = []
    while decimal > 0:
        resto = decimal % 2
        digitos_bin.append(str(resto))
        decimal //=2
    resultado = ''.join(digitos_bin[::-1])
    return resultado
    

if __name__ == '__main__':
    pass