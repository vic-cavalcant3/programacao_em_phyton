#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

#Leitura de dados
numero = int(input('Digite o numero: '))

#Condição
if numero % 2 == 0:
    print(f'O numero é par!! ')
elif numero % 2 == 1:
    print(f'O numero é impar!! ')