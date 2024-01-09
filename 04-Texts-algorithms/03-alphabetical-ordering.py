# porządkowanie alfabetyczne (leksykograficzne)
words = ["jabłko", "banan", "arbuz", "ananas", "gruszka"]

# użycie sorted()
sortedWords = sorted(words)
print(sortedWords)

# użycie list.sort()
words.sort()
print(words)

# użycie reverse=True
sortedWordsDesc = sorted(words, reverse=True)
print(sortedWordsDesc)

# użycie bubble sort
def lexicographicBubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
lexicographicBubbleSort(words)
print(words)