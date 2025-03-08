#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

#Leitura de dados
numero = int(input('Digite um numero: '))

#Condição
if  numero == 1:
    print('Segunda-Feira')

elif numero == 2:
    print('Terça-Feira')

elif numero == 3:
    print('Quarta-Feira')

elif numero == 4:
    print('Quinta-Feira')

elif numero == 5:
    print('Sexta-Feira')

elif numero == 6:
    print('Sabado')

elif numero == 7:
    print('Domingo')

else:
    print('Por Favor, Digite um numero de 1 a 7')




