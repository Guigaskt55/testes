# STYLE 0 NONE(nenhum estilo) 1 BOLD(NEGRITO) 4 (UNDERLINE) NEGRITO 7 NEGATIVE (INVERTER )
#?TEXT  30  WHITE 31  RED 32 GREEN 33 YELLOW 34 BLUE 35 PURPLE 36 BLUE OCEAN 37 GRAY (MAIS CORES APENAS COM IMPORTAÇÕES)
#*!BACK (COR DO FUNDO DO PADRÃO ANSI) 40  WHITE 41  RED 42 GREEN 43 YELLOW 44 BLUE 45 PURPLE 46 BLUE OCEAN 47 GRAY (MAIS CORES APENAS COM IMPORTAÇÕES)

#print('\033[0;30;41m TESTE')

#print('\033[7;37;45m TESTE \033[m')

#print('\033[30m TESTE \033[m')
#Cores= {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7:30m'}
#print(f"{Cores['amarelo']}{nome}{Cores['limpa']}")
nome=input('digite seu nome: ')

cores={'Limpa':'\033[m',
       'yellow':'\033[33m',
       'purple':'\033[35m'}

print(f'{cores["purple"]}{nome}{cores['Limpa']}')

