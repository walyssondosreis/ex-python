# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        # CANVAS 1
        self.cv1=Canvas(toplevel,width=400,height=400,cursor='dot',bd=0,bg='white')
        self.cv1.create_rectangle(0,0,200,200, fill='#%02x%02x%02x'%(255,200,255))
        #------------------------------------------------------
        print('NUMERO HEXA = ' ,hex(360))
        print('NUMERO HEXA = #%02x' %360)
        print(type(hex(360)))
        #------------------------------------------------------
        # '#%02x%02x%02x' é o parametro RGB hexadecimal de cores
        self.cv1.create_rectangle(200, 0, 400, 200, fill='#%02x%02x%02x'%(255,255,200))
        self.cv1.create_rectangle(0, 200, 200, 400, fill='#%02x%02x%02x'%(200,255,255))
        self.cv1.create_rectangle(200, 200, 400, 400, fill='#%02x%02x%02x'%(200,200,255))

        self.cv1.pack()

        # FRAME
        self.fr1=Frame(toplevel)
        self.fr1.pack()

        self.lb=Label(self.fr1,text='PythoN :CORES RGB',font=('bold','30'))
        self.lb.pack()


painel=Tk()
pYpanel(painel)
painel.mainloop()
