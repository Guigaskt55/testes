#Crie um programa que leia um numero inteiro e mostre na tela se le é par ou impar

num=int(input('Digite um número: '))


if num % 2 == 0: # # Se o resto da divisão por 2 for 0, é par
    print(f'o número digitado é par ')
else:
    print(f'o número digitado é ímpar ')
    
#Em vez de criar uma variável extra, pode fazer tudo na linha do if