#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

#leitura de dados
numero = int(input('Digite um numero negativo ou positivo: '))

if numero > 0:
    input('POSITIVO')
elif numero < 0:
    input('NEGATIVO')
else:
    print('Não é um número')









'''''
#Sinal
sinal_numero = numero.find(' {numero} ')
primeiro_sinal = numero[:sinal_numero]

#Condição
if primeiro_sinal == ' - ':
    print('O seu numero é negativo')
elif primeiro_sinal == ' + ':
    print('O seu numero é positivo')
else:
    print('Numero não correspondido')
'''''