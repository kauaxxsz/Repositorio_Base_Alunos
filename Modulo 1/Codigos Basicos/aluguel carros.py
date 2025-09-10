# nome=input('Informe o seu veiculo: ')
# dias=int(input('Informe a quantidades de dias: '))
# KM=float(input('Informe a quantidade de KM rodados: '))

# if nome == '911':
#     valor_dias=int(dias*60)
#     valor_KM=float(KM*0.15)
#     total=(valor_dias+valor_KM)

# elif nome == 'R34':
#     valor_dias=int(dias*70)
#     valor_KM=float(KM*0.30)
#     total=(valor_dias+valor_KM)

# elif nome == 'nissam':
#     valor_dias=int(dias*67)
#     valor_KM=float(KM*0.20)
#     total=(valor_dias+valor_KM)


# print(' ')
# print (f'O valor com {dias} dias e com {KM}KM rodados vai ficar em {total}')


nome=input('Informe o seu veiculo: ')
dias=int(input('Informe a quantidades de dias: '))
KM=float(input('Informe a quantidade de KM rodados: '))

valor_por_dia = 0
valor_por_km = 0

if nome == '911':
    valor_por_dia = 200
    valor_por_km = 0.20
elif nome == 'R34':
    valor_por_dia = 150
    valor_por_km = 0.50
elif nome == 'nissam':
    valor_por_dia = 100
    valor_por_km = 0.30

else:
    valor_por_dia = 60
    valor_por_km = 0.15

valor_dias=int(dias*valor_por_dia)
valor_KM=float(KM*valor_por_km)
total=(valor_dias+valor_KM)

print(' ')
print (f'O valor com {dias} dias e com {KM}KM rodados vai ficar em {total}')
