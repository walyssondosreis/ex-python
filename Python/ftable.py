
from tkinter import *
from tkinter.ttk import *


class Table(Frame):


    def __init__(self, parent,width=100,height=20):
        self.parent=parent
        self.withTable=width
        self.heightTable=height
        Frame.__init__(self, parent)
        self.CreateUI() # METODO QUE IRÁ CRIAR A TABELA
        self.parameters={'lbimg':'','lbsinop':''}
    def pack_configure(self, cnf={}, **kw):
        self.grid(sticky=(N, S, W, E))
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['selectmode']='browse' # DEFINE O MODO DE SELEÇÃO DA TABELA: extended , browse, ou none
        tv['height']=self.heightTable # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA
        tv['padding']=5# DEFINE A BORDA INTERNA DA TABELA
        #tv['show']='tree' # OCULTA OS INDICES DA TABELA
        style=Style()
        #style.configure(".", font=('TkHeadingFont', 20,'italic'), foreground="white") # DEFINE STYLO PARA TODOS OS ELEMENTOS
        #style.configure("Treeview", foreground='black') # DEFINE STYLO PARA A TREEVIEW
        style.configure("Treeview.Heading", foreground='red',font=('System','12','bold')) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW



        tv['columns'] = ('tit','cat', 'clas', 'ano','res')
        tv.heading('#0', text='')
        tv.column('#0',width=0)
        tv.heading('tit', text='TITULO', anchor='center') #0
        tv.column('tit', anchor="center")
        tv.heading('cat', text='CATEGORIA')
        tv.column('cat', anchor='center', width=self.withTable)
        tv.heading('clas', text='CLASSIFICAÇÃO')
        tv.column('clas', anchor='center', width=self.withTable)
        tv.heading('ano', text='ANO')
        tv.column('ano', anchor='center', width=self.withTable)
        tv.heading('res',text='RESOLUÇÃO')
        tv.column('res',anchor='center', width=self.withTable)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)


    def InsertInTable(self, tit, cat='', clas='', ano='', res=''):
        #self.treeview.insert('','end',text='',values=('Titanic','DRAMA','12', '2000','720'))
         #self.treeview.insert('', 'end', text='', values=(tit,cat,clas, ano,res))
        self.treeview.insert('', 'end', text='', tags=('tit', 'cat','clas','ano','res'),values=(tit,cat,clas,ano,res))
        self.treeview.tag_configure('tit',background='white',font=('System','12'))
        #self.treeview.insert(k,'end',text='',values=('VALOR SUB LINHA')) # CRIA SUBLINHA
        #self.treeview.focus_force()
        self.treeview.tag_bind('tit','<1>',self.eventTableBt1)
        #self.treeview.tag_bind('tit', '<Up>', self.eventTableSeta)
        #self.treeview.tag_bind('tit', '<Return>', self.eventTablePlay)

    def eventTableBt1(self,event):
        #self.InsertInTable('EVENTO', 'MOUSE CLICK','BUTTON-1')
       # k=self.treeview.get_children()
       # print(self.treeview.item(k[0])['values'])
        self.parameters['lbimg']['text']='EVENTO 1000 GRAU!'
        self.parameters['lbimg']['font']=('Fixedsys','20')
        self.parameters['lbimg']['foreground']='red'
        self.parameters['lbimg']['text']= 'EVENTO <Button-1>'
        print('RODANDO O EVENTO')
        pass
    def eventTableSeta(self,event):
        self.InsertInTable('EVENTO', 'SETA DIRECIONAL','UP/DOWN')
        print('RODANDO O EVENTO')
    def eventTablePlay(self,event):
        self.InsertInTable('EVENTO', 'PLAY','RETURN')
        print('RODANDO O EVENTO')



#root = Tk()
#inserir=Table(root).InsertInTable
#Table(root).pack()
#inserir('FILME DO POSTGRESQL','COMEDIA','12','2001','210')

#root.mainloop()

# FONTE
# http://stackoverflow.com/questions/22456445/how-to-imitate-this-table-using-tkinter
# http://stackoverflow.com/questions/28685048/python-tkinter-treeview-iterating-get-children-output

# TREEVIEW
# http://www.tkdocs.com/tutorial/tree.html

# CONFIG INDICES TABELA
# http://stackoverflow.com/questions/32051780/how-to-edit-the-style-of-a-heading-in-treeview-python-ttk