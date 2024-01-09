# sortowanie przez scalanie
elements = [38, 65, 85, 72, 6, 44, 15, 66, 86, 70, 92, 52, 63, 45, 71, 64, 17, 73, 40, 50]
def mergeSorting(elements):
    """
    Funkcja sortuje przez scalanie
    :param elements: lista do posortowania
    :return: lista posortowana
    """
    if len(elements) < 2:
        return elements

    i = j = k = 0
    middle = len(elements) // 2
    left, right = elements[:middle], elements[middle:]
    mergeSorting(left)
    mergeSorting(right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            elements[k] = left[i]
            i += 1
        else:
            elements[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        elements[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        elements[k] = right[j]
        j += 1
        k += 1
    return elements

print(mergeSorting(elements))