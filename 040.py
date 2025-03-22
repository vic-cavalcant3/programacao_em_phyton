#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
'''''
n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
a, b = 0, 1  
contador = 0

while contador < n:
    print(a)  
    a, b = b, a + b  
    contador += 1  
'''''

#COREÇÃO PROFESSOR
n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
contador = 0
proximo = 0
atual = 1
anterior = 1

while contador < n:

    if contador == 0:
        print(0)
    elif contador == 1:
        print(1)
    elif contador == 2:
        print(1)
    else:
        proximo = atual + anterior
        anterior = atual
        atual = proximo

        print(proximo)
    contador+=1