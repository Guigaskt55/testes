# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO


ano=(int(input('digite um ano aleatório:')))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
# bissexto é quando o ano é divisivel por 4 ( 4 == 0)
# bissexto nao pode ser divisivel por 100 (100 != 0) (!= 0 significa ''diferente de'' verifica se os dois valores nao sao iguais, impede que o programa aceite anos que nao sao divisiveis por 4 ou 400)
# Divisível por 4 e não divisível por 100, ou divisível por 400.
    print(f'o ano é bissexto')
else:
    print(f'o ano não é bissexto')
    