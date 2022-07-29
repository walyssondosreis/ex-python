# TITULO: RADAR MULTA
# AUTOR: WALYSSON DOS REIS
# DATA: 26/09/2015

velocidade = float(input("VELOCIDADE DO CARRO (KM/H): "))
if velocidade>80: 
 print("VOCÊ ULTRAPASSOU A VELOCIDADE EM %.2f KM/H. MULTA DE R$%.2f " %(velocidade-80,(velocidade-80)*5))
