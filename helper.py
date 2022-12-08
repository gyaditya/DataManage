#Bubble sort

def bubblesort(k):
    for i in range(1, len(k)):
        for j in range(len(k) - i):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]
            