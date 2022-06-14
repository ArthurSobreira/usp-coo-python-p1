def remove_repetidos(lista):
    my_list = []
    for c in lista:
        if c not in my_list:
            my_list.append(c)
    my_list.sort()
    return my_list
