#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
resposta = ''
soma = 0
contador = 0

maior =None
menor =None

while resposta != 'N':
    n = int(input('Digite um número: '))

    if menor == None and maior == None:
        maior = n
        menor = n

    if n < menor:
        menor = n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    if n > maior:
        maior = n

    soma += n
    contador +=1
    resposta = input('Deseja continuar?? [S/N]').upper().strip()[0]

print(f' A media é {soma/contador}'
    f'\n O maior numero é {maior}'
    f'\n O menor numero é {menor}')