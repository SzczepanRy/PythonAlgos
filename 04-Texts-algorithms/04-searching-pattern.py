# wyrażenia regularne
import re

text = 'To jest przykład tekstu do wyszukania wzorca'
pattern = 'wzorca'

matches = re.finditer(pattern, text)

for match in matches:
    print(f'Znaleziono na pozycji {match.start()}: {match.group()}')

# algorytm Knutha-Morrisa-Pratta (KMP)
def buildFailureTable(pattern):
    # Funkcja do budowania tabeli porażki (failure table) dla wzorca
    m = len(pattern)
    failureTable = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failureTable[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
        failureTable[i] = j

    return failureTable


def searchPattern1(text, pattern):
    n = len(text)
    m = len(pattern)
    failureTable = buildFailureTable(pattern)
    j = 0  # Indeks w tekście

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failureTable[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            # Wzorzec znaleziony, zwracamy indeks pierwszego wystąpienia
            return i - m + 1

    # Wzorzec nie został znaleziony w tekście
    return -1


# Przykład użycia
text = "To jest przykład tekstu do wyszukania wzorca."
pattern = "wzorca"
result = searchPattern1(text, pattern)

if result != -1:
    print(f"Wzorzec znaleziony na pozycji {result}.")
else:
    print("Wzorzec nie został znaleziony w tekście.")

# algorytm Boyera-Moore'a
def buildBadCharacterTable(pattern):
    # Funkcja do budowania tabeli złych znaków (bad character table) dla wzorca
    m = len(pattern)
    badCharTable = {}

    for i in range(m - 1):
        badCharTable[pattern[i]] = m - i - 1

    return badCharTable


def buildGoodSuffixTable(pattern):
    # Funkcja do budowania tabeli dobrego sufiksu (good suffix table) dla wzorca
    m = len(pattern)
    goodSuffixTable = [0] * m
    j = 0

    for i in range(m - 2, -1, -1):
        while j > 0 and pattern[i] != pattern[j]:
            j = goodSuffixTable[j]

        if pattern[i] == pattern[j]:
            j += 1
        goodSuffixTable[i] = j

    return goodSuffixTable


def searchPattern1(text, pattern):
    n = len(text)
    m = len(pattern)
    badCharTable = buildBadCharacterTable(pattern)
    goodSuffixTable = buildGoodSuffixTable(pattern)
    i = 0  # Indeks w tekście

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            # Wzorzec znaleziony, zwracamy indeks pierwszego wystąpienia
            return i

        badCharShift = badCharTable.get(text[i + j], m)
        goodSuffixShift = goodSuffixTable[j]

        i += max(badCharShift, goodSuffixShift)

    # Wzorzec nie został znaleziony w tekście
    return -1


# Przykład użycia
text = "To jest przykład tekstu do wyszukania wzorca."
pattern = "wzorca"
result = searchPattern1(text, pattern)

if result != -1:
    print(f"Wzorzec znaleziony na pozycji {result}.")
else:
    print("Wzorzec nie został znaleziony w tekście.")