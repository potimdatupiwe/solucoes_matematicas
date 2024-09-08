from django.shortcuts import render,redirect
import polinomio as pn
import matplotlib.pyplot as plt
import numpy as np
from .models import Question, User
from django.utils import timezone
import datetime
def logout(request):
    try:
        u = User.objects.get(user = request.session['usuario'])
    except:
        pass
    else:
        if u.logoutuser():
            u.login = False
            u.save()

def register(request):
    if request.method == 'GET':
        return render(request, 'polls/user.html')
    else:
        usuario  = request.POST.get('usuario')
        senha = request.POST.get('senha')
        verificacao = False
        try:
            user1 = User.objects.get(user = usuario, password = senha)
        except:
            verificacao = True
            context = {'verificacao':verificacao}
            return render(request, 'polls/user.html', context)
        else: 
            request.session['usuario'] = usuario
            request.session.save()
            user1.login_date = timezone.now()
            user1.login = True
            user1.save()
            return redirect('polinomio2')

def polinomio2(request, verificacao = False, value = str()):
    if request.method == 'GET' or verificacao:
        logout(request)
        context = {'verificacao':verificacao,
                   'valor':value}
        return render(request, 'polls/index.html',context)
    else:
        verificacao = False
        polinomio3 = request.POST.get('polinomio2')
        diretorio = 'static/imagens/pol.png'
        polinomio1 = pn.Polinomio(polinomio3)
        po = polinomio1.poly()
        r = np.roots(po)
        r2 = r.tolist()
        x = np.linspace(-10000, 10000)
        y = po(x)
        fig = plt.figure(clear=True)
        plt.plot(x,y)
        fig.savefig(diretorio)
        verificacaop = True
        if 'usuario' in request.session:
            session = request.session['usuario']
            u = User.objects.get(user = str(session))
            if u.login:
                q = Question(user12 = u, url = 'polinomio2')
                q.value = polinomio3
                q.save()
        context = {'r':r2,
                   'p':polinomio3,
                   'verificacaop':verificacaop}
        return render(request,'polls/index.html', context)

def equadio(request,verificacao = False, value = str()):
    if request.method == 'GET' or verificacao:
        logout(request)
        context = {'verificacao':verificacao,
                   'valor':value}
        return render(request, 'polls/equadio.html', context)
    else:
        equadiof = request.POST.get('equadio')
        eq = str()
        lista = []
        for i,v in enumerate(equadiof):
            if v == '=':
                a = i
                break
            eq = eq+v
        eq2 = equadiof[a+1:]
        p = pn.Polinomio(eq)
        p.poly()
        a = p.coeficientes[0]
        b = p.coeficientes[1]
        c = int(eq2)
        resul = pn.dioequa(int(a),int(b),int(c))
        verificacao2 = True
        for k in equadiof:
            if k.isalpha():
                lista.append(k)
        if 'usuario' in request.session:
            session = request.session['usuario']
            u = User.objects.get(user = str(session))
            if u.login:
                q = Question(user12 = u, url = 'equacaodio')
                q.value = equadiof
                q.save()
        context = {'verificacao2':verificacao2,
                'resul':resul,
                'equadiof':equadiof,
                'lista':lista}
        return render(request,'polls/equadio.html', context)    

def number(request,verificacao = False, value = str()):
    if request.method == 'GET' or verificacao:
        logout(request)
        context = {'verificacao':verificacao,
                   'valor':value}
        return render(request, 'polls/number.html', context)
    else:
        
        Nu = request.POST.get('numero')
        numero = pn.Numero(int(Nu))
        fat = numero.fat()
        if len(numero.prime)>1:
            isprimebool = False
        else:
            isprimebool=True
        verificacao2 = True
        context = {'verificacao2':verificacao2,
                   'isprimebool':isprimebool,
                   'fat':fat,
                   'N':Nu}
        if 'usuario' in request.session:
            session = request.session['usuario']
            u = User.objects.get(user = str(session))
            if u.login:
                q = Question(user12 = u, url = 'number')
                q.value = Nu
                q.save()
        return render(request, 'polls/number.html', context)

