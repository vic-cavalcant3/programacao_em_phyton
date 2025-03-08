#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

#Leitura de dados
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
cidade_nascimento = input('Digite sua cidade de nascimento: ')

#Retorno de dados
print(f'O seu nome é {nome}, você tem {idade} anos. \nVocê nasceu na cidade de {cidade_nascimento}')