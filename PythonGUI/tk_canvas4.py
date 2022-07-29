# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=400,height=400,cursor='dot',bd=0,bg='white',takefocus=1)
        self.cv1.focus_force()
        self.cv1.bind('<Button-1>',self.desenhar)

        self.cv1.pack()

        # FRAME
        self.fr1=Frame(toplevel)
        self.fr1.pack()

        self.lb=Label(self.fr1,text='LOCALIZAÇÃO ROOT POINTER',font=('bold','18'))
        self.lb.pack()

    def desenhar(self,event):
        x_origem= self.cv1.winfo_rootx()
        y_origem= self.cv1.winfo_rooty()
        x_abs=self.cv1.winfo_pointerx()
        y_abs=self.cv1.winfo_pointery()
        try:
            p=(x_abs-x_origem,y_abs-y_origem)
            self.cv1.create_line(self.ultimo_p,p)
            self.ultimo_p=p
        except:
            self.ultimo_p=(x_abs-x_origem,y_abs-y_origem)


painel=Tk()
pYpanel(painel)
painel.mainloop()
