# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=400,height=400,cursor='dot',bd=0,bg='blue')
        self.cv1.create_rectangle(10,10,390,390, fill='black')
        self.cv1.create_text(200,200,text=' P Y T H O N \n (N | E) ',
                             font=('Impact','30'),justify='center',fill='yellow',anchor=NE)
        self.cv1.create_text(200, 200, text=' P Y T H O N \n (S | W) ',
                             font=('Impact', '30'), justify='center', fill='yellow', anchor=SW)
        self.cv1.create_text(200, 200, text=' P Y T H O N \n (S | E) ',
                             font=('Impact', '30'), justify='center', fill='yellow', anchor=SE)
        self.cv1.create_text(200, 200, text=' P Y T H O N \n (N | W) ',
                             font=('Impact', '30'), justify='center', fill='yellow', anchor=NW)
        # bg não é aceito para definições de obj canvas, usa-se então fill
        # anchor é a posição do texto em relação a cordenada, CENTER já é o padrão
        self.cv1.pack()

        # FRAME
        self.fr1=Frame(toplevel)
        self.fr1.pack()

        # CANVAS 2
        self.cv2 = Canvas(toplevel, width=400, height=300, cursor='dotbox', bg='white')
        self.cv2.create_line(0,0,self.cv2['width'],self.cv2['height'],fill='red',width=20) # create_line DESENHA UMA LINA
        self.cv2.create_line(self.cv2['width'],0,0,self.cv2['height'],fill='red',width=20)
        self.ycv2=float(self.cv2['height'])/2 # Define coordenada Y
        self.xcv2 = float(self.cv2['width']) / 2 # Define coordenada X
        self.cv2.create_line(0,self.ycv2,self.cv2['width'],self.ycv2,fill='blue',width=20)
        self.cv2.create_line(self.xcv2,0, self.xcv2,self.cv2['height'],fill='blue',width=20)
        self.cv2.pack()

        self.lb=Label(self.fr1,text='PythoN : CANVAS',font=('bold','30'))
        self.lb.pack()


painel=Tk()
pYpanel(painel)
painel.mainloop()

# ALGUNS VALORES PARA CURSOR : X_cursor ,dot , circle, dotbox, fleur, target
# bd especifica a espessura da borda do widget/canvas

# MACETE PARA COORDENADA DO CANVAS:
# (X , ALTURA - Y) FORMA CARTESIANA QUE CORRESPONDE AO ( X, Y) DO CANVAS

#FONTE :
# TK CURSORS
# https://www.tutorialspoint.com/python/tk_cursors.htm

# TK COLORS LIST
# http://wiki.tcl.tk/37701