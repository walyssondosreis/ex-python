# coding: utf-8
# TITULO: Verificação se Um Número é Perfeito
# Autor: Walysson dos Reis

for num in range(1,8300):

    soma=0
    for divisor in range(1,num): #Como eu limitei a faixa range o divisor começara do 1
        if(num%divisor == 0): soma+=divisor
        #print('%d resto %d = %d' %(num,divisor,(num%divisor)))
        if(soma == num and divisor==(num-1)):
            print('PERFEITO! :) [ Num: %d] [ Som: %d]\n' %(num,soma));break