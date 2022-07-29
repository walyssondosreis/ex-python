# TITULO: CALCULA AUMENTO SALARIO CONDICIONAL
# AUTOR: WALYSSON DOS REIS
# DATA : 26/09/2015

salario = float(input("DIGITE SALÁRIO: "))

if salario>1250.00 :
    print ("NOVO SALARIO: R$%.2f" %(salario+salario*0.1))
if salario<=1250.00 :
    print ("NOVO SALARIO: R$%.2f" %(salario+salario*0.15))
