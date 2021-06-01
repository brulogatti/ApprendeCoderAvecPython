""""
def deux_egaux(x,y,z):
    if x==y:
        return True
    elif x==z:
        return True
    elif y==z:
        return True
    else:
        return False

x=int(input())
y=int(input())
z=int(input())
print(deux_egaux(x,y,z))
"""
""""
def soleil_leve(x,y,z):
    if x<=y:
        if z>=x and z<y:
            return True
        if x==12 and y ==12:
            return False
        if x==0 and y==0:
            return True
        else:
            return False
    else:
        if z<y:
            return True
        if z>=x:
            return True
        else:
            return False


x_e1515= int(input())
y_e1515 = int(input())
x_e666 = int(input())
y_e666=int(input())

for i in range(24):
    if ((soleil_leve(x_e1515,y_e1515,i)==True) or (soleil_leve(x_e666,y_e666,i)==True)):
        print(i)
    else:
        print(i,"*")
"""
"""
def premier(n):
    cont = 0
    if n==1:
        return False
    else:
        for i in range(1,n+1):
            if n%i==0:
                cont=cont+1
        if cont==2:
            return True
        else:
            return False


x=int(input())
for j in range(2,x):
    if premier(j)==True:
        print(j)
"""
"""
import random

def alea_dice(s):
    random.seed(s)
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    d3=random.randint(1,6)
    resposta = False
    if (d1==4 and d2==2 and d3==1):
        resposta=True
    elif (d1==4 and d2==1 and  d3==2):
        resposta = True
    elif (d1==2 and d2==4 and  d3==1):
        resposta=True
    elif (d1==2 and d2==1 and d3==4):
        resposta = True
    elif (d1==1 and d2==4 and d3==2):
        resposta=True
    elif (d1==1 and d2==2 and d3==4):
        resposta = True
    return resposta


def rendre_monnaie(valeur,v20,v10,v5,v2,v1):
    valor=v20*20+v10*10+v5*5+v2*2+v1*1
    if (valor==valeur):
        x20=0
        x10=0
        x5=0
        x2=0
        x1=0
    elif valor<valeur:
        x20=None
        x10=None
        x5=None
        x2=None
        x1=None
    else:
        resultado=valor-valeur
        x20=resultado//20
        resultado=resultado-20*x20
        x10=resultado//10
        resultado=resultado-10*x10
        x5=resultado//5
        resultado=resultado-5*x5
        x2=resultado//2
        resultado=resultado-2*x2
        x1=resultado//1
    return x20,x10,x5,x2,x1

print(rendre_monnaie(80, 2, 2, 2, 3, 3))

def somme(a=0,b=1):
    return a+b



def rac_eq_2nd_deg(a,b,c):
    delta = b**2-4*a*c
    if delta==0:
        x=(-b)/(2*a)
        tuple=(x,)
    elif delta<0:
        tuple=()
    else:
        x1=(-b+delta**(1/2))/(2*a)
        x2=(-b-delta**(1/2))/(2*a)
        tuple=(min(x1,x2),max(x1,x2))
    return tuple
print(rac_eq_2nd_deg(1.0,-4.0,4.0))



def catalan(n):
    x1=n
    x2=n+1
    x3=2*n

    def fatorial(x):
        resultado=1
        for i in range(1,x+1):
            resultado=resultado*i
        return resultado

    fatorial1=fatorial(x1)
    fatorial2=fatorial(x2)
    fatorial3=fatorial(x3)
    catalao=fatorial3/(fatorial1*fatorial2)
    return int(catalao)

print(catalan(0))

"""

def bat(joueur_1, joueur_2):
    if (joueur_1==0 and joueur_2==2) or (joueur_1==1 and joueur_2==0) or (joueur_1==2 and joueur_2==1):
        resposta = True
    else:
        resposta = False
    return resposta

print(bat(0,0))
