from configuracion import *
from principal import *
import math
import random

def unaAlAzar(lista): #hay que desarrollar.
  return random.choice(lista)

def CategoriaCorrecta(palabraUsuario, palabrasDeCategoria):
    return palabraUsuario in palabrasDeCategoria

def letraCorrecta(letra, palabraUsuario):
    return letra == palabraUsuario[0]

def esPalabraCorrecta(palabraUsuario, letra, listaDeTodo):
    return CategoriaCorrecta(palabraUsuario, listaDeTodo) and letraCorrecta(letra, palabraUsuario)

def esCorrecta(palabraUsuario, letra, listaDeTodo):
    return 10 if esPalabraCorrecta(palabraUsuario, letra, listaDeTodo) else 0


def juegaCompu(letraAzar, listaDeTodo):
    listaAux= []
    listaCompu=[]
    for i in range (0, len(listaDeTodo)):
        del listaAux[:]
        for palabra in listaDeTodo[i]:
            if letraAzar == palabra[0]:
                listaAux.append(palabra)
        if not listaAux:
            listaAux.append("Palabra no encontada")
        listaCompu.append(random.choice(listaAux))
    return listaCompu

