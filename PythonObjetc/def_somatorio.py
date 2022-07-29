# coding: utf-8
# TITULO: FUNÇÃO DE SOMATORIO COM VERIFICAÇÃO
# Autor: Walysson dos Reis

def somatorio(*n):
    print (n)
    soma=0
    for i in n:
        try:i+0
        except:soma=None;break
        soma+=i
    return soma

result=somatorio(2,4,4.5,'CAVALINHO DE TROIA')
if(result!=None):print ('SOMATORIA = %.2f'%result)
else: print('Cara, Impossivel Somar Letras!')
