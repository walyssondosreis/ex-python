# coding: utf-8
# TITULO: Verificação se Um Número é Perfeito Usando o método reduce()
# Autor: Walysson dos Reis

from functools import reduce

def somaPerfeito(a,b):
    #print 'Retorno da Soma',a+b
    return a+b


def verificaPerfeito(num):
    if num<2:return False
    listaDivisores=[]
    for i in range(1,num):
        if num%i==0: listaDivisores.append(i)
    #print '\nLista de Soma:',listaDivisores
    if(reduce(somaPerfeito,listaDivisores)==num): return True
    else: return False

while 1:
    try:
        num=int(input('Por Favor Digite um Número: '))
        break
    except: print('Cara, Realmente  tem que ser um NÚMERO!')

print ('NUMERO É PERFEITO?',verificaPerfeito(num))