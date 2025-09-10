print ('escolha uma opcao')
print ('1- dolar em real')
print ('2- real em dolar')

opcao = int(input('digite a opcão: '))
valor = float(input('informe a cotacão do dolar: '))

if opcao == 1:
    dolares = float(input('infome a quantidade de dolares: '))
    print(f'o valor em reais e de R${valor*dolares:.2f}')
    
elif opcao == 2:
    reais = float(input('informe a quantidade de reais: '))
    print(f'o valor em dolares é ${reais/valor:.2f}')

else:
    print('Essa opcão nao existe')