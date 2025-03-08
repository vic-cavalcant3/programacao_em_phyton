#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time


maquina = random.randint(1,3)
jogador = int(input('Digite 1 para: PEDRA \n'
                'Digite 2 para: PAPEL \n'
                'Digite 3 para: TESOURA \n'))

print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
print('Ainda pensando!.....')
time.sleep(1)


if jogador == maquina:
    print(f'EMPATE!!')

elif jogador == ' ':
    print('Por favor, escolha um numero')


elif (jogador == 1 and maquina == 3) or (jogador == 2 and maquina == 1 ) or (jogador == 3 and maquina == 2 ):
    print(f'GANHOU!! {jogador} X {maquina}')

else:
    print(f'Perdeu {jogador} X {maquina}')

