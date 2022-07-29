# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=400,height=400,cursor='dot',bd=0,bg='white',takefocus=1)
        self.cv1.focus_force()
        self.cv1.bind('<Button-1>',self.desenhar)

        self.cv1.create_rectangle(100,100,200,200,tag='caixa',fill='red',outline='')
        #self.cv1.create_text(150,150,text='CAIXA',anchor=CENTER)
        self.cv1.create_oval(200,200,300,300,tag='bola',fill='blue',outline='')
        #self.cv1.create_text(250, 250, text='BOLA', anchor=CENTER)

        self.cv1.pack()

        # FRAME
        self.fr1=Frame(toplevel)
        self.fr1.pack()
        self.lb=Label(self.fr1,text='LOCALIZAÇÃO ROOT POINTER',font=('bold','18'))
        self.lb.pack()

        self.obj=['caixa','bola']
    def desenhar(self,event):
        x_origem= self.cv1.winfo_rootx()
        y_origem= self.cv1.winfo_rooty()
        x_abs=self.cv1.winfo_pointerx()
        y_abs=self.cv1.winfo_pointery()
        obj=self.cv1.find_closest(x_abs-x_origem,y_abs-y_origem,halo=None,start=None)[0]
        print(obj)
        self.cv1.move(self.obj[obj-1],5,5)



painel=Tk()
pYpanel(painel)
painel.mainloop()
