#Desenvolva um programa que pergunte a distancia de uma viagem em KM.Calcule o preço da passagem. Cobrando R$0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas
Viagem=(float(input('Qual a distancia de sua viagem ?')))

if Viagem <= 200:
    preço=Viagem*0.50
else:
    preço=Viagem*0.45
    
print(f'sua passagem final será {preço:.2f} ')