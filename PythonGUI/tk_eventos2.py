# coding: utf-8
# TITLE: EVENTOS DO TECLADO E CONF DE BOTÕES
# AUTHOR: WALYSSON DOS REIS

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):
        self.fr1=Frame(toplevel)
        self.fr1['padx'],self.fr1['pady']=100,100
        self.fr1.pack()

        self.ltt=Label(self.fr1,text='python')
        self.ltt['font']=['Fixedsys','30','underline']
        self.ltt.focus_force() # Passa o foco para o letreiro ltt
        self.ltt.bind('<Return>',self.keypressEnter)
        self.ltt.bind('<Double-Button-1>', self.keypressEnter) # A forma KeyPress-ALPHA serve para chamar qualquer letra
        # Existem os modificadores Double e Triple que faz com que o evento se repita para ser aceito
        self.ltt['padx'],self.ltt['pady']=200,0
        self.ltt['relief'],self.ltt['fg']=RIDGE,'red'
        self.ltt.pack()

        self.bt1=Button(self.fr1,text='OK')
        self.bt1['padx'],self.bt1['pady']=200,0 # ALTERA TAMANHO DO BOTÃO EM RELAÇÃO AO TEXTO DO MESMO
        self.bt1['font']=['Fixedsys','30','bold']
        self.bt1['relief']=GROOVE  # DEFINE O ESTILO/RELEVO DA BORDA DO BOTÃO : PODENDO SER GROOVE, RIDGE ou FLAT
        self.bt1['command']=self.buttonEvent # METODO BINDING QUE ATRAVÉS DO COMMAND USA DIRETAMENTE O EVENTO DO MOUSE CLICK
        self.bt1.pack()

    def keypressEnter(self,event):
        if not self.ltt['text'].isupper(): self.ltt['text']=self.ltt['text'].upper()
        else: self.ltt['text']=self.ltt['text'].lower()
    def buttonEvent(self): # COMO O EVENTO É CHAMADO POR BINDING DO COMMAND NÃO É ACEITO A VAR event
        if(self.bt1['text']=='OK'): self.bt1['text']='VaLeW!'
        else: self.bt1['text']='OK'



win=Tk()
pYpanel(win)
win.mainloop()


'''
MAPA DE ALGUNS EVENTOS DO TECLADO
----------------------------------
    EVENTO        |    STRING
----------------------------------
ENTER             | '<Return>'
DELETE            | '<Delete>'
BackSpace         | '<BackSpace>'
ESC               | '<Escape>'
Seta Direita      | '<Right>'
Seta Esquerda     | '<Left>'
Seta Cima         | '<Up>'
Seta Baixo        | '<Down>'
O widget com Foco | '<FocusIn>'
O widget sem Foco | '<FocusOut>'
-----------------------------------

-----------------------------------------------------------------------
MODIFICADORES
-----------------------------------------------------------------------
<Double-KeyPress-x>  # Exige Duas Confirmações na Entrada
<Triple-Button-1>  #Exige Três Confirmações na Entrada
<Any-KeyPress>  # Aceita qualquer Tecla Como Alvo do Evento
<Any-Button>   # Aceita qualquer clique do Mouse como Alvo do Evento
'''

#Eventos Binding Python:
# http: // effbot.org / tkinterbook / tkinter - events - and -bindings.htm