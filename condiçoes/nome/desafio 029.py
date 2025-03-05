#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar ( 80KM ), Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acma do limite

velocidade=float(input('Digite a velocidade em que o carro passou'))


limite=81

if velocidade >= limite:
    multa= (velocidade-limite)*7
    print(f'Você ultrapassou o limite, sua multa sera de {multa:.2f} por ter corrido a {velocidade:.2f}')
else:
    print('você não excedeu o limite')