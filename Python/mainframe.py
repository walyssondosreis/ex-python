# coding: utf-8

from tkinter import *
from ftable import *

class pyapk:
    def __init__(self,toplevel):

        # JANELA CONFIG
        #toplevel.grid_rowconfigure(0, weight=1)  # CENTRALIZA O GRID NAS LINHAS DA JANELA
        toplevel.grid_columnconfigure(0, weight=1)  # CENTRALIZA O GRID NAS COLUNAS DA JANELA

        # FRAMES ///////////////////////////////////////////////////////////////////////////
        #-----------------------------------------------------------------------------------
        self.mainFrame=Frame(toplevel)
        self.mainFrame.grid() #sticky=(N,S,E,W)
        # -----------------------------------------------------------------------------------
        self.table=Table(self.mainFrame,width=300,height=10)# FRAME DE TABELA QUE EU CRIEI
        #self.table.focus_force()
        self.table.grid()
        # -----------------------------------------------------------------------------------
        self.fr2=Frame(self.mainFrame)
        self.fr2.grid()
        # -----------------------------------------------------------------------------------

        #WIDGETS/////////////////////////////////////////////////////////////////////////////
        # -----------------------------------------------------------------------------------
        self.labelSinopse=Label(self.fr2,text=' TITULO AQUI! ')
        #self.labelSinopse.grid(row=0,column=1,padx=50,pady=50)
        # -----------------------------------------------------------------------------------
        self.labelCapa = Label(self.fr2, text=' CATEGORIA AQUI! ')
        self.labelCapa.grid(row=0,column=2,padx=50,pady=50)
        # -----------------------------------------------------------------------------------
        self.bt2=Button(self.fr2,text='OK')
        self.bt2.grid(row=1,columnspan=3)

        # -----------------------------------------------------------------------------------
        for i in range(7):
            self.table.InsertInTable('filme%d'%i, 'category', '12', '2017', '1080')
        # MANDA OS LABELS PARA OS EVENTOS
        self.table.parameters['lbimg']=self.labelCapa # PASSA LABEL DA CAPA PARA PREENCHER
        self.table.parameters['lbsinop']=self.labelSinopse # PASSA LABEL DA SINOPSE PARA PREENCHER

        # -----------------------------------------------------------------------------------
    def chamada(self,event):
        print('A CHAMADA É ESSA')


program=Tk()
pyapk(program)
program.mainloop()

# http://www.tkdocs.com/tutorial/tree.html
# http://stackoverflow.com/questions/36120426/tkinter-treeview-widget-inserting-data
# https://www.google.com.br/search?q=tk+treeview&oq=tk+tree&aqs=chrome.1.69i57j0l5.3863j0j7&sourceid=chrome&ie=UTF-8
#