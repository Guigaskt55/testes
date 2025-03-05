import math
#Escreva um programa que leia dois numeros inteiros e compare-os. mostrando na tela uma mensagem:
#- o primeiro valor é maior
#- o segundo valor é maior
#nao existe valor maior, os dois sao iguais

#entrada= n1, n2
#processo=

n1=int(input('digite um numero inteiro'))
n2=int(input('digite mais um numero inteiro'))

if n1 > n2:
    print('o \033[32m primeiro numero\033[m é maior. ')
elif n2 >n1:
    print('o \033[31m numero 2\033[m é maior. ')
elif n2 == n1:
    print('\033[35m são os mesmos valores\033[m')