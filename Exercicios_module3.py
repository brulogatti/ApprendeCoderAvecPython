'''
a=int(input())
b=int(input())
c=int(input())
if a==b:
    print(a)
elif a==c:
    print(a)
elif b==c:
    print(b)


temperature=int(input())
if temperature>0:
    if temperature<=10:
        print("Il va faire frais.")
else:
    print("Il va faire froid.")

a=int(input())
b=int(input())
c=int(input())
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a**2+a*b)
else:
    print("Erreur")


nombre=int(input())
if nombre%2==0:
    print(True)
else:
    print(False)



a=int(input())
b=int(input())
if a%b==0:
    print(False)
elif b%a==0:
    print(False)
else:
    print(True)



a=float(input())
b=float(input())
if a<0:
    print("Erreur")
elif b<0:
    print("Erreur")
else:
    print((a*b)**0.5)



nombre1=int(input())
nombre2=int(input())
if nombre1==nombre2:
    print(12*10)
elif nombre2==0:
    if nombre1==13:
        print(2*10)
    else:
        print(0)
elif nombre2%2==0:
    if nombre2==12:
        if nombre1==15:
            print(2*10)
        else:
            print(0)
    elif nombre1==13 or nombre1==16:
        print(2*10)
    else:
        print (0)
else:
    if nombre2==11:
        if nombre1==16:
            print(2*10)
        else:
            print(0)
    elif nombre1==14 or nombre1==15:
        print(2*10)
    else:
        print(0)

lettre=input()
a=float(input())
cube = a**3
if lettre=="T":
    print(((2**0.5)/12)*cube)
elif lettre=="C":
    print(cube)
elif lettre=="O":
    print(((2**0.5)/3)*cube)
elif lettre=="D":
    print(((15+(7*(5**0.5)))/4)*cube)
elif lettre=="I":
    print(((15+(5*(5**0.5)))/12)*cube)
else:
    print("Polyèdre non connu")


n = int(input('valeur du nombre n dont on veut tester la conjecture'))
while n != 1:
    print(n)
    if n % 2 == 0 :
        n = n // 2
    else:
        n = 3*n + 1
print(n)



import turtle
n = int(input())
for i in range(n):
   turtle.forward(100)
   turtle.left(360/n)
turtle.done()



import turtle
n = int(input())
for i in range(n):
    turtle.forward(100)
    turtle.left(((n-1)*180)/n)
turtle.done()



import turtle
from math import gcd # fonction du module math qui calcule le pgcd de 2 nombres

LONGUEUR = 100 # taille de chaque segment de l'étoile

n = int(input("Combien de branches désirez-vous ? :"))
inc = (n-1) // 2
while gcd(n, inc) > 1:
   inc = inc - 1
if inc == 1 :
   print("Impossible de dessiner une étoile à", n, "branches en un tenant")
else:
   angle =  180 - (n - 2 * inc) * 180 / n
   for i in range(n):
       turtle.forward(LONGUEUR)
       turtle.left(angle)
   turtle.done()

for x in range(5):
    for y in range(4):
        print(x, y)


import turtle
for i in range(3):  # à chaque itération, trace un losange
   angle = 120
   for j in range(4): # à chaque itération, trace un segment
       turtle.forward(100)
       turtle.left(angle)
       angle = 180 - angle
   turtle.right(120)
turtle.hideturtle()
turtle.done()


DISTANCE = 3844.0e5
nombre_pliages = 0
epaisseur = 0.0001
while epaisseur < DISTANCE :
   epaisseur = 2 * epaisseur
   nombre_pliages = nombre_pliages + 1
response = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while response!=nombre_pliages:
    print("Mauvaise réponse.")
    response = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo !")


flag=False
cont=0
soma=0
while flag==False:
    numero=float(input())
    if(numero==-1):
        flag=True
    else:
        soma=numero+soma
        cont=cont+1
print(soma/cont)


nombre=int(input())
lado=nombre
espaco=0
for i in range(nombre):
    print(espaco*" " + lado*"X", end="\n")
    lado=lado-1
    espaco=espaco+1



cont=int(input())
soma=0
flag=0
if cont>=0:
    for i in range(cont):
        numero=int(input())
        soma=soma+numero
    print(soma)
else:
    while flag!=1:
        entrada=input()
        if entrada=="F":
            print(soma)
            flag =1
        else:
            numero = int(entrada)
            soma=soma+numero



import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
chance=1
flag=0
nombre=int(input())
while chance<=NB_ESSAIS_MAX and flag==0:
    if nombre==secret:
        print("Gagné en", chance, "essai(s) !")
        flag=1
    elif nombre>secret and chance!=6:
        print("Trop grand")
        nombre=int(input())
        chance=chance+1
    elif nombre<secret and chance!=6:
        print("Trop petit")
        nombre=int(input())
        chance=chance+1
    else:
        chance=chance+1
if flag==0:
    print("Perdu ! Le secret était", secret)


saut=int(input())
position_cible=int(input())
position_courante=0
flag=0
proxima = 0
while position_courante!=position_cible and flag==0:
    proxima = position_courante + saut
    if proxima<100 and proxima!=0:
        position_courante=proxima
        if(position_courante!=position_cible):
            print(position_courante)
    elif proxima>100:
        position_courante=proxima-100
        if position_courante!=0 and position_courante!=position_cible:
            print(position_courante)
        elif position_courante==position_cible:
            flag=0
        else:
            flag=1
    else:
        flag=1
if flag==0:
    print("Cible atteinte")
else:
    print(0)
    print("Pas trouvée")



n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j, end = " ")
    print()



sin=float(input())
resultado = sin
sub=3
soma=5
flag=0
operacao=0
fatorial=1
modulo=0
while flag==0:
    for i in range(1,sub+1):
        fatorial = fatorial*i
    operacao=(sin**sub)/fatorial
    if operacao<0:
        modulo=operacao*(-1)
    else:
        modulo = operacao
    if modulo<10e-6:
        flag=1
    resultado = resultado - operacao
    fatorial=1
    sub = sub + 4
    for j in range(1,soma+1):
        fatorial=fatorial*j
    operacao=(sin**soma)/fatorial
    if operacao<0:
        modulo=operacao*(-1)
    else:
        modulo=operacao
    if modulo<10e-6:
        flag=1
    resultado = resultado + operacao
    fatorial = 1
    soma = soma+4
print(resultado)

'''
tamanho=int(input())
CONTADOR1=1
contador2=1
contador3=0
numero=0
flag=0

while flag==0:
    numero=contador2
    contador3 = contador3 + 1
    if contador2<CONTADOR1:
        for i in range(contador2,CONTADOR1+1):
            print(numero, end = "")
            if numero+1<10:
                numero = numero+1
            else:
                numero = 0
        numero = CONTADOR1
        for i in range(contador2+1, CONTADOR1+1):
            if numero - 1 > 0:
                numero = numero - 1
            else:
                numero = 0
            print(numero, end="")
        print()
    else:
        for i in range(contador2,CONTADOR1+1):
            print(numero, end = "")
            if numero+1<10:
                numero = numero+1
            else:
                numero = 0
        numero = CONTADOR1
        for i in range(contador2+1, CONTADOR1+1):
            if numero - 1 > 0:
                numero = numero - 1
            else:
                numero = 0
            print(numero, end="")
        print()
    if CONTADOR1+2<10:
        CONTADOR1=CONTADOR1+2
    else:
        CONTADOR1=CONTADOR1-8
    if contador2+1<10:
        contador2=contador2+1
    else:
        contador2=0
    if contador3==tamanho:
        flag=1#Terminar, exercício 3.18