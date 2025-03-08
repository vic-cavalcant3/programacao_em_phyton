#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez

#leitura frase
frase = input('digite uma frase: ').strip().lower()
frase = frase.replace('á', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('ã', 'a')

#Análise
print(f'A letra "a" aparece: {frase.count('a')} vezes \n'
      f'O Primeiro "a" está na posição {frase.find('a') + 1} \n'
      f'O Ultimo "a" está na posição {frase.rfind('a') + 1}')
