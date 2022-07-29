# TITULO: IMPRIME MAIOR E MENOR NUMERO
# AUTOR: WALYSSON DOS REIS
# DATA: 26/09/2015

num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
num3 = int(input("DIGITE O TERCEIRO NÚMERO: "))

if num1>num2:
     if num1>num3:
          print ("O PRIMEIRO NUMERO É O MAIOR: %d" %num1)
          if num2>num3: print ("O TERCEIRO NUMERO É O MENOR: %d" %num3)
          else: print("O SEGUNDO NUMERO É O MENOR: %d" %num2)
if num2>num1:
     if num2>num3:
          print ("O SEGUNDO NUMERO É O MAIOR: %d" %num2)
          if num1>num3: print ("O TERCEIRO NUMERO É O MENOR: %d" %num3)
          else: print("O PRIMEIRO NUMERO É O MENOR: %d" %num1)

if num3>num1:
     if num3>num2:
          print ("O TERCEIRO NÚMERO É O MAIOR: %d" %num3)
          if num1>num2: print ("O SEGUNDO NUMERO É O MENOR: %d" %num2)
          else: print("O PRIMEIRO NUMERO É O MENOR: %d" %num1)
