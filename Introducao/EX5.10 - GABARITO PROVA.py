# TITULO: GABARITO PROVA
# AUTOR: WALYSSON DOS REIS
# DATA: 28/09/15

pontos = 0
questao = 1


while questao<=3:
        resposta = input("QUESTÃO %d: " %questao)
        if questao == 1 and (resposta=="b" or resposta=="B"):pontos = pontos+1
        if questao == 2 and (resposta=="a" or resposta=="A"):pontos = pontos+1
        if questao == 3 and (resposta=="d" or resposta=="D"):pontos = pontos+1
        questao+=1

print ("PONTOS DO ALUNO: %d" %pontos)
