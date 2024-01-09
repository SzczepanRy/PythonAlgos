# sortowanie bąbelkowe
elements = [94, 87, 12, 14, 39, 47, 74, 85, 68, 66]
def bubbleSorting(elements):
    """
    Funkcja sortująca bąbelkowo
    :param elements: tablica do posortowania
    :return: tablica posortowana
    """
    for i in range(len(elements)):
        for j in range(len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j + 1], elements[j] = elements[j], elements[j + 1]
    return elements

print(bubbleSorting(elements))

# wersja zoptymalizowana
def swap(elements, x, y):
    """
    Funkcja pomocnicza realizująca operację swap
    :param elements: tablica elementów do posortowania
    :param x: element pomocniczy do swap
    :param y: element pomocniczy do swap
    :return: elementy zamienione miejscami, swap
    """
    temp = elements[x]
    elements[x] = elements[y]
    elements[y] = temp

def bubbleSorting1(elements):
    """
    Funkcja sortująca bąbelkowo
    :param elements: tablica do posortowania
    :return: tablica posortowana
    """
    for i in range(len(elements)):
        isSorted = True
        for j in range(1, len(elements) - i):
            if elements[j] < elements[j - 1]:
                swap(elements, j, j - 1)
                isSorted = False
        if isSorted:
            break

bubbleSorting1(elements)
print(elements)