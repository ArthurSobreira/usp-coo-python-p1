my_list = []
num = (input('Digite um número: '))

adja = False
for c in num:
    my_list.append(int(c))

for c in range(0, (len(my_list) - 1)):
    if my_list[c] == my_list[c+1]:
        adja = True
    c =+ 1

if adja == True:
    print('sim')
else:
    print('não')
