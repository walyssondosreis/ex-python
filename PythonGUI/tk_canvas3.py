# coding: utf-8
# TITLE: PROGRAMA QUE DEMOSTRA O USO DE EVENTOS NO CANVAS
# AUTHOR: WALYSSON DOS REIS
from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=800,height=200,bd=0,bg='white',
                        takefocus=1,highlightthickness=2)
        # highlightthickness configura o tamanho da borda de seleção do focus objeto
        # takefocus faz com que o canvas seja tratado como widgets ou seja poderá ser alvo de eventos
        self.cv1X=float(self.cv1['width'])/4
        self.cv1Y = float(self.cv1['height'])/4
        #MESA
        #self.cv1.create_rectangle([100,150],[500,200],fill='brown',tag='mesa')
        self.cv1.create_polygon([0,4*self.cv1Y],
                                [0,3*self.cv1Y],
                                [2*self.cv1X,3*self.cv1Y],
                                [3*self.cv1X,4*self.cv1Y],fill='green4',tag='mesa')
        #BOLA
        self.cv1.create_oval([0, 2*self.cv1Y], [50, 3*self.cv1Y], fill='blue3', tag='bola') # SOBRE UMA MESMA TAG OS DOIS OBJETOS ESTARÂO SUJEITOS AOS MESMOS EVENTOS
        self.cv1.create_oval([0, 0.5 * self.cv1Y], [50, 1.5 * self.cv1Y], fill='red', tag='bola2')
        #EVENTOS
        self.cv1.focus_force()
        self.cv1.bind('<Right>', self.moverR)
        self.cv1.bind('<Left>', self.moverL)
        self.cv1.bind('<Up>', self.moverU)
        self.cv1.bind('<Down>', self.moverD)

        self.cv1.pack()

    def moverR(self,event):
        self.cv1.move('bola',5,0)
    def moverL(self,event):
        self.cv1.move('bola',-5,0)
    def moverU(self,event):
        self.cv1.move('bola',0,-5)
    def moverD(self,event):
        self.cv1.move('bola',0,5)


painel=Tk()
pYpanel(painel)
painel.mainloop()

