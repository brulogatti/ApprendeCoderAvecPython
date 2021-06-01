"""
def anagrammes (v,w):
    resultado = False
    lettre1=[]
    lettre2=[]
    for i in range(0,len(v)):
        lettre1.append(v[i])
    for j in range(0,len(w)):
        lettre2.append(w[j])
    lettre1.sort()
    lettre2.sort()
    if lettre1==lettre2:
        resultado = True
    else:
        resultado=False
    return resultado

print(anagrammes('marion', 'romina'))
"""
"""
def dupliques(elemento):
    resultado=False
    contador=0
    thing=[]
    for i in range(0,len(elemento)):
        thing.append(elemento[i])
    thing.sort()
    print(thing)
    for j in range(0,len(thing)):
        for k in range(0,len(thing)):
            if contador>len(thing):
                resultado=True
                #break
            if thing[k]==thing[j]:
                contador=contador+1
    return resultado

print(dupliques('abcda'))

"""
"""
def intersection(v,w):
    mot1=[]
    mot2=[]
    resultado=""
    for i in range(0,len(v)):
        mot1.append(v[i])
    for j in range(0,len(w)):
        mot2.append(w[j])
    print(mot1)
    print(mot2)
    for i in range(len(mot1)):
        if mot1[i] in mot2:
            inicio=0
            flag=0
            while flag==0:
                if mot1[i]==mot2[inicio]:
                    inicio1=i
                    flag=1
                else:
                    inicio=inicio+1
            fim=inicio
            fim1=inicio1
            contador=0
            print(inicio, inicio1)
            while mot1[i+contador]==mot2[inicio+contador]:
                contador=contador+1
                if mot1[i+contador]==mot2[inicio+contador]:
                    fim=inicio+contador
                    fim1=inicio1+contador
    if mot1[inicio1]==mot2[inicio]:
        for i in range(inicio1,fim1+1):
            resultado=resultado+mot1[inicio1]
    return resultado



print(intersection('programme', 'grammaire'))
"""
"""
def distance_mots(mot_1,mot_2):
    resultado=None
    if(len(mot_1)!=len(mot_2)):
        resultado=None
    else:
        contador=0
        mot1 = []
        mot2 = []
        for i in range(0, len(mot_1)):
            mot1.append(mot_1[i])
        for j in range(0, len(mot_2)):
            mot2.append(mot_2[j])
        for k in range(0,len(mot1)):
            if (mot1[k]!=mot2[k]):
                contador=contador+1
        resultado = contador
    return resultado

print(distance_mots("Python", "Python"))
"""
"""
def correcteur(mot, liste_mots):
    resultado=""
    similar=[]
    for i in range(0,len(liste_mots)):
        if len(mot)==len(liste_mots[i]):
            contador=0
            palavra=liste_mots[i]
            for k in range(0, len(mot)):
                if (mot[k] == palavra[k]):
                    contador = contador + 1
            similar.insert(i,contador)
        else:
            similar.insert(i,0)
    maior=similar[0]
    for z in range(len(similar)):
        if similar[z]>maior:
            posicao=z
            maior=similar[z]
    resultado=liste_mots[posicao]
    return resultado

print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
"""
"""
def my_insert(numeros,nombre):
    resultado=[]
    if type(nombre)!=int:
        resultado = None
    else:
        if nombre>numeros[len(numeros)-1]:
            posicao=len(numeros)
            resultado[0:posicao + 1] = numeros[0:posicao + 1]
            resultado.append(nombre)
        elif(nombre<=numeros[0]):
            posicao=0
            resultado.append(nombre)
            resultado[posicao + 1:] = numeros[posicao:len(numeros)]
        else:
            posicao=0
            for i in range(len(numeros)):
                if nombre >= numeros[i]:
                    print(numeros[i])
                    if i != len(numeros):
                        print(numeros[i])
                        if nombre <= numeros[i + 1]:
                            print(numeros[i])
                            posicao = i
            resultado[0:posicao + 1] = numeros[0:posicao + 1]
            resultado.append(nombre)
            resultado[posicao + 2:] = numeros[posicao + 1:len(numeros)]
    return resultado
"""

"""
while contador!=posicao+1:
    resultado.append(numeros[contador])
    contador=contador+1
    resultado.append(nombre)
    contador2 = contador
    contador=contador+1
    while contador<(len(numeros)+1):
        resultado.append(numeros[contador2])
        contador2=contador2+1
        contador=contador+1
        """
"""
def my_insert(numeros,nombre):
    resultado=[]
    assert type(nombre)==int

    if nombre>numeros[len(numeros)-1]:
        posicao=len(numeros)
        resultado[0:posicao + 1] = numeros[0:posicao + 1]
        resultado.append(nombre)
    elif(nombre<=numeros[0]):
        posicao=0
        resultado.append(nombre)
        resultado[posicao + 1:] = numeros[posicao:len(numeros)]
    else:
        posicao=0
        for i in range(len(numeros)):
            if nombre >= numeros[i]:
                if i != len(numeros):
                    if nombre <= numeros[i + 1]:
                        posicao = i
        resultado[0:posicao + 1] = numeros[0:posicao + 1]
        resultado.append(nombre)
        resultado[posicao + 2:] = numeros[posicao + 1:len(numeros)]
    for i in range(len(numeros)):
        numeros.pop()
    for j in range(len(resultado)):
        numeros.insert(j,resultado[j])
    return None

"""
"""
while contador!=posicao+1:
    resultado.append(numeros[contador])
    contador=contador+1
    resultado.append(nombre)
    contador2 = contador
    contador=contador+1
    while contador<(len(numeros)+1):
        resultado.append(numeros[contador2])
        contador2=contador2+1
        contador=contador+1
        """
'''
def my_pow(m,b):
    if type(m)==int and type(b)==float:
        fatorial=[]
        for x in range(0,m):
            fatorial.append(b**x)
        return fatorial
    else:
        return None


print(my_pow(1, 4))
'''
'''
def decompresse(lista):
    resultado=[]
    tamanho=len(lista)
    for i in range(0,tamanho):
        if(lista[i][0]!=0):
            contador=int(lista[i][0])
            for j in range(contador):
                resultado.append(lista[i][1])
    return resultado

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
'''
'''

def my_filter(lst, f):
    resultado=[]
    tamanho=len(lst)
    for i in range(tamanho):
        if(f(lst[i])==True):
            resultado.append(lst[i])
    return resultado

print(

my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)

)
'''




