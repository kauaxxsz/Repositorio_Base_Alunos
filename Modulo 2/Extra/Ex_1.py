# Utilize um loop while e um loop for para contar de 0 até o número que o usuário digitar:

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# LOOP WHILE

valor=int(input('Digite um numero a ser contado: '))

numero=0
while numero <=valor:
    print(numero)
    numero+=1

# LOOP FOR
numero=int(input('Digite um numero a ser contado: '))

sequencia=0
for sequencia in range(0,numero):
    print(sequencia+1)