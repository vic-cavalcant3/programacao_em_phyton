#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
posicao_incial = float(input('Posição inicial: '))
velocidade_inicial = float(input('Velocidade inicial: '))
tempo = float(input('Tempo: '))
aceleracao = float(input('Aceleração: '))

posicao_final = posicao_incial + velocidade_inicial * tempo + (aceleracao * (tempo **2)) / 2

print(f'A posição final de {posicao_incial} é {posicao_final}')