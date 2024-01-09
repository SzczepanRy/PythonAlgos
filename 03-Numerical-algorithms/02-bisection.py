def bisection(f, a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError('Funkcja nie zmienia znaku na tym przedziale')

    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c # znalezione dokładne miejsce zerowe
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0 # zwraca przybliżone miejsce zerowe

def myFunction(x):
    return x ** 3 - x ** 2 + 2

a = -2
b = 2
tolerance = 0.0001

zeroPoints = bisection(myFunction, a, b, tolerance)
print('Przybliżone miejsce zerowe: ', zeroPoints)