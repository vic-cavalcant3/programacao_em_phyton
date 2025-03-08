#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''''
#Leitura de dados
idade = int(input('Digite sua idade: '))
peso = float(input('Digite sua peso: '))
saude = input('Você está se sentindo bem? (s/n) : ').lower()
medicamento = input('Você está tomando algum remedio? (s/n) : ').lower()
gravidez = input("Você está grávida? (s/n) : ").lower()
amamentacao = input("Está amamentando? (s/n): ").lower()
viajem = input("Você viajou recentemente para alguma área endêmica? (s/n): ").lower()


#Condição
if idade < 16 or idade > 60:
    print(f'Idade inválida para doação')
if peso < 50:
    print(f'Peso abaixo do limite mínimo para doação')

if saude != 's':
    print("Você precisa estar saudável para doar sangue.")

if medicamento != 's':
    print(f'Você não pode estar tomando medicamentos que afetem a doação.')

if gravidez == 's':
    print("Grávidas não podem doar sangue.")

if amamentacao == 's':
    print("Mulheres amamentando devem esperar pelo menos 12 meses após o parto.")

if viajem == 's':
    print("Você não pode doar sangue após viajar para áreas endêmicas recentemente.")

else:
    print("Você pode ser doador de sangue!")
'''''


#=======================================================================================================================


'''''
idade = int(input('Digite sua idade: '))
peso = float(input('Digite sua peso: '))
horas_sono = int(input('Horas de sono: '))
consumo_bebida = input('Consumiu bebida alcolina nas ultimas 12 horas (S/N)').upper() .strip() [0]

if idade >16 and idade <60 and peso> 50 and horas_sono > 5 and consumo_bebida == 'N':
    print('Você pode doar sangue!!!')
else :
    print('Você nao pode doar!!')
'''''


#=======================================================================================================================


idade = int(input('Idade: '))
if idade >16 and idade <69:
    peso = float(input('Peso: '))
    if peso > 50:
        horas_sono = int(input('Horas de sono: '))
        if horas_sono > 5:
            consumo_bebida = input('Consumiu bebida alcolina nas ultimas 12 horas (S/N)').strip() .upper() [0]
            if consumo_bebida == 'N':
                print('Pode doar')
            else:
                print('Não poderia consumir bebida alcolica!!')
        else:
            print('Horas de sono incorretaa')
    else:
        print('Peso Incorreto')
else:
    print('Idade Incorreta')