from configuracion import *
from principal import *
import math
import random


#Elige una letra al azar gracias a la funcion ramdom.choice y se le pasa todo el abc
def unaAlAzar(lista):
  return random.choice(lista)


#se utiliza booleanos para comparar si la palabra que se ingresó corresponde a una palabra de la categoria situada en el evento actual
def CategoriaCorrecta(palabraUsuario, palabrasDeCategoria):
    return palabraUsuario in palabrasDeCategoria

def letraCorrecta(letra, palabraUsuario):
    return letra == palabraUsuario[0]

def esPalabraCorrecta(palabraUsuario, letra, listaDeTodo):
    return CategoriaCorrecta(palabraUsuario, listaDeTodo) and letraCorrecta(letra, palabraUsuario)

def esCorrecta(palabraUsuario, letra, listaDeTodo):
    return 10 if esPalabraCorrecta(palabraUsuario, letra, listaDeTodo) else 0


#se utiliza la letra al  azar y las listas de las categorias para hacer que la maquina regrese una palabra corresponiente con la letra elegida,
#la palabra que regresa es aleatoria
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


#lee los archivos para generar las listas
def leerArchivo(archivo):
    archivo_txt = open(archivo, "r")
    listaCategoria = archivo_txt.readlines()
    listaCategoriaCorregida = borrarSobra(listaCategoria)
    archivo_txt.close()
    return listaCategoriaCorregida

#gracias al uso del strip se va eliminando el sobrante "\n" para mejorar la lista
def borrarSobra(lista):
    listaCategoria = []
    for i in range(0, len(lista)):
        listaCategoria.append(lista[i].strip("\n"))
    return listaCategoria


