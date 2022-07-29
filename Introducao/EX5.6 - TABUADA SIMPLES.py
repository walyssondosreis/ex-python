# TITULO: TABUADA SIMPLES
# AUTOR: WALYSSON DOS REIS
# DATA: 28/09/2015

numero = int(input("DESEJA A TABUADA DE QUAL NÚMERO? "))
conta=1;
while conta<=10:
	print("%2.d  * %2.d = %2.d" %(conta,numero,conta*numero))
	conta=conta+1
