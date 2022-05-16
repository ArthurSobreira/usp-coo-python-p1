def main():
    seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
    dias = seg // 86400
    horas = (seg % 86400) // 3600
    minutos = ((seg % 86400) % 3600) // 60
    seg_rest = ((seg % 86400) % 3600) % 60
    print(f'{dias} dias, {horas} horas, {minutos} minutos e {seg_rest} segundos.')

main()