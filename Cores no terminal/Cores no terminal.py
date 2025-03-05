#ANSI (PADRAO NORMALIZAÇÃO INTERNACIONAL) [ESCAPA SEQUENCE](Utiizar dentro do terminal)

#ANSI PARA CORES  \033[ 
#EXEMPLO:\033[0;33;44m

#\033[STYLE;TEXT;BACK M

#*!STYLE 0 NONE(nenhum estilo) 1 BOLD(NEGRITO) 4 (UNDERLINE) NEGRITO 7 NEGATIVE (INVERTER )
#?TEXT  30  WHITE 31  RED 32 GREEN 33 YELLOW 34 BLUE 35 PURPLE 36 BLUE OCEAN 37 GRAY (MAIS CORES APENAS COM IMPORTAÇÕES)
#BACK (COR DO FUNDO DO PADRÃO ANSI) 40  WHITE 41  RED 42 GREEN 43 YELLOW 44 BLUE 45 PURPLE 46 BLUE OCEAN 47 GRAY (MAIS CORES APENAS COM IMPORTAÇÕES)

#print('\033[0;30;41m TESTE')

#print('\033[7;37;45m TESTE \033[m')

#print('\033[30m TESTE \033[m')

a = 3
b = 5
print (f'Os valores são \033[32m {a}\033[m e \033[31m {b}')#? ainda depois do 32 pode colocar  + ;40/47 para decidir o fundo


nome= 'guigas'
Cores= {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7:30m'}

print(f"{Cores['amarelo']}{nome}{Cores['limpa']}")
#! abrir f'{ colocar a lista de cores [colocar o nome da cor ]}{nome}{Cores['limpa']}') 'limpa serve para desativar a cor