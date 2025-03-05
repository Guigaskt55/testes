m1=float(input('Me fale sua nota na m1: '))
m2=float(input('Agora sua nota em M2: '))

média=(m1+m2+m2)/3 # COLOCAR EM () para nao confundir deixar claro que depois da soma voce quer dividir

if média >= 5 :
    print('Aprovado')
elif média >= 3 :
    print('Você terá que realizar o exame')
else:
    print('reprovado')
    