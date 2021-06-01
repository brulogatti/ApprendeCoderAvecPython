"""
def signature(identite):
    resultat=""
    for x in range((len(identite)-1),-1,-1):
        if x!=len(identite)-1:
            resultat = resultat + identite[x]
        else:
            resultat = resultat + identite[x] + " "
    return resultat

print(signature(('de Saint-Exupéry', 'Antoine')))
"""
"""
def est_adn(adn):
    resultado = False
    if adn=="":
        resultado=False
    else:
        cont = 0
        for x in range(len(adn)):
            if(adn[x]=="A" or adn[x]=="T" or adn[x]=="C" or adn[x]=="G"):
                cont=cont+1
        if cont==len(adn):
            resultado = True
        else:
            resultado = False
    return resultado

print(est_adn(""))
"""
"""
def duree(duration1,duration2):
    heures=0
    minutes=0
    inicial=duration1[0]*60+duration1[1]
    final=duration2[0]*60+duration2[1]
    if(duration2[0]>duration1[0]):
        resultado = final - inicial
        heures=resultado//60
        minutes=resultado-heures*60
    else:
        resultado = (final+24*60)-inicial
        heures = resultado//60
        minutes=resultado-60*heures
    return (heures,minutes)


print(duree((6, 0), (5, 15)))

"""
"""
def distance_points(coordenade1, coordenade2):
    distance = (((coordenade1[0]-coordenade2[0])**2)+((coordenade1[1]-coordenade2[1])**2))**(1/2)
    return distance

print(distance_points((-1.0, 0.5), (2.0, 1.0)))
"""
"""
def longueur(*points):
    valoresx=[]
    valoresy=[]
    resultado=0
    for x,y in points:
        valoresx=[x]+valoresx
        valoresy=[y]+valoresy
    for i in range(len(valoresy)-1):
        operacao=((valoresx[i+1]-valoresx[i])**2 + (valoresy[i+1]-valoresy[i])**2)**(1/2)
        resultado = resultado+operacao
    return resultado

print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))
"""
"""
def transcription_arn(brin_codant):
    cont=0
    for c in brin_codant:
        cont=cont+1
        if(brin_codant[cont-1]=="T"):
            brin_codant = brin_codant[0:cont-1] + "U" + brin_codant[(cont):len(brin_codant)]
    return brin_codant


print(transcription_arn('TGTCTTACCGATCCAT'))
"""
"""
def prime_numbers(n):
    if type(n)!=int:
        resultado=None
    elif(int(n)>0):
        cont=0
        numero = 1
        resultado=[]
        while(cont<int(n)):
            numero=numero+1
            contprimo=0
            for i in range(1,numero+1):
                if(numero%i==0):
                    contprimo=contprimo+1
            if (contprimo==2):
                cont=cont+1
                resultado.append(numero)
    elif int(n)==0:
        resultado=[]
    elif int(n)<0:
        resultado = None
    return resultado

print(prime_numbers("T"))
"""
"""
def plus_grand_bord(w):
    anterior = 0
    coleta=[]
    contador=0
    maior=0
    if w[0]!=w[len(w)-1]:
        resultado=[]
    else:
        for i in range(0, len(w)-1):
            if w[i]==w[0]:
                coleta.append(w[anterior:(i+1)])
                anterior=i
                contador=contador+1
    for j in range(len(coleta)):
        if(len(coleta[j])>maior):
            maior=j
    resultado=coleta[maior]
    if(contador+1==len(w)):
        resultado=(len(w)-1)*w[0]
    return resultado

print(plus_grand_bord('aaaaa'))

def plus_grand_bord(w):
   for i in range(len(w)//2, -1, -1):
      if w[:i] == w[-i:]:
          print(w[:i])
          break
   print(i)
   return w[:i]

print(plus_grand_bord('abdabda'))

"""

def plus_grand_bord(w):
   for i in range(1, len(w)):
      if w[:i] == w[-i:]:
          print(w[:i])
          break
   print(i)
   return w[:i]

print(plus_grand_bord('abdabda'))
