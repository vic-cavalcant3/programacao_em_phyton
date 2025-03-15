#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

soma = 0
for i in range (501):
    if i % 4 == 0:
        soma = soma + i
        print(soma)
'''''
for i in range (0,501,4):
    print(i)
'''''