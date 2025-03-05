#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario,com 15% de aumento
Salário=float(input('qual é o seu salário ? R$'))
Aumento_salarial=float(input('qual é o percentual do aumento ?'))

aumento=Salário*(Aumento_salarial/100)
salário_com_aumento=Salário+aumento

print(f'o valor do aumento é {aumento}')
print(f'o seu novo salário com o aumento será {salário_com_aumento}')                           