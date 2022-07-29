# coding: utf-8
# TITLE: A Minimal Application
# AUTHOR: WALYSSON PEREIRA DOS REIS
# EMAIL: walyssondosreis@email.com
# TKINTER 8.5 REFERENCE A GUI FOR PYTHON : NEW MEXICO
# SECTION 2 (PG 4:9)

import tkinter as tk # o 'as' cria um alias para o módulo logo na importação

class Application(tk.Frame):
    # 'tkinter' é módulo onde contem varias classes
    #  'Frame' é uma classe dentro de 'tkinter'
    def __init__(self,master=None): # NONE SIGNICA QUE ESTA INSTANCIA TK SERÁ A TOPLEVEL
        tk.Frame.__init__(self,master) # Chama o met. construtor da classe pai 'Frame'
        self.grid()
        self.createWidgets()
        self.__imprimir() # Usando metodo privado
    def createWidgets(self):
        self.quitButton=tk.Button(self,text='Quit',command=self.quit)
        self.quitButton.grid()
        # WIDGET QUE EQUIVALE AO RICHTEXTBOX
        self.tx=tk.Text(self,width=50,height=4) #! height em linhas, width em pixels
        self.tx.grid()
        top=self.winfo_toplevel() # METODO CAPTURA A JANELA TOPLEVEL INSTANCIADA
        top.columnconfigure(0,weight=1)
        top.rowconfigure(0,weight=1)


    def __imprimir(self): # O underline duplo no inicio do nome do metodo faz com que este seja privado
        print('ESTE METODO PERTENCE A CLASSE APPLICATION!')
app=Application()
app.master.title('Sample application')
app.mainloop()

