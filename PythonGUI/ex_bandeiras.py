# coding: utf-8

from tkinter import *

class pYpanel:
    def __init__(self,toplevel):

        toplevel.title('NATIONAL FLAGS')

        #toplevel.wm_iconbitmap(".\\images\\flag.ico")  # TROCA ICONE DA JANELA TK
        #toplevel.tk.call('wm','iconbitmap',toplevel._w,'-default','.\\images\\flag.ico') # SEGUNDA FORMA DE TROCAR ICONE

        toplevel.resizable(width=True, height=True)  # MET. QUE DETERMINA QUAIS EIXOS PODEM SER REDIMENSIONADOS
        #toplevel.wm_attributes("-transparentcolor", "SystemButtonFace",) # DEFINE TRANSPARENCIA DA JANELA PARA A COR SYST..
        toplevel.wm_attributes("-alpha",0.95)
       # toplevel.state('zoom') # DEFINE O MODO DE JANELA MAXIMIZADA AO EXECUTAR
        toplevel.overrideredirect(0) # Tira a barra de titulo da Janela

        # TAMANHO DAS BANDEIRAS
        self.flagSizeX=400
        self.flagSizeY=230

        # FRAMES
        self.fr0=Frame(toplevel)
        self.fr0.pack()
        self.fr1=Frame(self.fr0,padx=5,pady=5)
        self.fr1.grid(row=0,column=1)
        self.fr2=Frame(self.fr0,padx=5,pady=5)
        self.fr2.grid(row=1,column=1)

        #BANDEIRAS:-----------------------------------------------------------

        #JAPÃO
        self.labJapan=Label(self.fr1,text='JAPAN',font=('fixedsys','14'),bg='white')
        self.labJapan.grid(row=0,column=1)
        self.flagJapan=Canvas(self.fr1,width=self.flagSizeX,height=self.flagSizeY,bg='white')
        self.flagJapanX=float(self.flagJapan['width'])/6
        self.flagJapanY=float(self.flagJapan['height'])/4
        self.flagJapan.create_oval(self.flagJapanX*2,self.flagJapanY,
                                   self.flagJapanX*4,self.flagJapanY*3.5,
                                   fill='red',outline='')
        self.flagJapan.grid(row=1,column=1)

        # SUIÇA
        self.labSwit = Label(self.fr1, text='SWITZERLAND', font=('fixedsys', '14'),bg='white')
        self.labSwit.grid(row=0, column=2)
        self.flagSwit = Canvas(self.fr1,width=self.flagSizeX,height=self.flagSizeY, bg='red')
        self.flagSwitX=float(self.flagSwit['width'])/5
        self.flagSwitY = float(self.flagSwit['height']) / 5
        self.flagSwit.create_polygon([self.flagSwitX*1.45,self.flagSwitY*2],[self.flagSwitX*1.45,self.flagSwitY*3],[self.flagSwitX*2.15,self.flagSwitY*3],
                                     [self.flagSwitX*2.15,self.flagSwitY*4],[self.flagSwitX*2.85,self.flagSwitY*4],[self.flagSwitX*2.85,self.flagSwitY*3],
                                     [self.flagSwitX*3.52,self.flagSwitY*3],[self.flagSwitX*3.52,self.flagSwitY*2],[self.flagSwitX*2.85,self.flagSwitY*2],
                                     [self.flagSwitX*2.85,self.flagSwitY],[self.flagSwitX*2.15,self.flagSwitY],[self.flagSwitX*2.15,self.flagSwitY*2],fill='white')
        self.flagSwit.grid(row=1,column=2)

        # INGLATERRA
        self.labEng = Label(self.fr1, text='ENGLAND', font=('fixedsys', '14'),bg='white')
        self.labEng.grid(row=0, column=3)
        self.flagEng = Canvas(self.fr1,width=self.flagSizeX,height=self.flagSizeY, bg='white')
        self.flagEngFaixa = float(self.flagEng['height']) / 5
        self.flagEng.create_line([float(self.flagEng['width'])/2,0],[float(self.flagEng['width'])/2,float(self.flagEng['height'])],fill='red',width=self.flagEngFaixa)
        self.flagEng.create_line([0,float(self.flagEng['height'])/2],[ float(self.flagEng['width']),float(self.flagEng['height']) / 2], fill='red',width=self.flagEngFaixa)
        self.flagEng.grid(row=1,column=3)

        # BANDEIRA FRANÇA
        self.labFrance = Label(self.fr2, text='FRANCE', font=('fixedsys', '14'),bg='white')
        self.labFrance.grid(row=0, column=1)
        self.flagFrance = Canvas(self.fr2,width=self.flagSizeX,height=self.flagSizeY, bg='white')
        self.flagFranceX = float(self.flagFrance['width'])/3
        self.flagFrance.create_rectangle([0,0],[self.flagFranceX,float(self.flagFrance['height'])],fill='blue',outline='')
        self.flagFrance.create_rectangle([self.flagFranceX*2, 0], [self.flagFranceX*3, float(self.flagFrance['height'])], fill='red',outline='')
        self.flagFrance.grid(row=1,column=1)

        # BANDEIRA GRECIA
        self.labGreece = Label(self.fr2, text='GREECE', font=('fixedsys', '14'),bg='white')
        self.labGreece.grid(row=0, column=2)
        self.flagGreece = Canvas(self.fr2,width=self.flagSizeX,height=self.flagSizeY, bg='white',bd=0)
        self.flagGreeceFlamX=float(self.flagGreece['width'])/3
        self.flagGreeceY = float(self.flagGreece['height'])/2
        self.flagGreeceP5X = self.flagGreeceFlamX / 3
        self.flagGreeceP4X = float(self.flagGreece['width'])
        self.flagGreeceFaixa= float(self.flagGreece['height'])/9
        #PARTE DA FLAMULA
        self.flagGreece.create_rectangle([0,0],[self.flagGreeceFlamX,self.flagGreeceY+self.flagGreeceY/5],fill='dodgerblue4',outline='')
        self.flagGreece.create_line([self.flagGreeceFlamX/2,0],[self.flagGreeceFlamX/2,self.flagGreeceY+self.flagGreeceY/5],fill='white',width=self.flagGreeceFaixa)
        self.flagGreece.create_line([0, (self.flagGreeceY + self.flagGreeceY / 5)/2.05],[self.flagGreeceFlamX,(self.flagGreeceY + self.flagGreeceY / 5)/2.05], fill='white',width=self.flagGreeceFaixa)
        # PARTE LATERAL A FLAMULA DE 4 FAIXAS
        self.flagGreece.create_rectangle([self.flagGreeceFlamX, 0], [self.flagGreeceP4X, self.flagGreeceY+self.flagGreeceY/5], fill='dodgerblue4',outline='')
        self.flagGreece.create_line([self.flagGreeceFlamX,2*self.flagGreeceY/5.5],[self.flagGreeceP4X,2*self.flagGreeceY/5.5],fill='white',width=self.flagGreeceFaixa)
        self.flagGreece.create_line([self.flagGreeceFlamX, 4.3 * self.flagGreeceY / 5.5],[self.flagGreeceP4X, 4.3 * self.flagGreeceY / 5.5], fill='white', width=self.flagGreeceFaixa-9)
        # PARTE INFERIOR A FLAMULA DE 5 FAIXAS
        self.flagGreece.create_rectangle([0,self.flagGreeceY+self.flagGreeceY/5],[self.flagGreeceP4X,self.flagGreeceY*2],fill='dodgerblue4',outline='')
        self.flagGreece.create_line([0,self.flagGreeceY+self.flagGreeceY/5],[self.flagGreeceP4X,self.flagGreeceY+self.flagGreeceY/5],fill='white',width=self.flagGreeceFaixa-2)
        self.flagGreece.create_line([0,self.flagGreeceY+3*self.flagGreeceY/5],[self.flagGreeceP4X,self.flagGreeceY+3*self.flagGreeceY/5],fill='white',width=self.flagGreeceFaixa-2)
        self.flagGreece.grid(row=1,column=2)

        # BANDEIRA ALEMANHA
        self.labGermany = Label(self.fr2, text='GERMANY', font=('fixedsys', '14'),bg='white')
        self.labGermany.grid(row=0, column=3)
        self.flagGermany = Canvas(self.fr2,width=self.flagSizeX,height=self.flagSizeY, bg='white')
        self.flagGermanyX = float(self.flagGermany['width'])
        self.flagGermanyY = float(self.flagGermany['height']) / 3
        self.flagGermany.create_rectangle([0,0],[self.flagGermanyX,self.flagGermanyY],fill='black',outline='')
        self.flagGermany.create_rectangle([0, self.flagGermanyY], [self.flagGermanyX, 2*self.flagGermanyY], fill='red', outline='')
        self.flagGermany.create_rectangle([0, 2*self.flagGermanyY], [self.flagGermanyX, 3*self.flagGermanyY], fill='yellow', outline='')
        self.flagGermany.grid(row=1,column=3)



painel=Tk()
pYpanel(painel)
painel.mainloop()

# CONFIGURAÇÃO DE JANELA TK()
# http://stackoverflow.com/questions/30091675/resizing-tkinter-window-for-full-screen
# TROCAR ICONE DA JANELA
# http://www.jamesstroud.com/jamess-miscellaneous-how-tos/icons/tkinter-title-bar-icon