# sortowanie szybkie
elements = [38, 65, 85, 72, 6, 44, 15, 66, 86, 70, 92, 52, 63, 45, 71, 64, 17, 73, 40, 50]
def quickSorting(elements):
    """
    Funkcja sortująca metodą szybką
    :param elements: list ado posortowania
    :return: posortowana lista
    """

    if len(elements) <= 1:
        return elements

    pivot = elements[-1]
    smaller = []
    greater = []

    for i in range(0, len(elements) - 1):
        if elements[i] <= pivot:
            smaller.append(elements[i])
        else:
            greater.append(elements[i])

    return quickSorting(smaller) + [pivot] + quickSorting(greater)

print(quickSorting(elements))