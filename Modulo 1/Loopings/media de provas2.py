print ('MEDIA DAS PROVAS 2')
prova=int(input('Informe a quantidade de provas: '))
contador=1
soma=0
while contador<=prova:
    soma=soma+notas
    notas=float(input(f'Informe a sua nota da prova {contador}: '))
    contador=contador+1
media=soma/prova
print (media)