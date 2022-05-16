num = str(input('Digite um número: '))
soma = 0
for c in num:
    soma += int(c)

print(f'A soma dos digitos de {num} é {soma}')