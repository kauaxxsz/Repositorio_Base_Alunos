nome=input('Informe seu nome: ')
peso=float(input('Infome seu peso: '))
altura=float(input('Informe sua altura: '))
IMC= peso / (altura ** 2)
print()
if IMC >= 40:
    print(f'{nome} Voce esta com ')
elif IMC >= 35:
    print(f'Obesidade Grau II')
elif IMC >= 30:
    print(f'Obesidade Grau I')
elif IMC >= 25:
    print(f'Sobrepeso')
elif IMC >= 18.5:
    print(f'Peso normal')
else:
    print(f'{nome} você esta ABAIXO DO PESO, Procure ajuda médica e cuide da saúde.')
print()