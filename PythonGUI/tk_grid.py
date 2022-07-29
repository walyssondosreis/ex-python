# coding: utf-8

from tkinter import *

class pYpanel:
    janela=''
    def __init__(self,toplevel):
        self.janela=toplevel
        toplevel.minsize(100,100)
        # FRAME
        self.fr1=Frame(toplevel,padx=100,pady=100)
        self.fr1.pack()
        #widgets
        self.bt1= Button(self.fr1,text='BOTÃO 1',width=20,height=2)
        self.bt1.grid(row=1,column=1)
        self.bt2 = Button(self.fr1, text='BOTÃO 2',width=20,height=2)
        self.bt2.grid(row=1, column=2)
        self.bt3 = Button(self.fr1, text='BOTÃO 3',width=20,height=2)
        self.bt3.grid(row=2, columnspan=3)
        self.bt4 = Button(self.fr1, text='ENCERRAR', width=20, height=2)
        self.bt4.grid(row=4, columnspan=3)
        self.bt4['command']=self.fechar

        # o rowspan e columnspan faz com que o widget seja intercalado entre as linhas ou colunas
        self.bt3.grid_forget() # SOME COM O WIDGET DA TELA
        self.bt2.destroy() # simplesmente destroy o widget tendo que reconstruilo caso necessecite dele

    def fechar(self): # METODO QUE IRA ENCERRAR O PROGRAMA
        self.janela.destroy()

painel=Tk()
pYpanel(painel)
painel.mainloop()
