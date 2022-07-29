# coding: utf-8

from tkinter import *
from PIL import  ImageTk, Image
# PIL ESTA MORTO, TIVE QUE ISTALAR O PILLOW QUE ABRANGE O PIL: pip3 install pillow



class pYpanel:
    def __init__(self,toplevel):
        self.fr1=Frame(toplevel,pady='50',padx='50')
        self.fr1.pack()
        self.path='.\images\logofemc.jpg'

        self.img=Image.open(self.path)
        self.img= self.img.resize((300,100),Image.ANTIALIAS) # O PARAMETRO Image.ANTIALIAS FAZ COM QUE SEJA PRESERVADA A QUALIDADE DA IMAGEM
        self.img=ImageTk.PhotoImage(self.img)
        toplevel.tk.call('wm', 'iconphoto', toplevel._w, self.img)

        self.iconUser=Label(self.fr1,image=self.img)
        self.iconUser.image=self.img # SEM ESTA LINHA IMAGEM NÃO È MOSTRADA
        self.iconUser.pack()


painel=Tk()
pYpanel(painel)
painel.mainloop()

# FONTE
# IMAGEM EM TKINTER
# http://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter-python-2-7