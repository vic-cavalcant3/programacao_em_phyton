#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
'''''
for i in range (1, 10 +1):
    if i % 2 == 0:
        soma = soma + i
        print(soma)
'''''

soma = 0
for i in range (1, 10 +1):
    numeros = int(input('Digite um numero por favor: '))

    if numeros % 2 == 0:
        soma = soma + numeros

print(f'a soma é {soma}')