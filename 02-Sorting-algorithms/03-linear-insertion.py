# sortowanie przez wstwianie liniowe
elements = [38, 65, 85, 72, 6, 44, 15, 66, 86, 70, 92, 52, 63, 45, 71, 64, 17, 73, 40, 50]
def insertionSorting(elements):
    for i in range(1, len(elements)):
        number = elements[i]

        while i > 0 and elements[i - 1] > number:
            elements[i] = elements[i - 1]
            i -= 1
        elements[i] = number
    return elements

print(insertionSorting(elements))