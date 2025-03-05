#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
Reais=float(input('quanto você tem de dinheiro em reais ?'))

dol=Reais/5.714
eur=Reais/6.000
print(f'você tem R${Reais} e corvertidos em dolares seria ${dol:.2f} e acrescentando em euro voce téria {eur:.2f}')