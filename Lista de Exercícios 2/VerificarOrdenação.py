def main():
    num1 = int(input('Digite um Número: '))
    num2 = int(input('Digite outro Número: '))
    num3 = int(input('Digite um último Número: '))
    if num1 < num2 < num3:
        print('crescente')
    else:
        print('não está em ordem crescente')


main()
