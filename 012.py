#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#leitura de dados
nome = input('Digite o nome: ').strip()

#Primeiro nome
primeiro_espaco = nome.find(' ')
primeiro_nome = nome[:primeiro_espaco ]
#primeiro_nome = nome[:nome.find(' ')

#Ultimo nome
ultimo_espaco = nome.rfind(' ')
ultimo_nome = nome[ultimo_espaco + 1: ]
#ultimo_nome = nome[nome.find(' ':)



print(f'O Primeiro nome é: {primeiro_nome} \n'
      f'O Ultimo nome é: {ultimo_nome}')