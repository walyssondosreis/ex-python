#coding:utf-8
#Titulo: Exemplo de Dicionário passando duplas de valores com map() para funções

def fdic(componentX):
    print ('[ Key:'),componentX[0],('] [ Value:'),componentX[1],']'

dic={50:'Horse',33:'Chicken',14:'Mouse'}
dic2={'Turtle':12,'Spider':11,'Monkey':44}

#map(fdic,dic)
map(fdic,dic2.items())
print
map(fdic,dic.items())