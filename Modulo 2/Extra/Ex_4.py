# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE

soma=0
contador=0

while contador <len(notas):
    nota = float(notas[contador])
    soma=soma+nota
    contador=contador+1
print(soma/len(notas))



# LOOP FOR

soma=0

for nota in notas:
    numero=float(nota)
    soma=soma+numero
    
print(soma/len(notas))