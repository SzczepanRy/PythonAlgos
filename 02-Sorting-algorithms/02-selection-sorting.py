# sortowanie przez wybór
elements = [94, 87, 12, 14, 39, 47, 74, 85, 68, 66]
def selectionSorting(elements):
    """
    Funkcja sortująca przez wybór
    :param elements: tablica do posortowania
    :return: tablica posortowana
    """
    for i in range(len(elements)):
        minElement = i
        for j in range(i + 1, len(elements)):
            if elements[minElement] > elements[j]:
                minElement = j
        elements[i], elements[minElement] = elements[minElement], elements[i]
    return elements

print(selectionSorting(elements))
