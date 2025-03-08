#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

#Leitura de dados
idade = int(input('Digite a idade: '))

#Condição
if idade >= 18:
    print(f'Maior de idade!!')
elif idade < 18:
    print(f'Menor de idade!!')