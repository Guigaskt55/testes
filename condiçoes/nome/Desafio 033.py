#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1=int(input('Digite um número'))
n2=int(input('Digite outro número'))
n3=int(input('Digite mais um número'))

maior=max(n1, n2, n3)

menor=min(n1, n2, n3)

print(f'O maior numéro é {maior}')
print(f'O menor numéro é {menor} ')