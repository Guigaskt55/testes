#Faça um programa quee leia a largura e a altura de uma parede em metros, 
#calcule sua area e a quantidade de tinta necessaria para pinta-la ,
# sabendo que cada litro de tinta pinta uma area de 2m²
largura=(float(input('Me informe qual é a largura dessa parede. ')))
altura=(float(input('quanto de altura tem a parede?')))

área=largura*altura

quantidade_tinta=área/2

print(f'A área da parede é {área:.2f}')
print(f'de acordo com a área da parede você precisaria de {quantidade_tinta:.2f} litros de tinta para pinta-la por completo') 