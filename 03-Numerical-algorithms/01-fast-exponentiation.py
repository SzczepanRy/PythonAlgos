# szybkie podnoszenie do potęgi
def fastExponentiation(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        # jeśli wykładnik jest parzysty a^n = (a^(n/2)^2)
        halfPower = fastExponentiation(base, exponent // 2)
        return halfPower * halfPower
    else:
        # jeśli wykładnik jest nieparzysty a^n = a * (a^(n-1))
        return base * fastExponentiation(base, exponent - 1)

base = 2
exponent = 10
result = fastExponentiation(base, exponent)
print(f'{base} do potęgi {exponent} = {result}')