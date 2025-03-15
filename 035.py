#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:

#A média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos

soma_idades = 0
quant_mulheres_menos_20_anos = 0
idade_home_mais_velho = 0
nome_home_mais_velho = 0

for i in range(4):
    nome = input('Digite o nome: ') .strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo? [M/F] ') .strip() .lower() [0]

    soma_idades += idade

    if sexo ==  'M' and idade > idade_home_mais_velho:
        idade_home_mais_velho = idade
        nome_home_mais_velho = nome




    if sexo == 'F' and idade < 20:
        quant_mulheres_menos_20_anos += 1

    print(f'1. A media de idades é {soma_idades / 4} \n'
          f'2. Nome do homem mais velho é {nome_home_mais_velho} \n'
          f'3. Mulheres mais velhas: {quant_mulheres_menos_20_anos}')