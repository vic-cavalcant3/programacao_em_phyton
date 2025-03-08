#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o primeiro numero: '))

for i in range(n1 , n2 + 1):
    if i % 2 == 0:
        print(i)