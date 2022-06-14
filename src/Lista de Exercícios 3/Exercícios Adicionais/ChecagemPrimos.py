num = int(input('Digite um número inteiro: '))

cont_div = 0
for c in range(1, num+1):
    if num % c == 0:
        cont_div += 1

if cont_div == 2:
    print('primo')
else:
    print('não primo')
