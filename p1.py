array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def duplicate(list1, list2):
    newList = []
    i = 0
    while i < len(array):
        j = 0
        while j < len(array2):
            if list1[i] == list2[j] and list1[i] not in newList:
                newList.append(list1[i])
            j = j + 1
        i = i + 1
    return newList

print(duplicate(array,array2))