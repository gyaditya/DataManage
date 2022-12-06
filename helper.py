#Insertion Sort
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertion = anArray[i]["genre"]
        n = i -1
        while n >= 0 and insertion < anArray[n]:
            anArray[n + 1] = anArray[n]
            n = n - 1
        anArray[n + 1] = insertion