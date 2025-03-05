numero=(int(input('escolha um número para ver sua tabuada')))

print(f'/ntabuada do {numero}:')
print('-'*11)
for i in range(1,11):
    print(f'|{numero:2}X{i:2}={numero*i:3}|')
print('-'*11)

#° \n	Nova linha	Pula para a próxima linha
#°For ''i'' range(1,11) é para repetir quantas vezes caso queira 100 precisa colocar 101 sempre 1 a mais
#°o I é apenas o contador que vai passando de 1 até 10. (variável)

       