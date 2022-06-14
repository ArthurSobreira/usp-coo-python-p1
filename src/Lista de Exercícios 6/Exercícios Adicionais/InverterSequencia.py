my_list = []

while True:
    num = int(input('Digite um número: '))
    if num != 0:
        my_list.append(num)
    else:
        break


for c in range(1, len(my_list)):
    print(my_list[c*(-1)])
print(my_list[0])
