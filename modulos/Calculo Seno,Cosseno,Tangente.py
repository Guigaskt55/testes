import math
#faça um programa que leia um angulo qualquer e mostre na tela o valor do cosseno seno tangente

angulo = float(input('digite um numero em graus: '))

angulos_radianos = math.radians(angulo)

seno =math.sin(angulos_radianos)
cosseno =math.cos (angulos_radianos)
tangente =math.tan (angulos_radianos)

print(f'o angulo de \033[32m{angulo}\033[m graus tem:')
print(f'seno \033[31m{seno:.2f}\033[m')
print(f'cosseno \033[31m{cosseno:.2f}\033[m')
print(f'tangente \033[31m{tangente:.2f}\033[m')

