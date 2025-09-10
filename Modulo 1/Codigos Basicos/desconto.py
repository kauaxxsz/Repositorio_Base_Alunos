nome = input('Nome do Produto: ')
preço_total = float(input('Preço do produto: '))
porcentagem = float(input ('Porcentagem do desconto: '))
desconto = preço_total * (porcentagem / 100)
valor_novo = preço_total - porcentagem

print('A',nome, 'De valor',preço_total,'com',porcentagem,'% de desconto, é de:',valor_novo)
print(f'A {nome} De valor {preço_total} com {porcentagem}% de desconto, é de: {valor_novo}')