listamais = [0]
listamenos = [0]
def teoch(request,verificacao = False, value = str()):
    m = 0
    n = 0
    if request.method == 'GET' or verificacao:
        logout(request)
        k9 = str()
        i = 0
        listamais.clear()
        listamenos.clear()
        if verificacao:
            l2 = []
            l3 = []
            while True:
                if value[i].isdigit():
                    k9 = k9+value[i]
                else:
                    if k9!='':
                        l2.append(int(k9))
                    k9 =str()
                
                i+=1
                if i>=len(value):
                    break
            listamais.append(int((len(l2)-1)/6))
            m = sum(listamais)
            for i in range(0,int(len(l2)/3)):
                l3.append(l2[3*i:3*(i+1)])
            context = {'m':range(0,m+1),
                        'verificacao':verificacao,
                        'l3':l3}
            return render(request,'polls/teoch.html',context)
        return render(request,'polls/teoch.html',{'m':range(0,m+1),
                                                  'verificacao':verificacao})
    
    if '+' in request.POST or '-' in request.POST and not 'Enviar' in request.POST:
       
        if '+' in request.POST:
            m+=1
            listamais.append(m)
        if '-' in request.POST :
            n += 1
            listamenos.append(n)
        if sum(listamais)-sum(listamenos)>=1:
            verificacao2 = True
        else:
            verificacao2 = False
        q = sum(listamenos)
        p = sum(listamais)
        j = p-q
        context = {'m':range(0,j+1),
                   'v':verificacao2}
        return render(request,'polls/teoch.html', context)
    else:
        l = []
       
        for i in request.POST:
            if i.isdigit():
                for k in request.POST.getlist(f'{i}'):
                    l.append(int(k))    
        k = pn.teoch(l)
        a = k[0]
        b = k[1]
        q = sum(listamenos)
        p = sum(listamais)
        j = p-q
        if 'usuario' in request.session:
            session = request.session['usuario']
            u = User.objects.get(user = str(session))
            if u.login:
                k = str()
                for i in l:
                    k = k+' '+str(i)+' '
                q = Question(user12 = u, url = 'teoch')
                q.value = k
                q.save()    
        context = {'m':range(0,(j+1)),
                   'l':f'{b}k+{a}',
                   'e':'Enviar' in request.POST,
                   'verificacao':verificacao}
        return render(request,'polls/teoch.html', context)


def historic(request):
    logout(request)
    if 'usuario' in request.session:
        usuario = request.session['usuario']
        u = User.objects.get(user = usuario)
        verificacao2 = False
        verificacao = True
        if u.login:
            lista_question = list(Question.objects.filter(user12 = u))
            lista = lista_question
            for i in lista_question:
                        if i.value=='':
                            lista.remove(i)
            if len(lista) == 0:
                verificacao2 = True
            if request.method == 'POST':
                lista_request = list(request.POST)
                if lista_request[1][1].isdigit():
                    p = int(lista_request[1][1:])
                    u = lista_question[p]   
                    u.delete()
                    u.save()
                    for i in lista_question:
                        if i.value=='':
                            lista.remove(i)
                else:
                    value2 = request.POST.getlist('question')
                    u2 = Question.objects.get(value = value2[0], user12 = str(request.session['usuario']))
                    if u2.url == 'polinomio2':
                        return polinomio2(request, verificacao, value2[0])
                    if u2.url == 'equacaodio':
                        return equadio(request, verificacao, value2[0])
                    if u2.url == 'number':
                        return number(request, verificacao, value2[0])
                    if u2.url == 'teoch':
                        return teoch(request, verificacao, value2[0]) 
            return render(request, 'polls/historic.html',
                                {'lista_question':lista,
                                'verificacao2':verificacao2})
        else:
            return render(request, 'polls/historic.html',{'verificacao':True})
    else:
        return render(request, 'polls/historic.html',{'verificacao':True})

def cadastro(request):
    if request.method == 'GET':
        return render(request,'polls/cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user_exist = False
        try:
            user = User.objects.get(user=usuario)
        except:
            user = User(user = usuario, password = senha, login_date = (timezone.now()-datetime.timedelta(minutes=60)))
            user.save()
            return redirect('register')
        else:
            user_exist = True
            return render(request, 'polls/cadastro.html',{'user_exist':user_exist})
def mudarsenha(request):
    if request.method == 'GET':
        return render(request, 'polls/mudarsenha.html')
    else:
        usuario = request.POST.get('usuario')
        try:
            u = User.objects.get(user = usuario)
        except:
            verificaco3=True
            return render(request,'polls/mudarsenha.html', {'verificacao3':verificaco3})
        else:
            senha2 = request.POST.get('password')
            senha=request.POST.get('password2')
            if senha != senha2:
                return render(request, 'polls/mudarsenha.html',{'v':True})
            u.password=senha
            u.save()
            return redirect('register')