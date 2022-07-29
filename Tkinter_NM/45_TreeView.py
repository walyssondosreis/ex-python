# coding: utf-8
# TITLE: TreeView Widget
# AUTHOR: WALYSSON PEREIRA DOS REIS
# EMAIL: walyssondosreis@email.com
# TKINTER 8.5 REFERENCE A GUI FOR PYTHON : NEW MEXICO
# SECTION 14 (PG 137:145)

#! LEGENDA: #! SIGNICA NÃO DESOMENTAR

from tkinter import *
from tkinter.ttk import *

class app:
    def __init__(self,toplevel):
        self.fr1=Frame(toplevel)
        self.fr1.grid()
        toplevel.columnconfigure(0,weight=1)
        toplevel.rowconfigure(0,weight=1)

        # SCROLLS PARA TREEVIEW
        self.yScroll = Scrollbar(self.fr1, orient=VERTICAL)  # DEFINE O SCROLL VERTICAL
        self.yScroll.grid(row=0, column=2, sticky=N + S)
        self.xScroll = Scrollbar(self.fr1, orient=HORIZONTAL)  # DEFINE O SCROLL HORIZONTAL
        self.xScroll.grid(row=1, column=1, sticky=E + W)

        #! ATRUBUTOS E DECLARAÇÃO DO TREEVIEW
        #---------------------------------------------------------------------------------------------
        self.tv=Treeview(self.fr1)#! CRIA UMA TREEVIEW WIDGET
        #! O ATRIBUTO class_='NomeDaClasse'SÒ PODERA SER INFORMADO UMA VEZ E NA CRIAÇÃO DO WIDGET. SERVE PARA QUE ...
        #! ... POSSAMOS DEFINIR UMA NOVA CLASSE DE WIDGET RESPONSAVEL PELO TREEVIEW
        self.tv.grid(row=0,column=1)
        self.tv['columns']=('col1','col2','col3') #! IDENTIFICA AS COLUNAS DENTRO DO WIDGET, SÂO ID INTERNAS APENAS NÃO SENDO EXIBIDAS
        #! o '#0' SEMPRE SERA NA PRIMEIRA COLUNA E SEMPRE IDENTIFICARÁ O ÍCONE DA COLUNA (column icon)
        #! AS COLUNAS ADICIONAS NORMAIS COM columns SÃO ADICIONADAS DENTRO DO ICONE DA COLUNA.
        #self.tv['cursor']='mouse' # ESPECIFICA O ICONE DO MOUSE A SER MOSTRADO QUANDO PASSADO SOBRE A ARVORE
        #self.tv['displaycolumns']=('col3','col2') #! ESPECIFICA QUAIS COLUNAS SERÃO MOSTRADAS
        #! PODENDO SER '#all' PARA TODAS ou O NUMERO DA COLUNA (O-N)ou A IDENTIDFADE DA COLUNA
        self.tv['height']=10 #! ESPECIFICA O TAMANHO DESEJADO DA ARVORE EM QUANTIDADE DE LINHAS
        self.tv['padding'] = (2,2,2,2) #! ADICONA ESPAÇAMENTO EXTRA DENTRO DO CONTEUDO DO WIDGET...
        #! ...PODENDO PASSAR UMA TUPLA QUE IRA EQUIVALER AS DIMENSOES (LEFT,TOP,RIGHT,BOTTOM) OU...
        #! ...PASSANDO APENAS UM ARGUMENTO QUE EQUIVALERA AS QUATRO DIMENSÕES
        self.tv['selectmode'] = EXTENDED # DEFINE O TIPO DE SELEÇÃO DOS ITENS DA TABELA/ARVORE...
        #! ...PODENDO SER: 'BROWNSE' or 'EXTENDED' or 'NONE'
        #self.tv['show']='tree' #! PARAMETRO QUE DEFINE SE OS ROTULOS DAS COLUNAS SERÃO MOSTRADOS OU NÃO...
        #! ... PARA QUE NÃO SEJAM MOSTRADOS USE O ATRIBUTO 'tree'
        #self.tv[style]= * # PERSONALIZA OS NOMES NOS ROTULOS DO WIDGET
        #self.tv['takefocus'] =True # ESPECIFICA SE O WIDGET DE ARVORE IRÁ ACEITAR OU NÃO A VISITA' DE FOCUS

        # ---------------------------------------------------------------------------------------------
        #! MÉTODOS DO TREEVIEW
        # ---------------------------------------------------------------------------------------------
        #cord=self.tv.bbox() #! RETORNA AS CORDENADAS X,Y DO iid ITEM BUSCADO ASSIM COMO O TAMANHO...
        #! REQUER ARGUMENTO (iid ITEM, column=None)
        #print(cord)
        # ---------------------------------------------------------------------------------------------
        self.tv.column('#0',anchor=CENTER) # DEFINE ALGUMAS PROPRIEDADES DA COLUNA ...
        #! O anchor DEFINE O POSICIONAMENTO DO CONTEUDO DO WIDGET PODENDO SER N or S or E or W
        #! O PRIMEIRO ARGUMENTO REFERE-SE AO INDICE DA TABELA OU NUMERO LOGICO DA COLUNA ...
        #! O #0 COMO SEMPRE REFERENCIA A PRIMEIRA COLUNA ( Column ICON)
        #self.tv.column(1, id='colu1') # id DEFINE A ID DA COLUNA QUE É UMA OPçÃO SOMENTE LEITURA DEFINIDO NO CONSTRUTOR
        self.tv.column('#0',minwidth=30) # minwidth DEFINE UMA LARGURA MÍNIMA PARA A COLUNA, POR PADRÃO É 20 PIXELS
        self.tv.column('col1',stretch=True) # stretch ATIVA OU NÃO O REDIMENSIONAMENTO DA COLUNA
        self.tv.column('#0',width=200) #! width LARGURA INICIAL DA COLUNA EM PIXELS , O PADRÃO É 200
        #resp=self.tv.column('#0') #! AO NÃO FORNECER OPÇÕES O METODO RETORNA UMA TUPLA CONTENDO AS CONF. DE TODOS OS ATRIBUTOS ATUAIS
        #print(resp)
        #resp2=self.tv.column('#0',option='width') #! option PERGUNTA O VALOR DO ARGUMENTO ESPECIFICADO
        #print(resp2)
        # ---------------------------------------------------------------------------------------------
        self.tv.heading('#0',anchor=CENTER,text='Column Icon') #! HEADING CONFIGURA O CABEÇALHO DA COLUNA
        self.tv.heading(0, anchor=CENTER, text='Coluna 1') #! PODE-SE PASSAR TANTO O INDICE QUANDO O ID DE COLUNA COMO ARGUMENTO
        self.tv.heading('col2', anchor=CENTER, text='Coluna 2') #! anchor IRÁ POSICIONAR O TEXTO DA COLUNA
        self.tv.heading(2, anchor=CENTER, text='Coluna 3') #! text IRÀ DEFINIR ALGO A SER EXIBIDO NA DESCRIÇÃO DA COLUNA
        #self.tv.heading('#0',command=print('EVENTO DA COLUNA')) #! command ESPECIFICA UM PROCEDIMENTO PARA QUANDO HOUVER UM CLICK NA COLUNA
        # self.tv.heading(2,image=*) #
        # PARA OBTER RESPOSTA DE VALORES DE CONFIGURAÇÔES EM TUPLAS, USE O MESMO QUE APLICADO PARA column ACIMA
        # ---------------------------------------------------------------------------------------------
        #.identify_column(x) # PASSANDO-SE UMA COORDENADA X O METODO RETORNARÁ UM TUPLA CONTENDO EM QUAL COLUNA SE ENCONTRA A ...
        #! ... COORDENADA, NO MODELO '#1', QUANDO FOR NA PRIMEIRA SERÀ '#0' ENTÃO NESTE CASO SERÁ CONSIDERADO A CONTAGEM FISICA,...
        #! ...SENDO A PRIMEIRA COLUNA DEPOIS DO #0 (Icon COlumn) A NUMERO 1
        # ---------------------------------------------------------------------------------------------
        #.identify_element(x,y) # RETORNA TUPLA COM O NOME DO ELEMENTO NA COORDENADA PASSADA COMO ARGUMENTO, NÃO HAVENDO ELEMENTOS SERÁ VAZIA ''
        # ---------------------------------------------------------------------------------------------
        #.identify_region(x,y) # RETORNA O NOME DA REGIÃO QUE CONTEM O PONTO ESPECIFICADO ...
        #! ... PODENDO SER O RETORNO: 'nothing' or 'heading' or 'separator' or 'tree' or 'cell'
        # ---------------------------------------------------------------------------------------------
        #.identify_row(y) # RETORNA o iid DO IDEM O QUAL A CORDENADA BATE. CASO NÃO HOUVER SERÁ RETORNADO VAZIO ''
        # ---------------------------------------------------------------------------------------------
        #.index(iid) # RETORNA O NUMERO DE INDICE DO iid ESPECIFICADO, EM RELAÇÃO AO SEU PAI (PARENT)
        # ---------------------------------------------------------------------------------------------
        #.set_children (item,newChildren) #! DEFINE NOVOS FILHOS PARA O ITEM PASSADO O SEU iid. CASO JA EXISTA UMA REALAÇÃO...
        #! ... ANTERIOR DE CHILDREN ESTA SERÁ REMOVIDA
        # ---------------------------------------------------------------------------------------------
        self.tv.insert(parent='',index='end',iid='L1',open=False,tags='L1tag',text='Linha 1 ICO',
                       values=('VALOR1','VALOR2','VALOR3'))
        self.tv.insert(parent='', index='end', iid='L2', open=False, tags='L2tag', text='Linha 2 ICO',
                       values=('WALYSSON', 'GERALD', 'CHESPIRITO'))
        self.tv.insert(parent='', index='end', iid='L3', open=False, tags='L3tag', text='Linha 3 ICO',
                       values=('BRAZIL', 'ENGLAND', 'MEXICO'))
        #! parent IRÁ DEFINIR A HIERARQUIA DA INSERÇÃO, O SEJA A QUAL ITEM SERA ADICIONADO
        #! index IRÁ DEFINIR A POSIÇÃO DA INSERÇÃO  NA HIERARQUIA
        #! iid IRÀ DEFINIR UMA IDENTIDADE PARA A 'LINHA'/VALOR INSERIDO , A iid SEMPRE SERÁ UNICA
        #! image É O ARGUMENTO DE IMAGEM QUE PODERÁ SER ATRIBUIDO APENAS A DIREITA DO ICONE
        #! open DEFINE SE O PADRÃO INCIAL DA HIERARQUIA DESSE ITEM SERÁ ABERTO OU FECHADO (PADRÂO)
        #! tags ASSOCIA UMA STRING AO ITEM ADICIONADO , A TAG PODERÁ SER COMPARTILHADA
        #! text IRÁ FORNECER UM DESCRIÇÃO PARA COLUNA ICON DO ITEM ADICIONADO
        #! values  SÃO OS VALORES FORNECIDOS PARA O ITEM QUE SERÀ ALOCADO NAS COLUNAS EM SEQUENCIA LOGICA,...
        #! ...PARA VALORES QUE EXCEDAM AS POSIÇÕES NÃO SERÁ CRIADO OUTRA COLUNA, NEM MESMO RETORNADO ERRO, APENAS SERÂO DESCARTADOS
        # ---------------------------------------------------------------------------------------------
        self.tv.item('L1',values=['NOVO VALOR 1','NOVO VALOR 2','NOVO VALOR 3']) #! ESTE MÉTODO CONSEGUE ALTERAR OS ATRIBUTOS DO ITEM
        #! POSE ALTERERAR DIVERSOS OUTRO ATRIBUTOS QUE FORAM FORNECIDOS NA CRIAÇÃO DESTE ITEM
        # ---------------------------------------------------------------------------------------------
        iterecov=self.tv.item('L1') #! RETORNA UM DICIONARIO COM TODOS OS VALORES DOS ATRIBUTOS DO ITEM BUSCADO PELO iid
        #print(iterecov)
        # ---------------------------------------------------------------------------------------------
        #iterecov2=self.tv.item('L2',option='values') #! RETORNA UMA TUPLA CONTENDO OS VALORES DO ATRIBUTO DESEJADO
        #print(iterecov2)
        # ---------------------------------------------------------------------------------------------
        #self.tv.move('L2','L1',1) # MOVE UM ITEM PARA DENTRO DE OUTRO ITEM OU PARENT PASSANDO ASSIM , O ITEM A SER MOVIDO,...
        #! ... O ITEM PARENT (PARA ONDE SERA MOVIDO) E O INDICE DA POSIÇÃO A QUAL ELE OCUPARA
        # ---------------------------------------------------------------------------------------------
        #nid=self.tv.next('L2') # RETORNA O iid DO PROXIMO ITEM NA SEQUENCIA DE UM PARENT, CASO ESTE SEJA ULTIMO NÃO SERA RETORNADO NADA
        #print(nid)
        # ---------------------------------------------------------------------------------------------
        #pid=self.tv.parent('L1') # SE O iid SOLICITADO FOR UM TOPLEVEL SERÁ RETORNADO UMA STRING VAZIA, SE NÃO SERA RETORNADO O idd PARENT
        #print(pid)
        # ---------------------------------------------------------------------------------------------
        #previd=self.tv.prev('L3') # SE O iid SOLICITADO FOR UM child SERA RETORNADO O iid DO child ANTERIOR,..
        #!... SE O iid FOR UM TOP LEVEL SERÁ RETORNADO O TOPLEVEL ANTERIOR, SE NÂO SERA RETORNADO UM STRING VAZIA
        # ---------------------------------------------------------------------------------------------
        #self.tv.see('L2') # GARANTE QUE O ITEM COM O iid PASSADO ESTEJA VISIVEL NO WIDGET
        # ---------------------------------------------------------------------------------------------
        #self.tv.selection_add('L1','L2','L3') # POSICIONA O SELETOR NA(s) iid(s) PASSADAS COMO ARGUMENTO, SE JA TIVEREM ITENS SELECIONADOS...
        #!... ESTES SÒ SERÃO SOMADOS A NOVA SELEÇÃO
        # ---------------------------------------------------------------------------------------------
        #self.tv.selection_remove('L2') # DESSELECIONA O(s) ITEM(s) COM idd PASSADO(s)
        # ---------------------------------------------------------------------------------------------
        #self.tv.selection_set('L3','L1') #! SELECIONA ITENS NA TABELA , SE JA TIVEREM ITENS SELECIONADOS ESTES SERÃO DESSELECIONADOS
        # ---------------------------------------------------------------------------------------------
        #self.tv.selection_toggle('L3','L2') #! SELECIONA O ITEM DA SEGUINTE FORMA: SE O ITEM JA ESTIVER SELECIONADO NA LISTA ELE SERÁ...
        #! ...DESCELECIONADO , SE NÃO ESTIVER SELECIONADO SERÁ ENTÂO SELECIONADO.
        # ---------------------------------------------------------------------------------------------
        #conflinha=self.tv.set('L2') # PODE SER USADO PARA RECUPERAR OS VALORES DE UMA iid POR COLUNAS OU PARA ALTERA-LOS...
        #!... SERÀ RETORNADO UM DICIONARIO CONTENDO O ID DAS COLUNAS COM SEUS RESPECTIVOS VALORES
        self.tv.set('L2',column='col2',value='FREDERICK')
        #print(conflinha)
        # ---------------------------------------------------------------------------------------------
        #self.tv.tag_bind('L2tag',sequence='<1>',callback=self.eventTree) # ASSOCIA UM EVENTO BIND QUALQUER A UMA TAG DE ITEM REGISTRADA
        #!... ONDE O CALLBACK È UM METODO DE EVENTO E SEQUENCE É UM EVENTO DO MOUSE OU TECLADO
        # ---------------------------------------------------------------------------------------------
        self.tv.tag_configure('L2tag',background='red') # O tag_configure ALTERA CONFIGURAÇÕES POR TAG NA LISTA
        self.tv.tag_configure('L3tag',font=('System','11','bold'))
        #! EXISTE AINDA O ATRIBUTO DE 'image' QUE DEFINE UMA IMAGEM A SER MOSTRADAS NO(s) ITEM(s) COM A TAG
        # ---------------------------------------------------------------------------------------------
        #tagconfig=self.tv.tag_configure('L3tag') #! QUANDO CHAMADO RETORNA UM DICIONARIO COM A DEFINIÇÃO DE TODOS OS ATRIBUTOS DA TAG
        #print(tagconfig)
        # ---------------------------------------------------------------------------------------------
        #tagh=self.tv.tag_has('L1tag') #! RETORNA TODOS OS ITENS CADASTRADOS COM A TAG PASSADA
        #print(tagh)
        # ---------------------------------------------------------------------------------------------
        #tagh2=self.tv.tag_has('L1tag','L1') #! RETORNA UM BOLEANO INFORMANDO SE EXISTE O iid PASSADO DENTRO DA TAG PASSADA
        #print(tagh2)
        # ---------------------------------------------------------------------------------------------
        #self.tv.bind('<<TreeviewSelect>>',self.eventTree) # O EVENTO VIRTUAL TreeviewSelect EXECUTA UM EVENTO A CADA ITEM SELECIONADO
        # ---------------------------------------------------------------------------------------------
        #self.tv.bind('<<TreeviewOpen>>',self.eventTree) # O EVENTO VIRTUAL TreeviewOpen EXECUTA UM EVENTO PARA CADA ITEM ABERTO
        # ---------------------------------------------------------------------------------------------
        #self.tv.bind('<<TreeviewClose>>',self.eventTree)  # O EVENTO VIRTUAL TreeviewOpen EXECUTA UM EVENTO PARA CADA ITEM FECHADO
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        #.delete(*items) #! APAGA ITENS DA ARVORE PELO iid, OS ITENS SÂO REALMENTE DESTRUIDOS
        # ---------------------------------------------------------------------------------------------
        #.detach(*items) #! REMOVE ITENS DA ARVORE PELO iid, OS ITENS NÃO SÂO DESTRUIDOS E PODEM SER RETORNADOS USANDO O MED move()
        # ---------------------------------------------------------------------------------------------
        #.exists(iid) #! RETORNA UM BOLEANO DIZENDO SE EXISTE OU NÂO O ITEM NA ARVORE/TABELA, MESMO ESTE ITEM NÃO SENDO VISIVEL
        # ---------------------------------------------------------------------------------------------
        #.focus([iid]) # NÃO PASSANDO ARGUMENTO RETORNA O iid DO ITEM EM FOCO, CASO PASSE VOCÊ ESTARA COLOCANDO O ITEM COM iid EM FOCO
        # ---------------------------------------------------------------------------------------------
        #.getchildren([item]) # RETORNA UMA TUPLA CONTENDO OS VALORES DO ITEM FORNECIDO, CASO NÃO SEJA PASSADO ARGUMENTOS...
        #! ... ESTE RETORNARA UM TUPLA COM OS ELEMENTO DA TOPLEVEL
        # ---------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] = self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        # ---------------------------------------------------------------------------------------------



    def eventTree(self,event):
        print('EVENTO NA RODANDO')
        pass


