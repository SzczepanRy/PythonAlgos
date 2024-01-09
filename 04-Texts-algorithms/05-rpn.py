# obliczanie wyrażenia podanego w odwrotnej notacji polskiej 2 4 +
def calculateRpn(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise ValueError('Niewystarczająco operandów dla operatora')
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError('Dzielenie przez zero')
                result = a / b
            stack.append(result)

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError('Niewłaściwa ilość operatprów')

expression1 = '3 4 + 2 *'
result1 = calculateRpn(expression1)
print(f'Wynik wyrażenia {expression1} to {result1}')

expression2 = '5 1 2 + 4 * + 3 -'
result2 = calculateRpn(expression2)
print(f'Wynik wyrażenia {expression2} to {result2}')