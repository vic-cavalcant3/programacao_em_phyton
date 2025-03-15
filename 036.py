#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''''
maior_peso = None
menor_peso = None #numeros vazios
  
    if menor_peso == None and maior_peso == None:
        menor_peso = peso
        maior_peso = peso
'''''


maior_peso = 0
menor_peso = 999999999



for i in range(7):
    peso = float(input('Digite o peso: '))


    if peso > maior_peso:
        maior_peso = peso

    elif peso < menor_peso:
        menor_peso = peso

print(f' O maior peso é {maior_peso} kg \n'
      f' O menor peso é {menor_peso} kg ')









