import math

x1 = int(input('Digite o Valor de X no primeiro ponto: '))
y1 = int(input('Digite o Valor de Y no primeiro ponto: '))
x2 = int(input('Digite o Valor de X no segundo ponto: '))
y2 = int(input('Digite o Valor de Y no segundo ponto: '))
print(f'Primeiro Ponto: ({x1},{y1})\n'
      f'Segundo Ponto: ({x2},{y2})')

dis = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if dis >= 10:
    print('longe')
else:
    print('perto')
    