#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#Leitura de dados
raio = float(input('Digite o raio da esfera: '))

#Operação Matematica
volume = (4/3) * 3.1415 * raio**3
area = 4 * 3.1415 * raio ** 2

#Resultado da conta
print(f'O Volume do raio ({raio}) é {volume:.2f}' )
print(f'A Área do raio ({raio}) é {area:.2f}')
