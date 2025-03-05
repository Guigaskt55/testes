#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar [valor da casa], o [salário] do comprador e em [quantos anos]ele vai pagar

#CALCULE o valor da pretação mensal, sabendo que ela nao pode exceder [30%] do salário ou entao o empréstimo sera negado

#entradas=valor da casa/salario/anos 
#processamento=
#saidas=

valor_da_casa=float(input('qual séria o valor da casa em que o senhor tem interesse?'))
salario=float(input('Preciso saber seu salário para entrar em análise. '))
anos=int(input('Em quantas anos deseja pagar ? '))

meses=anos*12
parcelas_mensais=valor_da_casa/meses # calcula quanto sera cada parcela
limite= salario*0.30


color={
    'limpa':'\033[30m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
  }




print(f'O valor da prestação será de R$ {color["verde"]}{parcelas_mensais:.2f}{color["limpa"]} por mês.')

if parcelas_mensais <= limite:

    print(f'{color["verde"]}Parabens,podemos seguir com o empréstimo de sua casa{color["limpa"]}')
else:
    print(f'{color["vermelho"]}Emprestimo negado, pois passa de 30% do seu salário, sinto muito{color["limpa"]}')