#coding: utf-8
#Título: Função(def) Verificadora de Números Primos
#Autor: Walysson dos Reis

def primoVerifica(num):
    for i in range(2, num):
        print ('valor de i: %d' % i)
        print ('valor de num: %d' % num)
        if (num % i == 0):
            return False
        elif (i == num - 1):
            return True
    if (num == 0 or num == 1): return False
    if (num==2): return True

while 1:
    try:
        num=int(input('Digite o Número a ser testado: '))
        if(num<0): num+'vaca' #Teste feito apenas para disparar excessão genérica
        break
    except: print ('ADVERTÊNCIA: Numero deve pertencer ao conjunto dos números naturais (N), ou seja, deve ser INTEIRO E NÃO NEGATIVO!')

print (primoVerifica(num))
