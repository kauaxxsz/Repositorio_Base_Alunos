nome=input('Seu nome: ')
idade=float(input('Sua idade: '))

if idade>17:
    print('Maior de idade')
    sim=input('Ja tem carteira de habilitacão 1= (sim) 2= (não): ')
    if sim=='1':
        print('Você ja pode ter seu veiculo.')
        print(':)')
    else:
        print('Você nâo pede dirigir!!!')
else:
    print('Menor de idade')
