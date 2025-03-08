#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome


#Leitura de dados
nome = input('Digite o nome: ').strip()
nome_sem_espaco = nome.replace(' ', '')

#Primeiro nome
posicao_primeiro_espaço = nome.find(' ')
primeiro_nome = nome[:posicao_primeiro_espaço]
quantidade_letras_primeiro_nome = len(primeiro_nome)


#Prints
print(f'Nome em máiusculo: {nome.upper()} \n'
      f'Nome em minusculo: {nome.lower()} \n'
      f'Quantidade de letras: {len(nome_sem_espaco)} \n'
      f'A quantidade de letras do primeiro nome é:  {quantidade_letras_primeiro_nome}')

