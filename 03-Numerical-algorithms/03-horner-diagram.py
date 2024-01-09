# konwersja z dziesiętnego na system dwójkowy (binarny)
def decimalToBinary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

# Przykład użycia:
decimalNumber = 10
binaryRepresentation = decimalToBinary(decimalNumber)
print(f"Reprezentacja dziesiętna {decimalNumber} w systemie dwójkowym: {binaryRepresentation}")

# konwersja z systemu dwójkowego na dziesiętny przy użyciu schematu Hornera
def binaryToDecimal(binary):
    decimal = 0
    binary = binary[::-1]  # Odwracamy ciąg binarny
    for i, digit in enumerate(binary):
        if digit == '1':
            decimal += 2**i
    return decimal

# Przykład użycia:
binaryNumber = "1010"
decimalRepresentation = binaryToDecimal(binaryNumber)
print(f"Reprezentacja binarna {binaryNumber} w systemie dziesiętnym: {decimalRepresentation}")

# konwersja z dziesiętnego na system ósemkowy (oktalny)
def decimalToOctal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8
    return octal

# Przykład użycia:
decimalNumber = 23
octalRepresentation = decimalToOctal(decimalNumber)
print(f"Reprezentacja dziesiętna {decimalNumber} w systemie ósemkowym: {octalRepresentation}")

# konwersja z systemu ósemkowego na dziesiętny przy użyciu schematu Hornera
def octalToDecimal(octal):
    decimal = 0
    octal = octal[::-1]  # Odwracamy ciąg ósemkowy
    for i, digit in enumerate(octal):
        decimal += int(digit) * (8**i)
    return decimal

# Przykład użycia:
octalNumber = "37"
decimalRepresentation = octalToDecimal(octalNumber)
print(f"Reprezentacja ósemkowa {octalNumber} w systemie dziesiętnym: {decimalRepresentation}")

# konwersja z dziesiętnego na system szesnastkowy (heksadecymalny)
def decimalToHexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal = decimal // 16
    return hexadecimal

# Przykład użycia:
decimalNumber = 10
hexadecimalRepresentation = decimalToHexadecimal(decimalNumber)
print(f"Reprezentacja dziesiętna {decimalNumber} w systemie szesnastkowym: {hexadecimalRepresentation}")

# konwersja z systemu szesnastkowego na dziesiętny przy użyciu schematu Hornera
def hexadecimalToDecimal(hexadecimal):
    decimal = 0
    hexadecimal = hexadecimal[::-1]  # Odwracamy ciąg szesnastkowy
    for i, digit in enumerate(hexadecimal):
        if '0' <= digit <= '9':
            decimal += int(digit) * (16**i)
        else:
            decimal += (ord(digit.upper()) - ord('A') + 10) * (16**i)
    return decimal

# Przykład użycia:
hexadecimalNumber = "A"
decimalRepresentation = hexadecimalToDecimal(hexadecimalNumber)
print(f"Reprezentacja szesnastkowa {hexadecimalNumber} w systemie dziesiętnym: {decimalRepresentation}")

# konwersja z systemu dziesiętnego na inny system liczbowy
def decimalToBase(n, b):
    result = ""
    while n > 0:
        remainder = n % b
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        n = n // b
    return result

# Przykład użycia:
decimalNumber = 255
base = 16  # System szesnastkowy
baseRepresentation = decimalToBase(decimalNumber, base)
print(f"Reprezentacja dziesiętna {decimalNumber} w systemie o podstawie {base}: {baseRepresentation}")

# konwersja z innego systemu liczbowego na system dziesiętny
def baseToDecimal(number, b):
    decimal = 0
    for digit in number:
        if '0' <= digit <= '9':
            decimal = decimal * b + int(digit)
        else:
            decimal = decimal * b + (ord(digit) - ord('A') + 10)
    return decimal

# Przykład użycia:
baseNumber = "FF"
base = 16  # System szesnastkowy
decimalRepresentation = baseToDecimal(baseNumber, base)
print(f"Reprezentacja liczby {baseNumber} w systemie dziesiętnym: {decimalRepresentation}")