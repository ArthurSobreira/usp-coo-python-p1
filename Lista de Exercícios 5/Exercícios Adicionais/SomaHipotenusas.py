def e_hipotenusa(n):
    c = 1
    while c <= n:
        i = 1
        while i <= n:
            if ((c**2) + (i**2)) == (n**2):
                return True
            i += 1
        c += 1

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while c <= n:
        if e_hipotenusa(c):
            soma += c
        c += 1
    return soma
