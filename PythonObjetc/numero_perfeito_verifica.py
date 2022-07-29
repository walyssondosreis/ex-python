# coding: utf-8
# TITULO: Verificação se Um Número é Perfeito
# Autor: Walysson dos Reis

while 1:
    try:
        num=int(input('Por Favor Digite um Número: '))
        break
    except: print('Cara, Realmente  tem que ser um NÚMERO!')

soma=0

if(num>1):
    for divisor in range(1,num): #Como eu limitei a faixa range o divisor começara do 1
        if(num%divisor == 0): soma+=divisor
        if(soma == num): print('Número É perfeito! :) [ Num: %d] [ Som: %d]' %(num,soma));exit(0)

print('Número NÃO é perfeito! :( [ Num: %d] [ Som: %d]' %(num,soma))