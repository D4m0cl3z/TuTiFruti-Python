from configuracion import *
from principal import *
import math
import random

def lectura(nomArch):
    nomArch=nomArch + ".txt"
    archivo=open(nomArch,"r", encoding='utf-8')
    salida=[]
    while(True):
        linea=archivo.readline().rstrip("\n")
        if not linea:
            break
        else:
            salida.append(linea.upper())
    archivo.close()
    return salida

def lectura2(nomArch):
    nomArch=nomArch + "-v2.txt"
    archivo=open(nomArch,"r", encoding='utf-8')
    salida=[]
    i=0
    while(True):
        linea=archivo.readline()
        if not linea:
            break
        else:
            salida.append([])
            salida[i].append(buscaPalabra(linea).upper())
            if buscaPuntaje(linea).upper()== "":
                salida[i].append(puntajeXLongitud(buscaPalabra(linea).upper()))
            else:
                salida[i].append(buscaPuntaje(linea).upper())
            i+=1
    archivo.close()
    return salida

def puntajeXLongitud(palabra):
    if (len(palabra) > 7):
        return 3;
    elif (len(palabra) > 5):
        return 2;
    else:
        return 1;
    return 0;

def buscaPalabra(linea):
    cadena=""
    for letra in linea:
        if letra == "#" or letra=="\n":
            break
        else:
            cadena+=letra
    return cadena

def buscaPuntaje(linea):
    cadena=""
    flag=0
    cadena=""
    for letra in linea:
        if letra == "#":
            flag=1
        elif flag==1 and letra != "\n":
            cadena+=letra
    return cadena

def unaAlAzar(lista): #hay que desarrollar.
    return random.choice(lista)

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo,jugadaCompu):
    palabraUsuario=palabraUsuario.upper()
    letra=letra.upper()
    aux=[]
    puntaje=[]
    for i in range(0, len(listaDeTodo[item])):
        aux.append(listaDeTodo[item][i][0])
        puntaje.append(listaDeTodo[item][i][1])

    if palabraUsuario != "" and palabraUsuario[0:1] == letra and palabraUsuario in aux:
        n=puntaje[aux.index(palabraUsuario)]
##aca se puede usar un moltiplicador o un +10 por ejemplo
        multiplicador=1
        if palabraUsuario == jugadaCompu[item]:
            multiplicador=2
        if n=="3":
            return 15*multiplicador
        elif n=="2":
            return 10*multiplicador
        else:
            return 5*multiplicador
    return 0

def juegaCompu(letraAzar, listaDeTodo):
    letraAzar=letraAzar.upper()
    salida=[]
    listaAux=[]
    aux=[]
    for i in range(0,len(listaDeTodo)):
        aux.clear()
        listaAux.clear()
        for j in range(0, len(listaDeTodo[i])):
            aux.append(listaDeTodo[i][j][0])
        for parabra in aux:
            if parabra[0:1] == letraAzar:
                listaAux.append(parabra)
        if not listaAux:
            salida.append("sinPalabrasEnBase")
        else:
            salida.append(random.choice(listaAux))
    return salida