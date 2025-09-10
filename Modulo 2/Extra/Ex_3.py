# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

numero=1

quantidade=int(input('Digite a quantidade de fimes a ser adicionado: '))

while numero <=quantidade:
    filme=input('Digite o Filme a ser adicionado: ')
    filmes.append(filme)
   
    numero=numero+1
print(filmes)

# LOOP FOR

quantidade=int(input('Digite a quantidade de fimes a ser adicionado: '))

for filme in range(quantidade):
    filme=input('Digite o Filme a ser adicionado: ')
    filmes.append(filme)
print(filmes)

