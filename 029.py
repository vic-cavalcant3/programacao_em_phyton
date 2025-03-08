#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''''
numero = int(input('Digite um numero por favor: '))

for i in range (1,11):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')
'''''

import random
numero = int(input('Digite O numero de exercicios que deseja: '))

for i in range (1, numero):
    print(f' {random.randint(1, 10)} X {random.randint(1, 10)  } = ')
