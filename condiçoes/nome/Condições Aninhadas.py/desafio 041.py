#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade>

# até  9 anos :mirim
# até 14 anos:infantil
# até 19 anos:junior
# até 20 anos:sênior
# acima: master

idade=int(input('quantos anos voce tem? '))

if idade <= 9 :
    print('parabens você é mirim')
elif idade <= 14 :
    print('você está na categoria infantil, logo logo voce se tornara junior, parabens')
elif idade <= 19 :
    print('você ja se torno junior ? uau, que incrivel!! ')
elif idade <= 20:
    print(input('sênior com 20 anos é algo que todos almejam nao é mesmo ?'))
    if 'sim':
        print('E você é aquele que conseguiu, que demais!!')
    else:
        print('é uma otima perspectiva')
else:
    print('você está acima de todos, o grande master que luta pela sua nação em busca da medalha olimpica')
        
    