# TITULO: CALCULA SEGUNDOS
# AUTOR: WALYSSON DOS REIS
# DATA: 25/09/2015

dias = int(input("DIGITE O NÚMERO DE DIAS: "))
horas = float(input("DIGITE O NÚMERO DE HORAS: "))
minutos = float(input("DIGITE O NÚMERO DE MINUTOS: "))
segundos = float(input("DIGITE O NÚMERO DE SEGUNDOS: "))

totalsegundos = (segundos+(minutos*60)+(horas*3600)+(dias*86400))

print ("TOTAL DE SEGUNDOS: %.2f s" %totalsegundos)
