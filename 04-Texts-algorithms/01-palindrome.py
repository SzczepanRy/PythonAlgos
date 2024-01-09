# sprawdzanie, czy dany ciąg znaków tworzy palindrom
# iteracja
def isPalindrome(word):
    word = word.lower()  # Zamieniaj na małe litery, aby nie zależało od wielkości liter
    reversedWord = word[::-1]  # Odwraca wyraz

    return word == reversedWord

# Przykład użycia:
word = "kajak"
if isPalindrome(word):
    print(f"'{word}' to palindrom.")
else:
    print(f"'{word}' nie jest palindromem.")

# rekurencja
def isPalindromeRecursive(word):
    # Usuń spacje i zmień na małe litery (opcjonalne)
    word = word.replace(" ", "").lower()

    # Warunek bazowy: wyraz o długości 0 lub 1 jest zawsze palindromem
    if len(word) <= 1:
        return True

    # Porównaj pierwszą i ostatnią literę
    if word[0] != word[-1]:
        return False

    # Wywołaj rekurencyjnie dla wyrazu bez pierwszej i ostatniej litery
    return isPalindromeRecursive(word[1:-1])


# Przykład użycia:
word = "kajak"
if isPalindromeRecursive(word):
    print(f"'{word}' to palindrom.")
else:
    print(f"'{word}' nie jest palindromem.")