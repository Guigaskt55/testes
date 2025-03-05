
#? elabore um programa que calcule o valor a ser pago por um produto, considerando o seu  [preço normal] e [condição de pagamento]
#? -a vista [dinheiro/cheque]  :   10% de desconto
#? -á vista no [cartão]        :   5% de desconto
#? -em ate [2x no cartao]      :   preço normal
#? 3x ou mais no cartão        :   20% de juros



# FUNÇÃO PARA CALCULAR VALOR FINAL COM BASE NA FORMA DE PAGAMENTO
def calcular_valor_final(preço, forma_pagamento):
    if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
        return preço * 0.90 # 10% de desconto 
    elif forma_pagamento == 'cartão_avista':
        return preço * 0.95 # 05% de desconto
    elif forma_pagamento == 'cartão_2x':
        return preço        # preço normal
    elif forma_pagamento == 'cartão_3x_ou_mais':
        return preço * 1.20 # 20% de juros
    else:
        return preço # caso a forma de pagamento nao seja reconhecida
    
    #dicionário
Produtos = {
    'consoles':{
        'playstation 5'      : 4500.00,
        'Xbox series x'      : 4000.00,
        'nintendo switch'    : 2000.00
    },

    'celulares':{
        'iphone 16'          : 8639.11,
        'samsung galaxy s21' : 5000.00,
        'xiaomi mi 11'       : 3000.00,
        'motorola edge'      : 2500.00
    },
    'notebooks':{
        'dell xps'           : 8000.00,
        'lenovo thinkpad'    : 7000.00,            
        'samsung book'       : 5000.00,      
        'macbook pro'        : 12000.00       
    },
    'eletrodomesticos':{
        'geladeira'          : 3000.00,
        'microondas'         :  800.00    
    }
}

print('bem vindo à nossa loja!')
print('Temos os seguintes produtos disponíveis')
print('1. \033[32m Consoles \033[m')
print('2. \033[32m Celulares \033[m')
print('3. \033[32m notebooks \033[m')
print('4. \033[32m eletrodomésticos \033[m')

#Escolh o tipo de produto
categoria=input('Digite o número correspondente ao tipo de produto que voce deseja: ') # solicitar ao usuário o número do produto ao inves do nome, pode diminuir erros

if categoria == '1':
    tipo_produto ='consoles'
elif categoria == '2':
    tipo_produto ='celulares'
elif categoria == '3':
    tipo_produto ='notebooks'
elif categoria == '4':
    tipo_produto ='eletrodomesticos'
else:
    print('Opção inválida. Encerrando o programa.')
    exit()
    
#Mostra os produtos disponíveis no tipo escolhido
print(f'\nVocê escolheu {tipo_produto}. Temos os seguintes produtos disponíveis:')
for produto in Produtos [tipo_produto]:
    print(f'- {produto.capitalize()}')
   
#Escolha do produto especifico 
escolha_produto=input('Digite o nome do produto que voce deseja: ').lower()

#verificar se o produto existe
if escolha_produto not in Produtos [tipo_produto]:
    print('Produto não encontrado. Encerrando o programa.')
    exit()
    
#Obter o preço do produto
preço_produto = Produtos[tipo_produto][escolha_produto]
    
print("\nFormas de pagamento disponíveis:")
print("1. À vista (dinheiro/cheque) - 10% de desconto")
print("2. À vista no cartão - 5% de desconto")
print("3. Em até 2x no cartão - Preço normal")
print("4. 3x ou mais no cartão - 20% de juros")

escolha_pagamento=input('Digite o número correspondente à forma de pagamento:')

if escolha_pagamento == '1':
    forma_pagamento = 'dinheiro'
elif escolha_pagamento == '2':
    forma_pagamento = 'cartão_avista'
elif escolha_pagamento == '3':
    forma_pagamento = 'cartão_2x'
elif escolha_pagamento == '4':
    forma_pagamento = 'cartão_3x_ou_mais'
else:
    print('Forma de pagamento inválida. Encerrando o programa.')
    exit()
    
#Calcular o valor final
Valor_final=calcular_valor_final(preço_produto, forma_pagamento)

#Mostra o valor final
print(f"\nO valor original do {escolha_produto.capitalize()} é: R$ {preço_produto:.2f}")
print(f"O valor a ser pago é: R$ {Valor_final:.2f}")

