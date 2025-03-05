#fatiamento 
frase= 'Curso em video python'
print(frase[9])# pega o V de (video)
print(frase[9:13])# vai ate 'vide' ele não lê o ultimo 'o'  indice 
print(frase[1:6:2]) # puxa curso porem o '2' pula de 2 em 2 entao ficaria 'cs'
print(frase[2:]) 
print(frase[15:])# indiquei o inicio mas nao indiquei o final o python entende que queremos completo
print(frase[15::3]) #pula de 2 em 2 porem facil até o final