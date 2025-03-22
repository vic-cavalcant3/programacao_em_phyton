#OPERAÇÕES MATEMÁTICAS===============================

'''
print( 45 + 9)
print(8166 - 80)
print(587 / 4)
print(25 * 10)
print(4 ** 0.5)

print('Olá Mundo!!!')

#Print Formatado (Texto + Variavel)
idade = 45
print(idade)
print(f'Sua idade é {idade}')


#Leitura de Dados
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(f'Seu nome  é {nome} , e você tem {idade} anos')

#Tipos de dados
idade_1 = int(input("Digite a primeira idade: "))
idade_2 = int(input("Digite a outra idade: "))
soma_idades = idade_1 + idade_2
print(f"A soma das idades é {soma_idades}")


#STRINGS============================

senai = 'Luis Eulálio'

#Fatiamento
print(senai[0])
print(senai[3:7])


#BIBLOTECAS=========================
import random

random.randint(1,3)
print(pc)


for i in range (1,10):  #varios *
    print(f'*')

for i in range (1,10): #crescente
    print(i)


for i in range (10,1,-1): #decrescente
    print(i)

soma = 0
for i in range (0,10):
    n = int(input('Digite um numero: '))
    soma = soma + n
    print(soma)


contador = 0

while contador < 5:
    print(f'O contador é {contador}')
    contador += 1
    print('Loop concluído!')

#Parada com strings
resposta = ''

while resposta != 'N':
    print('Bem vindo')
    resposta = input('Deseja continua? [S/N]: ').upper().strip([0])
'''




