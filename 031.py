#Escreva um programa que verifique se uma palavra é um palíndromo.
#Palíndromo é uma palavra, frase ou número que se lê igual da esquerda para a direita ou da direita para a esquerda
#Ovo
#Osso
#Ana

palavra = input('Digite a palavra por favor: ').strip().lower()
pontos =0


for i in range(0, len(palavra)):
    if palavra[i] == palavra[ -i -1]:
        pontos = pontos +1

if pontos == len(palavra):
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')