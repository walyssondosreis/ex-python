#coding: utf-8
# TITLE: EVENTOS DO MOUSE
# AUTHOR: WALYSSON DOS REIS

from tkinter import *

class Janela():
    def __init__(self,toplevel):
        self.fr1=Frame(toplevel)
        self.fr1.pack(side='top')

        self.fr2=Frame(toplevel)
        self.fr2.pack(side='bottom')

        self.titulof1=Label(self.fr1,text='EVENTO DUPLO',font=['Fixedsys','22','bold'],fg='yellow',bg='black')
        self.titulof1.pack()

        self.titulof2 = Label(self.fr2, text='PASSE O MOUSE', font=['Fixedsys', '22', 'bold'], fg='yellow',bg='black')
        self.titulof2.pack()

        self.bt1fr1=Button(self.fr1,text='MOUSE:LR',width='10')
        self.bt1fr1['font']=self.titulof1['font']
        self.bt1fr1['bg']='yellow'
        self.bt1fr1.bind(['<Button-1>','<Button-3>'],self.mudacor) # Metodo que gerencia a passagem dos Eventos
        #Uma tupla de eventos cria uma sequencia a ser seguida para que o metodo que ouvinte seja executado
        self.bt1fr1.pack(side='top')

        self.bt1fr2 = Button(self.fr2, text='OK', width='10')
        self.bt1fr2['font'] = self.titulof2['font']
        self.bt1fr2['bg']='green'
        self.bt1fr2.bind('<Leave>',self.mudacor2)
        self.bt1fr2.pack(side='top') # quando vazio pack assume side='top'

    def mudacor(self,event): # o arguimento event é obrigatorio
        if self.bt1fr1['bg']=='yellow':
            self.bt1fr1['bg']='SystemButtonFace'
            self.titulof1['text']="DON'T PANIC! :o"
        else:
            self.bt1fr1['bg']='yellow'
            self.titulof1['text']="EVENTO DUPLO"

    def mudacor2(self,event): # o arguimento event é obrigatorio
        if self.bt1fr2['bg']=='green':
            self.bt1fr2['bg']='SystemButtonFace'
            self.titulof2['text']="DON'T PANIC! :o"
            self.bt1fr2['text']='CANCEL'
        else:
            self.bt1fr2['bg']='green'
            self.titulof2['text']="PASSE O MOUSE"
            self.bt1fr2['text']='OK'

jtk=Tk()
#jtk2=Tk()
Janela(jtk)
#Janela(jtk2)
jtk.mainloop()
#jtk2.mainloop()