def bubbleSort(anArray, key):
    for i in range(len(anArray)):
        for j in range(i+1, len(anArray)):
            if anArray[i][key] > anArray[j][key]:
                anArray[i], anArray[j] = anArray[j], anArray[i]


def binary_search(data, key):
    
    matched_record = []
    
    bottom = 0
    top = len(data) -1
    found = False
    
    while(bottom <= top):
            middle = int((bottom + top)//2)
            if data[middle] == key : 
                matched_record.append((middle,key)) # position, key
                # looking for the duplicates in left side of the match
                for i in range(middle - 1, -1, -1):
                    if data[i] == key:
                        matched_record.append((i,key))
                    else:
                        break
                # looking for the duplicates in right side of the match
                for i in range(middle + 1, top):
                    if data[i] == key:
                        matched_record.append((i,key))
                    else:
                        break
                break
            else: 
                if key < data[middle]: 
                    top = middle -1
                else: 
                    bottom = middle +1