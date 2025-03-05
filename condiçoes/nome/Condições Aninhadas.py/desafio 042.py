#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou nao formar um triangulo

r1=float(input('Digite a reta 1: '))
r2=float(input('Digite a reta 2: '))
r3=float(input('Digite a reta 3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 >r2:
    print('Você consegue formar um triangulo')
    if r1 == r2 != r3:
        print('o seu triangulo é quase perfeito sendo um \033[35m isósceles \033[m')
    elif r1 == r2 == r3:
        print('o seu triangulo é perfeito sendo um \033[32m equilátero \033[m')
    elif r1 != r2 != r3:
        print('todos os lados sao diferentes, logo ele é um \033[31m escaleno \033[m')
else:
    print('Você nao consegue formar um triangulo')

#A LOGICA DESSE DESAFIO É : A R3 NÃO PODE SER MAIOR QUE A R1 E R2 SOMADAS 
# [EX: R1= 5 R2= 5 R3= 11 NAO FORMA UM TRIANGULO POIS O R3 É MAIOR QUE A SOMA DE R1 E R2]
# [EX: R1= 5 R2= 5 R3= 9 FORMA UM TRIANGULO POIS O R3 É MENOR QUE A SOMA DE R1 E R2]

# AND é para juntar DUAS CONDIÇÕES E AMBAS DEVEM SER VERDADEIRAS