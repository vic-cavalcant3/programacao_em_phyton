#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário
# faça depósitos,
# saques e
# consulte o saldo da conta,
# e sair

saldo = 0
resposta = 0
while resposta != 4:
    resposta = int(input('1. Depósito'
                         '\n2. Saque'
                         '\n3. Consultar Saldo'
                         '\n3. Sair-------->'))

    if resposta == 1:
        deposito = float(input('Quanto deseja depositar? '))
        saldo += deposito

    elif resposta == 2:
        saque = float(input('Quanto deseja sacar? '))
        saldo -= saque

    elif resposta == 3:
        print(f'Seu saldo é {saldo}')

    elif resposta == 4:
        print('Até logo!!')

    else:
        print('Opção Invalida!' )