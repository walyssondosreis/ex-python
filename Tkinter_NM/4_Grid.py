# coding: utf-8
# TITLE: GRID Geometry Manager / LAYOUT MANAGEMENT
# AUTHOR: WALYSSON PEREIRA DOS REIS
# EMAIL: walyssondosreis@email.com
# TKINTER 8.5 REFERENCE A GUI FOR PYTHON : NEW MEXICO
# SECTION 14 (PG 5:9)

#! LEGENDA: #! SIGNICA NÃO DESOMENTAR

from tkinter import *

class App():
    def __init__(self,toplevel):

        #! FRAME

        self.fr1=Frame(toplevel)
        self.fr1.grid()
        self.fr2=Frame(self.fr1,bd=5)
        self.fr2.grid()
        # ---------------------------------------------------------------------------------------------------
        #! WIDGETS
        self.bt1=Button(self.fr1,text='BOTÃO 1',width=20,height=3,font=('Lucida','12','bold'),bg='white')
        self.bt1.grid(row=1,column=0,columnspan=2,sticky=EW) #! columnspan FAZ COM QUE UM WIDGET POSSA OCUPAR MAIS DE UMA COLUNA
        # ! O VALOR PADRÃO DA COLUNA (column) É 0 ASSIM COMO A LINHA (row)
        #! O sticky FAZ COM QUE O WIDGET POSSA OCUPAR DO ESPAÇO DISPONIVEL PARA ELE NA GRADE
        self.bt2 = Button(self.fr1, text='BOTÃO 2', width=20, height=3,font=('Lucida','12','bold'),bg='white')
        self.bt2.grid(row=0,ipadx=100,ipady=10,column=3,rowspan=2,sticky=NS) #! ipadx / ipady ALTERA O PREENCHIMENTO INTERNO DO WIDGET NA DIMENSÃO X E/OU Y
        #! O rowspan FAZ COM QUE UM WIDGET POSSA OCUPAR MAIS DE UMA LINHA
        self.bt3 = Button(self.fr1, text='BOTÃO 3', height=3,font=('Lucida','12','bold'),bg='white')
        self.bt3.grid(row=0,column=1,in_=self.fr2)
        self.bt4 = Button(self.fr1, text='BOTÃO 4', width=20, height=3,font=('Lucida','12','bold'),bg='white')
        self.bt4.grid(row=0,column=0,in_=self.fr2,sticky=N+S+E+W) #! O ATRIBUTO_in CRIA UM GRAU DE PARENTESCO ENTRE WIDGETS QUE POSSUEM O MESMO PAI (PARENT)

        #! METODOS DA GRID
        #---------------------------------------------------------------------------------------------------
        #cord=self.bt1.grid_bbox(0,0,1,1) #! RETORNA UMA TUPLA CONTENDO OS LIMITES DA GRADE DO WIDGET
        # ---------------------------------------------------------------------------------------------------
        #self.bt1.grid_forget()  #! DESAPARECE COM O WIDGET DO LAYOUT SÒ QUE QUANDO QUISER QUE ELE RETORNE USANDO grid()...
        #! ...ELE NÃO VOLTARÁ COM AS MESMAS CONFIGURAÇÕES DE GRID
        # ---------------------------------------------------------------------------------------------------
        #info = self.bt2.grid_info() #! RETORNA UM DICIONARIO COM TODAS AS CONF. DE ATRIBUTOS DO WIDGET PARA O GRID
        #print(info)
        # ---------------------------------------------------------------------------------------------------
        #loct=self.fr1.grid_location(50,60) #! RETORNA UMA TUPLA CONTENDO A COLUNA E LINHA A QUAL A COORDENADA PERTENCE NA GRADE
        #print(loct)
        # ---------------------------------------------------------------------------------------------------
        #self.bt3.grid_propagate(0) #! FORÇA UM WIDGET A TER UM TAMANHO EXATO NA GRADE
        # ---------------------------------------------------------------------------------------------------
        #self.bt1.grid_remove()  #! ASSIM COMO grid_forget RETIRA O WIDGET DA GRADE , COM A DIFERENÇA DE QUE AQUI AS OPçÕES ...
        #! DE GRID ANTERIORES SERÃO LEMBRAR CASO O WIDGET RETORNE COM O COMANDO grid()
        # ---------------------------------------------------------------------------------------------------
        #tupTotal=self.fr1.grid_size() #! RETORNA UMA TUPLA CONTENDO O NUMERO DE COLUNAS E O NUMERO DE LINHAS RESPECTIVAMENTE
        #print(tupTotal)
        # ---------------------------------------------------------------------------------------------------
        #listSlaves=self.fr1.grid_slaves() #! RETORNA UMA LISTA CONTENDO QUAIS OBJETOS EXISTEM NA GRADE DO WIDGET
        #! PODE-SE ESPECIFICAR UMA LINHA OU UMA COLUNA PARA EFETUAR A BUSCA POR WIDGETS.EX: row=2 or column=0
        #! DESSA FORMA VIRÀ APENAS ELEMENTOS DA LINHA OU DA COLUNA ESPECIFICADA
        #print(listSlaves)
        # ---------------------------------------------------------------------------------------------------
        # METODOS DO PARENT GRID
        self.fr1.columnconfigure(0,minsize=500) #! DEFINE UM TAMANHO MÍNIMO PARA A COLUNA DA GRADE PAI
        #! ... SENDO O PRIMEIRO ARGUMENTO O NUMERO DA COLUNA
        self.fr1.rowconfigure(0,minsize=100) #! DEFINE UM TAMANHO MÍNIMO PARA A LINHA DA GRADE PAI
        # ! ... SENDO O PRIMEIRO ARGUMENTO O NUMERO DA LINHA
        self.fr1.rowconfigure(0,pad=150) #! NUMERO DE PIXEL QUE SE DESEJA ADICIONAR PARA UMA LINHA
        self.fr1.columnconfigure(0, pad=150,weight=1)  #! NUMERO DE PIXEL QUE SE DESEJA ADICIONAR PARA UMA COLUNA
        self.fr1.columnconfigure(1,weight=3) #! CONFIGURA UMA RELAÇÃO DE ESPAÇO DA GRADE POR UM PESO (weight) NO WIDGET
        #! ... SENDO O PRIMEIRO ARGUMENTO O NUMERO DA COLUNA
        self.fr1.rowconfigure(0, weight=3)  #! CONFIGURA UMA RELAÇÃO DE ESPAÇO DA GRADE POR UM PESO (weight) NO WIDGET
        #! ... SENDO O PRIMEIRO ARGUMENTO O NUMERO DA LINHA
        toplevel.columnconfigure(0,weight=1) #! APLICA O MET GRID DIRETO NA JANELA PRICIPAL
        #! ISSO IRÁ CENTRALIZAR A JANELA AO MAXIMIZAR HORIZONTALMENTE, OU SEJA NAS COLUNAS
        toplevel.rowconfigure(0, weight=1)  # ! APLICA O MET GRID DIRETO NA JANELA PRICIPAL
        #! ISSO IRÁ CENTRALIZAR A JANELA AO MAXIMIZAR VERTICALMENTE, OU SEJA NAS LINHAS
        # ---------------------------------------------------------------------------------------------------




root=Tk()
App(root)
root.mainloop()
