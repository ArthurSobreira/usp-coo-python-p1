def main():
    lar = int(input('digite a largura: '))
    alt = int(input('digite a altura: '))
    c = 1
    while c <= alt:
        i = 1
        while i <= lar:
            print('#', end='')
            i += 1
        print()
        c += 1


main()
