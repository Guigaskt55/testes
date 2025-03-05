import math
#faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
cateto_adjacente=float(input('digite o comprimento do cateto adjacente'))

#ou

cateto_adj=float(input('digite o comprimento do cateto adj '))
cateto_oposto=float(input('digite o comprimento do cateto oposto'))

hipotenu=math.hypot(cateto_adj,cateto_oposto)

print(f'A hipotenusa do triangulo com o cateto adj e cateto oposto é \033[32m{hipotenu:.2f}\033[m')