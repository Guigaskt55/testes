#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salário Superiores a R$ 1.250, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

Sálario_Atual=float(input('Digite Seu Sálario atual'))


if Sálario_Atual <= 1.250:
    sálario=Sálario_Atual*0.10#(0.10 = 10% de aumento)
else:
    sálario=Sálario_Atual*0.15#(0.10 = 15% de aumento)

novo_salário=Sálario_Atual+sálario
    
print(f'O aumento será de {sálario:.2f}, O seu novo salário será {novo_salário:.2f}')

#<=1250 é para se for maior tera um aumento de 10% [NO IF] e quando estiver abaixo [ELSE] o salário tera um aumento de 15% 