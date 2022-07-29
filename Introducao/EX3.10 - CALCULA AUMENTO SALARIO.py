# TITULO: CALCULA AUMENTO SALARIO
# AUTOR: WALYSSON DOS REIS
# DATA: 25/09/2015

salario = float(input("DIGITE SALARIO: "))
aumento = float(input("DIGITE A PORCENTAGEM DE AUMENTO (%): "))

novosalario = salario+salario*(aumento/100)

print (" NOVO SALÁRIO: R$%.2f" %novosalario)
