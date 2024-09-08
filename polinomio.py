import numpy as np
from math import gcd
class Polinomio:
    def __init__(self, poli = str()):
        self.poli = poli
        self.coeficientes = None

    def coeficiente(self,a = str()):
        lista = list()
        for i, v in enumerate(a):
            n = ''
            if v == '{':
                k = i
                while True:
                    if a[k+1] == '}':
                        break
                    k+=1
                    n = n+a[k]
                lista.append(n)
            try:
                m = a[i+1]
            except:
                if v.isalpha():
                    lista.append('1')
            else:
                if v.isalpha() and m != '^':
                    lista.append('1')
        return lista

    def root(self, lista_de_coeficientes2 = list(), lista_de_coeficientes3 = list()):
        d = {}
        m = max(lista_de_coeficientes2)
        for i in range(0,m+1):
            d[f'{i}'] = 0
        k = 0
        while True:
            if k in lista_de_coeficientes2:
                p = lista_de_coeficientes2.index(k)
                d[f'{k}'] = lista_de_coeficientes3[p]
            if k>m:
                break
            k+=1    
        return d

    def poly(self):
        eq = self.poli
        lista_de_coeficientes = []
        lista_de_coeficientes2 = []
        lista_de_coeficientes3 = []
        polinomio = []
        lista_de_caracteres = ['-','+']
        if not eq[0].isdigit() and not eq[0] in lista_de_caracteres:
            lista_de_coeficientes.append('1') 
        
        for i, v in enumerate(eq):
            if v in lista_de_caracteres and eq[i+1].isdigit() or v.isdigit() and i == 0:
                    k = i
                    inicio = ''
                    while True:
                        inicio = inicio + eq[k]
                        k+=1
                        if not eq[k].isdigit():
                            lista_de_coeficientes.append(inicio)
                            break
            elif not v.isdigit() and eq[i-1] in lista_de_caracteres:
                lista_de_coeficientes.append(eq[i-1]+'1')
        lista = self.coeficiente(eq)
        for _, v in enumerate(lista):
            lista_de_coeficientes2.append(int(v))
        for i in lista_de_coeficientes:
                lista_de_coeficientes3.append(int(i))
        self.coeficientes = lista_de_coeficientes3
        d = self.root(lista_de_coeficientes2, lista_de_coeficientes3)
        for v in d.values():
            polinomio.append(v)
        polinomio.reverse()
        poly = np.poly1d(polinomio)
        return poly

class Numero:
    def __init__(self, value = int()):
        self.value = value
    def fat(self):
        a = self.value
        k = 2
        fat = []
        resul = []
        resul2 = str()
        while(True):
            if a%k == 0:
                a = a/k
                fat.append(k)
                k = 2
            else:
                k+=1
            if a == 1:
                break
        for i in fat:
            if not i in resul:
                resul.append(i)
        self.prime = resul
        for _,i in enumerate(resul):
            resul2 = resul2+f'{i}^{fat.count(i)} \\cdot'

        return resul2+'1'
    
def mod(a = int(), c = int(), m = int()):
    x = 0
    while True:
        if ((a*x)-c)%m == 0:
            break
        x+=1
    return x

def teoch(equa = list()):
    k = 0
    m = np.prod(equa[2::3])
    xl = []
    while True:
        lista = equa[3*k:3*(k+1)]
        b = mod(lista[0],lista[1], lista[2])
        y = m/lista[2]
        yi = mod(y,1,lista[2])
        result = b*y*yi
        xl.append(result)
        k+=1
        if 3*(k+1)>(len(equa)):
            break
    return [sum(xl)%m,m]



def dioequa(a = int(), b = int(), c = int()):
     d = gcd(a,b)
     k = c//d
     m = a//d
     n = b//d
     r = k%m
     x0 = (k//m) + (teoch([1,r,n,1,0,m])[0]//m)
     y0 = (-teoch([1,r,n,1,0,m])[0]+r)//n
     return [f'{x0}+{n}k',f'{y0}-{m}k']

