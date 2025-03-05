# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu [IMC] e mostre seu status, de acordo com a tabela abaixo:
#-abaixo de 18.5:    abaixo do peso
#-entre 18.5 e 25:   peso ideal
#-25 até 30:         sobrepeso
#-30 até 40:         obesidade
#-acima de 40:       obesidade morbida
peso=float(input('digite seu peso [xx.xx]'))
altura=float(input('digite sua altura[x.xx]'))

IMC=peso/(altura*altura)

if IMC <18.5:
    print('abaixo do peso')
elif 18.5 <= IMC <= 25: # 18.5 < IMC significa que 
    print('peso ideal')
elif 25 <= IMC <= 30:
    print('sobrepeso')
elif 30 <= IMC <= 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade morbida')

print(f'seu IMC é {IMC:.2f}')

