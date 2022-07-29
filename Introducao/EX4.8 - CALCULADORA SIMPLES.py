# TITULO: CALCULADORA SIMPLES
# AUTOR: WALYSSON DOS REIS
# DATA: 28/09/2015

numero1 = int(input("DIGITE PRIMEIRO NUMERO: "))
operacao = input("DIGITE O TIPO DE OPERAÇÃO ( * / + - ): ")
numero2 = int(input("DIGITE SEGUNDO NUMERO: "))
if operacao=='+' : print ("%d + %d = %d" %(numero1,numero2,numero1+numero2))
elif operacao=='-': print ("%d - %d = %d" %(numero1,numero2,numero1-numero2))
elif operacao=='*': print ("%d x %d = %d" %(numero1,numero2,numero1*numero2))
elif operacao=='/': print ("%d / %d = %.2f" %(numero1,numero2,numero1/numero2))
 