root=Tk()
app(root)
root.mainloop()

# DEFINIÇÕES PARA ARVORE
#---------------------------------------------------------------------------------------------
#! item: UMA DAS ENTIDADES MOSTRADAS NO WIDGET, PODENDO SER UM DIRETORIO OU ARQUIVO...
#! ... CADA ITEM É ASSOCIADO COM UM LABEL QUE TAMbÉM PODE CONTER UMA IMAGEM OU TEXTO
#---------------------------------------------------------------------------------------------
#! iid : É O QUE IDEFICA O ITEM NA ARVORE, PODENDO SER SUPRIMIDO NA DECLARAÇÃO, ISSO FARÁ...
#! COM QUE O ttk GERA UM IID AUTOMATICA , OU PODENDO SER INFORMADO MANUALMENTE
#---------------------------------------------------------------------------------------------
#! child : PARTINDO-SE DE UMA HIERARQUIA SÃO OS HERDEIROS OU FILHOS DE UM PARENT
#---------------------------------------------------------------------------------------------
#! parent: PARTINDO-SE DE UMA HIERARQUIA, O ITEM QUE NÃO CONTER UM PARENT É O TOPO...
#! DA LISTA (toplevel), NÃO SENDO ESTE SERÁ child DO ITEM QUE O CONTEM
#---------------------------------------------------------------------------------------------
#! ancestor: O PAI DO PAI , ITEM ANTECESSOR, ATÉ NIVEL MAIS ALTO DA ARVORE.
#---------------------------------------------------------------------------------------------
#! visible: UM ITEM DO TOPO QUE É SEMPRE VISIVEL, OU QUANDO VISIVEL.
#---------------------------------------------------------------------------------------------
#! descendant: É TODA A SUBARVORE APARTIR DE UM ITEM
#---------------------------------------------------------------------------------------------
#! tag: IDENTICA UM OU MAIS ITEMS COM UMA PALAVRA CHAVE PARA QUE POSSA...
#! ... POSTERIORMENTE USAR ESSA TAG PARA MANIPULAR OS ITENS DA ARVORE
#!... AS TAGS TAMBÉM PODERA SER ASSOCIADAS COM EVENTOS
#---------------------------------------------------------------------------------------------
