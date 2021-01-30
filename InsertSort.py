mathsMarks = [68,62,57,42,87,71,81,84,74,63,64,97,52,65,89,76,87,62,72,56,93,78,62,97,44,87,74,81,74,72]

def insert(list, b):
    newList = []
    inserted = 1
    for c in list:
        if b < c and bool(inserted) : 
            newList = newList + [b]
            inserted = 0
        newList = newList + [c]
    if (bool(inserted)):
        newList = newList + [b]
    return(newList)

def sort(listToSort):
    sortedList = []
    for a in listToSort:
        sortedList = insert(sortedList, a)
    print(sortedList)

#sort(mathsMarks)
a = [1,3,2,5,4]
sort(mathsMarks)