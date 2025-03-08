#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Leitura dos dados
numero = float(input('Digite o numero que deseja: '))

#Operação Matematica
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

#Resultado da Operação
print(f'O dobro do numero({numero}) é {dobro} \n'
      f'O triplo do numero({numero}) é {triplo} \n'
      f'A raiz do numero({numero}) é {raiz:.2f} ')