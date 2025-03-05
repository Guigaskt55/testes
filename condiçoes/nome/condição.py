import random
nome =str(input('qual é seu nome'))
if nome =='Guilherme':
    print('que nome lindo voce tem!')
else:
    print('Seu nome é tão normal')
print(f'bom dia, {nome}!')

#MÉDIA NOTA CONDIÇÃO COMPOSTA
n1=float(input('digite a primeira: '))
n2=float(input('digite a segunda nota: '))
m = (n1+n2)/2
print(f'a sua media foi {m:.1f}')
if m>=6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('sua média foi ruim! ESTUDE MAIS!!!')

#MÉDIA NOTA CONDIÇÃO SIMPLES
num1=(float(input('digite a primeira nota: ')))
num2=float(input('dgite a segunda nota: '))
Mf=(num1+num2)/2
print(f'a sua média final foi {Mf:.1f}')
print('Parabens'if Mf >=6 else 'ESTUDE MAIS!')    

# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA
# PARA O USUARIO TENTAR DESCOBRI QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR.
#O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU
num=random.randint(1,5)
palpite=(int(input('qual numero de 1 a 5 voce acha q é ?')))

if palpite == num:
    print('parabens!voce venceu. ')
else:
    print(f'voce perdeu! o numero certo era {num}')


