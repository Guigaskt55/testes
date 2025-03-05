cidade=(input('\033[36mfale o nome de uma cidade :\033[m '))
começa_com_santo= cidade.lower().startswith(('santo','santa')) # startswith verifica se o texto começa com 'santo' ou nao. dentro do startwith quanto mais opção mais () () ()
if começa_com_santo :
    print("\033[32ma cidade começa com 'santo' ou 'santa .\033[m")
else :
    print("\033[31ma cidade não começa com 'santo' ou 'santa' .\033[m")
    