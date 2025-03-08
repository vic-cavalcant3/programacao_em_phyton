#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123")

#Leitura de dados
senha = input(f'Digite sua senha por favor: ')

#Condição
if senha == 'python123':
    print('A senha está correta, Seja bem vindo!!!!')
else :
    print('Senha Incoreta')