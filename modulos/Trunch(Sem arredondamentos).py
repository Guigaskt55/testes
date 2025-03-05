import math
#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
num=float(input('\033[35mescolha um número com casas decimais (ex:16.99)\033[m'))
trunc=math.trunc(num)
print(f'\033[31m{trunc}\033[m')