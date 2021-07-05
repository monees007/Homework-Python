def insert(list0, x):
    list1, notInserted = [], True
    for i in list0:
        if i > x:
            list1.append(x)
            notInserted = False
        list1.append(i)
    if notInserted:
        list1.append(x)
    return list1

def simple_sort(list0):
    list1 = []
    for x in list0:
        list1 = insert(list1, x)
    return list1


def simple_search(item_list, item):
    item_list = simple_sort(item_list)
    middle0 = len(item_list) // 2
    if len(item_list) == 1 and item != item_list[0]:
        return False
    elif item == item_list[middle0]:
        return True
    else:
        if item < item_list[middle0]:
            simple_search(item_list[0:middle0 + 1], item)
        else:
            simple_search(item_list[middle0:], item)

print(simple_sort([1,2,9,4,3,5,8,9]))