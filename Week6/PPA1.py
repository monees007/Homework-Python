def ind_d_rep(list):
    for i in list:
        if list.count(i) > 1:
            a = list.index(i)
            b = list[a+1:].index(i)
    return b

def shift_a_person(order_list, position=1):
    if position < 1 or position > len(order_list):
        position = 1
    x = order_list[position - 1]
    order_list.remove(x)
    order_list.append(x)
    while bool(ind_d_rep(order_list)):
        order_list.remove(ind_d_rep(order_list))
