def n_primos(n):
    c = 2
    cont_pri = 0
    while c <= n:
        i = 1
        div_c = 0
        while i <= c:
            if c % i == 0:
                div_c += 1
            i += 1
        if div_c == 2:
            cont_pri += 1
        c += 1
    return cont_pri
