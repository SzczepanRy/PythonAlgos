# sortowanie kubełkowe
elements = [4, 72, 29, 17, 78, 73, 54, 42, 11, 12, 96, 89, 15, 13, 10, 98, 53, 51, 57, 63]
def insertionSorting(elements):
    """
    Funkcja sortująca przez wstawianie
    :param elements: tablica do posortowania
    :return: posortowana tablica
    """
    for i in range(1, len(elements)):
        number = elements[i]

        while i > 0 and elements[i - 1] > number:
            elements[i] = elements[i - 1]
            i -= 1
        elements[i] = number
def bucketSorting(elements):
    """
    Funkcja sortująca metodą kubełkową
    :param elements: tablica do posortowania
    :return: tablica posortowana
    """
    buckets = [[] for _ in range(len(elements))]
    output = []

    for i in range(len(elements)):
        j = int(elements[i] / (max(elements) / len(elements)))
        if j != len(elements):
            buckets[j].append(elements[i])
        else:
            buckets[len(elements) - 1].append(elements[i])

    for z in range(len(elements)):
        insertionSorting(buckets[z])

    for x in range(len(elements)):
        output += buckets[x]

    return output

print(bucketSorting(elements))