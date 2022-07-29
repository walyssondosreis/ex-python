# TITULO: CALCULA DESCONTO PRODUTO
# AUTOR: WALYSSON DOS REIS
# DATA: 25/09/2015

produto = float(input("DIGITE O VALOR DO PRODUTO: "))
desconto = int(input("DIGITE O PERCENTUAL DE DESCONTO (%): "))
novopreco = produto - produto*(desconto/100)
print ("PRODUTO SEM DESCONTO: R$%.2f" %produto)
print ("PRODUTO COM DESCONTO: R$%.2f" %novopreco)
