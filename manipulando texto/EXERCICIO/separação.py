#faça um programa que leia um numero de 0a 9999 e mostre na tela cada um dos digits separados

numero =(input('escolha um numero de 1 a 9999:  ')).zfill(4)

milhar = numero[0]
centena= numero[1]
dezena= numero [2]
unidade= numero [3]

Cores={'azul':'\033[34m','limpa':'\033[m'}

print(f'milhar {Cores["azul"]}{milhar}{Cores['limpa']}')
print(f'centena {Cores['azul']}{centena}{Cores['limpa']}')
print(f'dezena {Cores["azul"]}{dezena}{Cores["limpa"]}')
print(f'unidade {Cores["azul"]}{unidade}{Cores["limpa"]}')