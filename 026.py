#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

#leitura de dados
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

#Calculo
imc = (peso / altura ** 2)


#Condição
if imc > 25.5:
    print(f'O IMC ({imc:.2f}) É OBESO')

elif imc > 18.5:
    print(f'O IMC ({imc:.2f}) ESTÁ IDEAL')

else:
    print(f'O IMC ({imc:.2f}) ESTÁ ACIMA DO PESO')
