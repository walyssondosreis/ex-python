# coding : utf-8

from tkinter import *

class Janela:
    def __init__(self,toplevel):

        self.fr1= Frame(toplevel)
        self.fr2= Frame(self.fr1)
        self.fr2.pack()
        self.fr1.pack() #PACK É O METODO QUE GERENCIA O LAYOUT, EXISTEM OUTROS COMO GRIDE

        self.frase = Label(self.fr1, text='PROGRAMA USANDO TKINTER')
        self.frase['font'] = ['Verdana', '16', 'italic', 'bold']
        self.frase.pack()

        self.botao3 = Button(self.fr2, text='BUTTON 3')
        self.botao3.pack()

        self.botao1= Button(self.fr2,text='BUTTON 1')
        self.botao1['background']='yellow'
        self.botao1['font']=('Verdana','12','italic','bold')
        self.botao1['width']=12
        self.botao1['height']=3
        self.botao1.pack()

        self.botao2= Button(self.fr2)
        self.botao2['background']='black'
        self.botao2['font']=['Times','16']
        self.botao2['text']='BUTTON 2'
        self.botao2['foreground']='yellow'
        self.botao2['width']=12
        self.botao2['height']=3
        self.botao2.pack()




raiz=Tk()
Janela(raiz)
raiz.mainloop()