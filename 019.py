#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

#Leituraa de dados
numero = int(input('Digite um numero: '))

#Condição
if  0 <=  numero  <= 10:
    print(f'O numero está entre 0 e 10!!')
elif 10 < numero <= 20:
    print(f'O numero está entre 10 e 20!!!')
elif numero > 20:
    print(f'O numero é maior que 20!!')
else:
    print(f'NEGATIVO')