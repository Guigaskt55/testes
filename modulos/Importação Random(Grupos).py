import random
import time
grupo=random.randint(1,4)

grupo1='thais'
grupo2='guigas'
grupo3='duds'
grupo4='mariana'

grupos=[grupo1,grupo2,grupo3,grupo4]

print(f'Bom, temos 4 grupos liderados por \033[31m{grupo1}\033[m, \033[35m{grupo2}\033[m, \033[33m{grupo3}\033[m e por fim o grupo da \033[36m{grupo4}\033[m')
time.sleep(2)
print(f'com isso faremos um sorteio de quem ira apresentar primeiro')

random.shuffle(grupos)

time.sleep(2)

print('a ordem dos grupos para apresentação é: ')

for i, grupo in enumerate(grupos,1):
    print(f'{i}° lugar: \033[33m{grupo}\033[m')