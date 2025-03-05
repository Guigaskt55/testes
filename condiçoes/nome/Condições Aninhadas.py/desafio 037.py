import math

#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base da conversao
#1 para binario
#2 para octal
#3 para hexadecimal

n=int(input('usuario me diga um numero inteiro por favor'))

escolha=(input('bin,oct,hex?'))

if escolha == 'bin':
    print(bin(n))
elif escolha == 'oct':
    print(oct(n))
else:
    print(hex(n))