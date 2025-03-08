#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#Leitura de dados
n1 = float(input('Qual foi a PRIMEIRA nota do aluno? '))
n2 = float(input('Qual foi a SEGUNDA nota do aluno? '))
n3 = float(input('Qual foi a TERCEIRA nota d1o aluno? '))
n4 = float(input('Qual foi a QUARTA nota do aluno? '))
n5 = float(input('Qual foi a QUINTA nota do aluno? '))
n6 = float(input('Qual foi a SEXTA nota do aluno? '))

#Media do aluno
media = (n1+n2+n3+n4+n5+n6) / 6

#Resultado da media do aluno
print(f'A media do aluno é: {media:.1f}')