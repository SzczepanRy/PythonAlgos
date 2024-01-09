# sprawdzanie, czy dane wyrazy są anagramami
# iteracja
def areAnagrams(word1, word2):
    # Usuń spacje i zmień na małe litery (opcjonalne)
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Sprawdź, czy oba wyrazy mają taką samą ilość każdej litery
    return sorted(word1) == sorted(word2)

# Przykład użycia:
word1 = "burza"
word2 = "arbuz"
if areAnagrams(word1, word2):
    print(f"'{word1}' i '{word2}' to anagramy.")
else:
    print(f"'{word1}' i '{word2}' nie są anagramami.")

# rekurencja
def areAnagramsRecursive(word1, word2):
    # Usuń spacje i przekształć litery na małe, aby porównanie było nieczułe na wielkość liter
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Sprawdź, czy obie frazy mają tę samą długość
    if len(word1) != len(word2):
        return False

    # Jeśli obie frazy są puste, to są anagramami
    if not word1:
        return True

    # Porównaj pierwszą literę z jednej frazy z pozostałymi literami w drugiej fazie
    if word1[0] in word2:
        # Rekurencyjnie sprawdź resztę frazy
        return areAnagramsRecursive(word1[1:], word2.replace(word1[0], '', 1))
    else:
        return False


# Przykład użycia
word1 = "burza"
word2 = "arbuz"
if areAnagramsRecursive(word1, word2):
    print(f"'{word1}' i '{word2}' to anagramy.")
else:
    print(f"'{word1}' i '{word2}' nie są anagramami.")