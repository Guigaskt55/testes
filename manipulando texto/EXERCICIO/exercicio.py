nome=str(input('me fale seu nome inteiro: '))

print(f'\033[35m{nome.upper()}\033[m')#todas as letras maiusculas

print(f'\033[35m{nome.lower()}\033[m')#todas as letras minusculas

print(f'\033[31m{len(nome.replace(' ',''))}\033[m')# len conta quantos indices numericos tem na strin e o replace substitui

print(f'\033[31m{len(nome.split()[0])}\033[m')#len conta quantos indices numericos tem na string