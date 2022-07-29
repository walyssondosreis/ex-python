# TITULO: CONTA DE ENERGIA ELETRICA
# AUTOR: WALYSSON DOS REIS
# DATA: 28/09/2015

consumo = float(input("DIGITE O VALOR CONSUMIDO (KW/H): "))
tipo = input("\nR:RESIDENCIA\nC:COMERCIO\nI:INDUSTRIA\n\nDIGITE O TIPO DE INSTALAÇÃO: ")
if tipo=="r":
	if consumo <=500: print ("VALOR A PAGAR: R$%.2f" %(consumo*0.4))
	elif consumo>500: print ("VALOR A PAGAR: R$%.2f" %(500*0.4)+(consumo-500)*0.65)
if tipo=="c":
	if consumo <=1000: print ("VALOR A PAGAR: R$%.2f" %(consumo*0.55))
	elif consumo>500: print ("VALOR A PAGAR: R$%.2f" %(1000*0.55)+(consumo-1000)*0.60)
if tipo=="i":
	if consumo <=5000: print ("VALOR A PAGAR: R$%.2f" %(consumo*0.55))
	elif consumo>500: print ("VALOR A PAGAR: R$%.2f" %(5000*0.55)+(consumo-5000)*0.60)



