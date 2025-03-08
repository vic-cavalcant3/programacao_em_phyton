#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

#Leitura dos dados
nota1 = float(input('Digite a primeira nota por favor: '))
nota2 = float(input('Digite a segunda nota por favor: '))
nota3 = float(input('Digite a terceira nota por favor: '))
nota4 = float(input('Digite a quarta nota por favor: '))
nota5 = float(input('Digite a quinta nota por favor: '))

#Calculo da media
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

#Condição

if media < 6:
    print(f'INSUFICIENTE')
elif 6 <= media <= 7:
    print(f'SUFICIENTE')
elif 7 < media <=9:
    print(f'BOM')
elif 9 < media <= 10:
    print(f'EXCELENTE')

