def main():
    lar = int(input('digite a largura: '))
    alt = int(input('digite a altura: '))
    c = 1
    while c <= alt:
        i = 1
        while i <= lar:
            if (c == 1) or (c == alt):
                print('#', end='')
            else:
                if (i == 1) or (i == lar):
                    print('#', end='')
                else:
                    print(' ', end='')
            i += 1
        print()
        c += 1


main()
