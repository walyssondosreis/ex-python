# coding: utf-8
# TITLE: ListBox Widget
# AUTHOR: WALYSSON PEREIRA DOS REIS
# EMAIL: walyssondosreis@email.com
# TKINTER 8.5 REFERENCE A GUI FOR PYTHON : NEW MEXICO
# SECTION 14 (PG 52:56)

#! LEGENDA: #! SIGNICA NÃO DESOMENTAR

from tkinter import *
from tkinter.ttk import *

class app:
    def __init__(self,toplevel):
        self.fr1=Frame(toplevel)
        self.fr1.pack()

        #---------------------------------------------------------------------------------------------

        # SCROLLS PARA LISTBOX
        self.yScroll=Scrollbar(self.fr1,orient=VERTICAL) # DEFINE O SCROLL VERTICAL
        self.yScroll.grid(row=0,column=2,sticky=N+S)
        self.xScroll = Scrollbar(self.fr1, orient=HORIZONTAL)  # DEFINE O SCROLL HORIZONTAL
        self.xScroll.grid(row=2, column=1, sticky=E+W)

        #---------------------------------------------------------------------------------------------

        #!LISTBOX
        self.listbox=Listbox(self.fr1)
        self.listbox['activestyle']='none' #! ESTILO DE SELEÇÃO: 'underline' (PADRÃO), 'dotbox','none'
        self.listbox['width']=40 #! DEFINE A LARGURA DA LINHA EM CARACTERES (NÃO PIXELS!)
        self.listbox['height']=4 #! DEFINE A QUANTIDADE DE LINHAS DA LISTA (NÃO PIXELS!)
        self.listbox['listvariable']=StringVar(value=('BRAZIL BRAZIL BRAZIL BRAZIL BRAZIL BRAZIL BRAZIL : WALYSSON','USA USA USA USA USA : GERALD','JAPAN: TAKOY','CHINA: YU','FRANCE: GIROUD'))
        self.listbox['background']='yellow' #! ou ['bg']
        self.listbox['foreground']='blue' #! ou {'fg'}
        self.listbox['borderwidth']=0 #! ou ['bd']
        self.listbox['cursor']='dotbox' #! DEFINE O ESTILO DO CURSOR DO MOUSE SOBRE A LISTA
        self.listbox['disabledforeground']='white'
        self.listbox['exportselection']=1 #! DESABILITA OU NÃO A OPÇÃO COPIAR PARA VALORES SELECIONADOS
        self.listbox['font']=('Fixedsys','22')
        self.listbox['justify']=CENTER
        self.listbox['highlightbackground']='red' #! DEFINE A COR DA BORDA DO WIDGET QUANDO NÃO ESTIVER EM FOCO
        self.listbox['highlightcolor']='green' #! DEFINE A COR DA BORDA DO WIDGET QUANDO ESTIVER EM FOCO
        self.listbox['highlightthickness']=5 #! DEFINE A ESPESSURA DO FOCUS  HIGH LIGHT EM PIXELS
        self.listbox['relief']=GROOVE #! DEFINE O ESTILO 3D DE BORDA LISTA
        self.listbox['selectbackground']='white' #! DEFINE A COR DE FUNDO DO SELETOR DE LINHAS
        self.listbox['selectforeground']='blue4'#! DEFINE A COR DO TEXTO DO SELETOR DE LINHAS
        self.listbox['selectborderwidth']=10 #! DEFINE A LARGURA DA BORDA DO SELETOR EM PIXELS
        self.listbox['selectmode']=EXTENDED #! DEFINE O MODO DE SELÇÃO DOS ITENS, COMO SÃO SELECIONADOS
        #! listbox['selectmode'] = BROWSE or SINGLE or MULTIPLE or EXTENDED
        self.listbox['state']=NORMAL #! FAZ COM QUE A LISTA RESPONDA OU NAO A EVENTOS DO MOUSE (EVENTOS unresponsive)
        #! listbox['state'] = NORMAL or DISABLED
        #self.listbox['xscrollcommand']=self.xScroll.set # DEFINE A BARRA DE ROLAGEM HORIZONTAL PARA A TABELA
        #self.listbox['yscrollcommand']=self.yScroll.set # DEFINE A BARRA DE ROLAGEM VERTICAL PARA A TABELA
        #self.listbox['takefocus']=True #
        self.listbox.grid(row=0,column=1,sticky=N+S+E+W)
        self.listbox.bind('<1>',self.eventList)

        # ---------------------------------------------------------------------------------------------
        self.listbox.xview_moveto(0.13) #! POSICIONA O SCROLL X MAIS A DIREITA POR UMA FRAÇÃO NO CONJ.[0,1]
        self.listbox.yview_moveto(0.0) #! POSICIONA O SCROLL Y MAIS PARA BAIXO POR UMA FRAÇÃO NO CONJ.[0,1]
        self.listbox.xview_scroll(1,PAGES) #! DIZ COMO SERÁ A ROLAGEM NO SCROLL DA LISTA EIXO x
        self.listbox.yview_scroll(1, UNITS) #! DIZ COMO SERÁ A ROLAGEM NO SCROLL DA LISTA EIXO Y
        #! O PRIMEIRO ARGUMENTO É O QUANTIDADE DE SALTOS, O SEGUNDO É O TIPO DE SALTO
        #! PODENDO SER UNITS or PAGES
        #---------------------------------------------------------------------------------------------
        #! BINDING DOS SCROOLS
        self.yScroll['command'] = self.listbox.yview # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        #! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.listbox.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        # ---------------------------------------------------------------------------------------------
        #self.listbox.focus_force()


    def eventList(self,event):
        # ---------------------------------------------------------------------------------------------
        #self.listbox.activate(0)  #! SELECIONA A LINHA ESPECIFICADA PELO INDICE DADO
        #! listbox.activate(ACTIVE or END or 'NumberLine')
        # ---------------------------------------------------------------------------------------------
        #bbox = self.listbox.bbox(ACTIVE)  #! RETORNA O PONTO NA CAIXA DE TEXTO DA LINHA SW (SUPERIOR ESQUERDO)...
        #! ... COMO TAMBÉM A LARGURA E ALTURA DA CAIXA DE TEXTO. TUPLA: (xoffset,yoffset,width,height)
        # ---------------------------------------------------------------------------------------------
        #cslt=self.listbox.curselection() #! RETORNA UMA TUPLA COM O NUMERO DA LINHA(s) SELECIONADA
        # ---------------------------------------------------------------------------------------------
        #self.listbox.delete(1,END) #! APAGA ELEMENTOS DA LISTA, OMITINDO-SE O SEG.PARAMETRO IRÁ APAGAR APENAS UM ITEM
        # ---------------------------------------------------------------------------------------------
        #gt=self.listbox.get(0,END) #! RETORNA UMA TUPLA CONTENDO OS VALORES DAS LINHAS DESEJADAS
        # ---------------------------------------------------------------------------------------------
        #self.listbox.index(5) #
        # ---------------------------------------------------------------------------------------------
        #self.listbox.insert(0,'ITALY') #! INSERE NOVA(S) LINHA NA LISTBOX, SEMPRE ANTES DO PRIM. ARG
        # ---------------------------------------------------------------------------------------------
        #iconf=self.listbox.itemconfig(2,foreground='red') #! MUDA UM ATRIBUTO DA LINHA PELO INDICE FORNECIDO
        #iget=self.listbox.itemcget(2,'foreground') #! RECUPERA UM ATRIBUTO DA LINHA PELO INDICE FORNECIDO
        #! ATRIBUTOS PODEM SER: 'foreground' or 'background' or 'selectbackground' or 'selectforeground'
        # ---------------------------------------------------------------------------------------------
        #nres=self.listbox.nearest(2) #! RETORNA O INDICE DA LINHA MAIS PROXIMA EM RELAÇÃO A COORDENA Y(DO WIDGET LIST) PASSADA
        # ---------------------------------------------------------------------------------------------
        #! DEFINE UMA ROLAGEM APARTIR DE UM EVENTO, OU SEJA O DESLOCAMENTO VISUAL DA LISTA DE UM PONTO A OUTRO
        #pc = self.listbox.scan_mark(40,0) #! POSIÇÃO REFERENCIA
        #px = self.listbox.scan_dragto(40, 40)  #! POSIÇÃO CORRENTE DO EVENTO
        # ---------------------------------------------------------------------------------------------
        #self.listbox.see(4) #! AJUSTA A POSIÇÃO DO LISTBOX PARA QUE A LINHA DO INDICE PASSADO SEJA VISIVEL
        # ---------------------------------------------------------------------------------------------
        #self.listbox.selection_anchor(1) #! IRÁ DEFINIR UMA ANCORA DE SELEÇÃO PARA O SELETOR
        #self.listbox.selection_set(ANCHOR,3) #! IRÁ SELECIONAR OS ITENS DA ANCORA DEFINIDA ATÉ A LINHA DESEJADA
        #! QUANDO CLICADO EM ALGUM ELEMENTO DA LISTA ESTE SERÁ O NOVO ANCORA
        # ---------------------------------------------------------------------------------------------
        #self.listbox.selection_clear(0,1) #! REMOVE O SELETOR DA(s) LINHA(s) ESPECIFICADA
        # ---------------------------------------------------------------------------------------------
        #slt=self.listbox.select_includes(2) #! RETORNA UM BOLEANO CASO O INDICE INFORMADO ESTEJA NA SELEÇÃO
        #print(slt)
        # ---------------------------------------------------------------------------------------------
        #self.listbox.select_set(0,END) #! SELECIONA TODAS AS LINHAS ENTRE UM INTERVALO
        # ---------------------------------------------------------------------------------------------
        #nlinhas=self.listbox.size() #! RETORNA O NUMERO DE LINHAS DO LISTBOX
        #print(nlinhas)
        # ---------------------------------------------------------------------------------------------
        pass


root=Tk()
app(root)
root.mainloop()
