# coding: utf-8
# Título: Função(def) Verificadora de Números Primos
# Autor: Walysson dos Reis

def primoVerifica(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
        elif (i == num - 1):
            return True
    if (num == 0 or num == 1): return False
    if (num == 2): return True

cont=0

print ('\nNUMEROS PRIMOS :\n\n{ '),
for i in range(2,100):
    if (primoVerifica(i)):
        print ('[%d]' %i),
        cont+=1
        if(cont==10):
            print ('\n')
            cont=0
print(' }')

