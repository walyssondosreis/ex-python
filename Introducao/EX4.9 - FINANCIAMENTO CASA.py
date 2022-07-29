# TITULO: FINANCIAMENTO CASA
# AUTOR: WALYSSON DOS REIS
# DATA: 28/09/2015

valorcasa = float(input("DIGITE O VALOR DA CASA: R$"))
salario = float(input("DIGITE O SEU SALÁRIO:"))
anosdivida = int(input("DIGITE A QUANTIDADE DE ANOS QUE DESEJA PAGAR: "))
mensalidade = valorcasa/(anosdivida*12)
if mensalidade>salario*0.3:
     print ("VALOR DA CASA: \tR$%.2f" %valorcasa)
     print ("SALARIO:\tR$%.2f" %salario)
     print ("MENsALIDADE:\tR$%.2f EM %d MESES" %(mensalidade,anosdivida*12))
     print ("CREDITO:\tNÃO APROVADO")
     print ("\nMOTIVO: *** COMPROMETIMENTO DO SALÁRIO SUPERIOR À 30%")
else:
     print ("VALOR DA CASA: \tR$%.2f" %valorcasa)
     print ("SALARIO:\tR$%.2f" %salario)
     print ("MENsALIDADE:\tR$%.2f EM %d MESES" %(mensalidade,anosdivida*12))
     print ("CREDITO:\tAPROVADO")
