# coding: utf-8

from tkinter import *
from tkinter import  messagebox
from PIL import  Image,ImageTk

class pYpanel():
    topTk=''
    def __init__(self,toplevel):
        self.topTk=toplevel

        #toplevel.grid_rowconfigure(0, weight=1) # CENTRALIZA O GRID NAS LINHAS DA JANELA
        toplevel.grid_columnconfigure(0, weight=1) # CENTRALIZA O GRID NAS colunas DA JANELA

        # FRAMES
        self.fr1=Frame(toplevel,pady='60',padx='50')
        self.fr1.grid()
        self.fr2=Frame(toplevel,pady='400',padx='650')

        # METODOS DA JANELA (TOPLEVEL)
        toplevel.resizable(width=True,height=True) # MET. QUE DETERMINA QUAIS EIXOS PODEM SER REDIMENSIONADOS AO MAXIMIZAR
        #toplevel.maxsize(400,350) # METODO QUE DEFINE O TAMANHO MAX DA JANELA
        toplevel.minsize(400,350) # METODO QUE DEFINE O TAMANHO MIN DA JANELA
        toplevel.title('PROGRAMA LOGIN') # MET. QUE DEFINE O TITULO DA JANELA
       # toplevel.wm_attributes("-transparentcolor", "purple3",)
        toplevel.wm_attributes("-alpha",0.9) # regula o nivel de opacidade da janela 0 - 1

        # TRY EXCEPT É NESSARIO NOS DOIS CASOS ABAIXO POR QUE O MÓDULO cx_Freeze TRATA AS IMAGENS(ARQ)
        # ... INCORPORADAS AO PROGRAMA DE FORMA DIFERENTE, NÃO CRIANDO A PASTA DE IMAGENS NO PROGRAMA
        #... APENAS LENDO OS ARQUIVOS DIRETAMENTTE DA PASTA RAIZ
        try: toplevel.wm_iconbitmap("flag.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: toplevel.wm_iconbitmap(r".\images\flag.ico")  # TROCA ICONE DA JANELA PADRÃO TK

        #FRAME 1 ---------------------------------------------------------------------------------------
        try: self.pathIcoLogin =open("login.png",'rb')
        except: self.pathIcoLogin = open(r".\images\login.png",'rb')

        #ICONE DE LOGIN APLICADO A UM LABEL
        self.icoLogin = Image.open(self.pathIcoLogin).resize((150, 150), Image.ANTIALIAS)
        self.icoLogin = ImageTk.PhotoImage(self.icoLogin)
        self.labelLogin=Label(self.fr1,image=self.icoLogin)
        self.labelLogin.image=self.icoLogin
        self.labelLogin.grid(row=0,column=1,sticky=N+S+E+W)

        #CAMPO USUARIO
        self.tx1=Label(self.fr1,text='Usuario:',font=('Fixedsys','16'),fg='blue',pady='10')
        self.tx1.grid(row=1)
        self.entNome=Entry(self.fr1,width='30',font=('Arial','10')) # Entry É O objeto sem. jtexfield
        # NÃO É POSSIVEL DEFINIR O HEIDTH POIS NO ENTRY O MAX É O TAMANHO DA LINHA
        self.entNome['justify']='center' # Justifica o Texto Digitado
        self.entNome.focus_force()
        self.entNome.grid(row=1,column=1)

        #CAMPO SENHA
        self.tx2=Label(self.fr1,text='Senha:',font=('Fixedsys','16'),fg='blue',pady='10')
        self.tx2.grid(row=2)
        self.entPass=Entry(self.fr1,width='30',font=('Arial','10'),show='*',justify='center')
        self.entPass.bind('<Return>',self.entradaComEnter)
        self.entPass.grid(row=2,column=1)

        #BOTAO LOGIN
        self.btlogin=Button(self.fr1,text='Entrar',font=('Fixedsys','16'),pady='5',relief=GROOVE,highlightthickness=5)
        # highlightthickness determina a espeçura da borta de seleção, podendo ser aplicado a qualquer widget
        self.btlogin['command']=self.validalogin
        self.btlogin.bind('<Return>',self.entradaComEnter)
        self.btlogin.grid(row=3,column=1,sticky=EW) # OPÇÕES DO STICK: N S W E

        #self.bth=Button(self.fr1,text='BLA BLA BLA',font='22')
        #self.bth.grid(row=2,column=1,pady=20,padx=50)

        #FRAME 2 -------------------------------------------------------------------------------------
        self.msg = Label(self.fr2, text='ThAnK YoU!',font=('Fixedsys',40))
        self.msg.grid()
        self.btlogoff=Button(self.fr2,text='Deslogar',font=('Fixedsys','16'),pady='5',relief=GROOVE)
        self.btlogoff['command']=self.deslogar
        self.btlogoff.grid()

    def validalogin(self):
        if self.entNome.get()=='walyssondosreis' and self.entPass.get()=='123':
            self.fr1.grid_forget() # O Pack_FOrget Retira o Frame , diferente do destroy() que irá elimina-lo
            self.fr2.grid()
        else:
            messagebox.showwarning('Login Inválido','Por Favor, Digite Novamente Sua Credencial')
            self.entNome.delete(0, 'end')
            self.entPass.delete(0, 'end')
            self.entNome.focus_force()
    def entradaComEnter(self,event):
        self.validalogin()

    def deslogar(self):
        self.fr2.grid_forget()
        self.entNome.delete(0,'end')
        self.entPass.delete(0,'end')
        self.entNome.focus_force()
        self.fr1.grid()


painel=Tk()
pYpanel(painel)
painel.mainloop()

# MESSAGE BOX PYTHON 3
# https://www.tutorialspoint.com/python3/tk_messagebox.htm

# TK GRID
# https://www.tutorialspoint.com/python/tk_grid.htm
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/grid.html

# ATRUBUTOS E MET DO TK ()
# http://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window?rq=1
