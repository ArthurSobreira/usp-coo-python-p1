def primo(num):
    div = 0
    for c in range(1, num+1):
        if num % c == 0:
            div += 1
    if div == 2:
        return True


def maior_primo(num):
    if primo(num):
        return num
    else:
        c = num
        while c > 0:
            if primo(c):
                return c
                break
            c -= 1
