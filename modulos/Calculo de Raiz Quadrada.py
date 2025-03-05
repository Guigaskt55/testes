import math

Cores={
    'limpa':'\033[m',
    'purple':'\033[35m',
    'vermelho':'\033[31m'
    }


num=int(input('digite um número:'))

raiz =math.sqrt(num)
print(f'A raiz de {Cores["vermelho"]}{num}{Cores["limpa"]}  é igual a {Cores["purple"]}{math.ceil(raiz)}{Cores["limpa"]}')