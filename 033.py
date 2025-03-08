#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

inicio = 1
fim = 100
soma = 0

for i in range (inicio, fim +1):
    if i % 4 == 0:
        soma = soma + i
        print(soma)