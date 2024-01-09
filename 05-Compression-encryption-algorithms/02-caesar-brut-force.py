message = 'RovvyG7y2vn'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print('Klucz #%s: %s' % (key, translated))