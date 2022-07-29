# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=200,height=200,bd=0,bg='SystemButtonFace')
        self.cv1.create_arc(50,50,150,150,start=0,extent=60,fill='yellow',outline='black',style=PIESLICE)
        # o atributo style pode ser: PIESLICE (padrão) ARC ou CHORD
        self.cv1.create_arc(50, 50, 150, 150, start=60, extent=60, fill='black', outline='black')
        self.cv1.create_arc(50, 50, 150, 150, start=120, extent=60, fill='yellow', outline='black')
        self.cv1.create_arc(50, 50, 150, 150, start=180, extent=60, fill='black', outline='black')
        self.cv1.create_arc(50, 50, 150, 150, start=240, extent=60, fill='yellow', outline='black')
        self.cv1.create_arc(50, 50, 150, 150, start=300, extent=60, fill='black', outline='black')
        # Da mesma forma que no arco é defido o centro apartir de um retângulo para as primeiras coordenadas
        # start é o atributo que indica a quantos graus se iniciará o arco
        # extent é o atributo que indica a quantos a mais graus cessará o arco
        self.cv1.pack()

        # FRAME
        self.fr1=Frame(toplevel)
        self.fr1.pack()

        # CANVAS 2
        self.cv2 = Canvas(toplevel, width=200, height=200, bg='white')
        self.cv2.create_oval(50,50,150,150,fill='red')

        self.cv2.pack()

        self.lb=Label(self.fr1,text='ARC and OVAL',font=('Fixedsys','20','bold'))
        self.lb.pack()


painel=Tk()
pYpanel(painel)
painel.mainloop()

