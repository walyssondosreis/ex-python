#coding: utf-8
#TITLE: FRAÇÃO - SOBRECARGA DE OPERADORES
#AUTHOR: WALYSSON PEREIRA DOS REIS

class fraction:
    """CLASSE QUE EXECUTA OPERAÇÕES FUNDAMENTAIS COM FRAÇÕES"""
    def __init__(self,n,d):
        """ MÉTODO CONSTRUTOR """
        self.valor=[n,d]
    def simplificar(self,u):
        h=u
        cont=2
        while cont<=u[0] and cont<=u[1]:
            if (h[0]%cont==0 and h[1]%cont==0):
                h[0]=h[0]/cont ; h[1]=h[1]/cont
            else: cont+=1
        return h
    def __add__(self, other):
        """ MÉTODO SOMA (A+B)"""
        if self.valor[1]!=other.valor[1]:
            denominador=float(self.valor[1]*other.valor[1])
            numerador=(denominador/self.valor[1])*self.valor[0]+(denominador/other.valor[1])*other.valor[0]
            return self.simplificar([numerador,denominador])
        else:
            return self.simplificar([self.valor[0]+other.valor[0],self.valor[1]])
    def __sub__(self, other):
        """ MÉTODO SUBTRAÇÃO (A-B)"""
        if self.valor[1]!=other.valor[1]:
            denominador=float(self.valor[1]*other.valor[1])
            numerador=(denominador/self.valor[1])*self.valor[0]-(denominador/other.valor[1])*other.valor[0]
            return self.simplificar([numerador,denominador])
        else:
            return self.simplificar([self.valor[0]-other.valor[0],self.valor[1]])
    def __mul__(self, other):
        """ MÉTODO MULTIPLICAÇÃO (A*B)"""
        return self.simplificar([self.valor[0]*other.valor[0],self.valor[1]*other.valor[1]])
    def __truediv__(self, other): #NO PYTHON 2.7 O MÉTODO ESPECIAL SERIA __div__
        """MÉTODO DIVISÃO (A/B)"""
        return self.simplificar([self.valor[0]*other.valor[1],self.valor[1]*other.valor[0]])
    def __pow__(self, power, modulo=None):
        """ MÉTODO POTENCIAÇÃO (A**N)"""
        return self.simplificar([self.valor[0]**power,self.valor[1]**power])
    def __call__(self, *args, **kwargs):
        print('TROREI!')
        return 'Argumento Callable do Objeto:',args
    def __str__(self):
        return 'string que define comportamento do print do objeto para esta frase!'

b=fraction(2,6)
c=fraction(4,6)


print(b.valor,'+', c.valor,'=',b+c)
print(b.valor,'-', c.valor,'=',b-c)
print(b.valor,'*', c.valor,'=',b*c)
print(b.valor,'/', c.valor,'=',b/c)
print(b.valor,'^',2,'=',b**2)
#print(callable(b))
#print(b('Obj B CHAMANDO!'))
a=fraction(1,1)
print(a)
#print(help(b))

