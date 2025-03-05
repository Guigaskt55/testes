Preço_Original=float(input('Digite o preço original R$'))
desconto=float(input('Digite o percentual do desconto'))

valor_desconto=Preço_Original*(desconto/100)

preço_com_desconto=Preço_Original-valor_desconto

print(f'O valor do desconto é R${valor_desconto:.2f}')
print(f'O preço final do produto é R${preço_com_desconto:.2f}')