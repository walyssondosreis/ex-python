# TITULO: EQUAÇÃO DO SEGUNDO GRAU
# AUTOR: WALYSSON DOS REIS
# DATA: 29/09/2015

from math import sqrt

#APRESENTAÇÃO DO PROGRAMA
print ("%s\n\t\t\t\tEQUAÇÃO DO 2º\n%s" %('-'*80,'-'*80))

#ENTRADA DE DADOS
a=float(input("DIGITE A:"))
b=float(input("DIGITE B:"))
c=float(input("DIGITE C:"))

#CÁLCULO DO DELTA
delta=(b**2)-4*a*c

#CALCULO DAS RAIZES
if delta < 0: print ("NÃO EXISTEM RAIZES PERTENCENTES AO CONJUNTO DOS NÙMEROS REAIS")
if delta > 0:
     x1=(-b+sqrt(delta))/2*a
     x2=(-b-sqrt(delta))/2*a
     print ("\nDELTA \t= %.2f" %delta)
     if delta==0:
          print ("X \t= %.2f" %x1)
     else:
          print ("X1 \t= %.2f" %x1)
          print ("X2 \t= %.2f" %x2)
