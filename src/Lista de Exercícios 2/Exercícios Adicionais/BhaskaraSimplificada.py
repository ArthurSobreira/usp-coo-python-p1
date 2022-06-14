from math import *

a = int(input('Digite o Valor de A na equação: '))
b = int(input('Digite o Valor de B na equação: '))
c = int(input('Digite o Valor de C na equação: '))

delt = (b ** 2) - (4 * a * c)

if delt < 0:
    print('esta equação não possui raízes reais')
else:
    x1 = (-(b) + sqrt(delt)) / (2 * a)
    x2 = (-(b) - sqrt(delt)) / (2 * a)
    if delt == 0:
        print(f'a raiz desta equação é {x1}')

    if delt > 0:
        if x1 <= x2:
            print(f'as raízes da equação são {x1} e {x2}')
        else:
            print(f'as raízes da equação são {x2} e {x1}')
