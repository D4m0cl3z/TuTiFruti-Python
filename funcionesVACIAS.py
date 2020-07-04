from configuracion import *
from principal import *
import math
import random

#Elige una letra al azar gracias a la funcion ramdom.choice
def unaAlAzar(lista):
  return random.choice(lista)

#Devuelve booleanos para comparar si la palabra que se ingresó corresponde a una palabra de la categoria situada en el evento actual
def CategoriaCorrecta(palabraUsuario, palabrasDeCategoria):
    return palabraUsuario in palabrasDeCategoria

def letraCorrecta(letra, palabraUsuario):
    return letra == palabraUsuario[0]

def esPalabraCorrecta(palabraUsuario, letra, listaDeTodo):
    return CategoriaCorrecta(palabraUsuario, listaDeTodo) and letraCorrecta(letra, palabraUsuario)

def esCorrecta(palabraUsuario, letra, listaDeTodo, stage, letraAzar,eleccionCompu):
    return Puntos(palabraUsuario, eleccionCompu[stage]) if esPalabraCorrecta(palabraUsuario, letra, listaDeTodo) else 0

#dependiendo de la longitud de la palabra se modifica cantidad de puntos y si la compu elige la misma palabra el puntaje se multiplica por 2
def Puntos(palabraUsuario, PalabraCompu):
    multiplicador = 1
    palabraPunto = len(palabraUsuario)

    if palabraUsuario == PalabraCompu:
        multiplicador = 2

    if (palabraPunto >= 8 ):
        return 15 * multiplicador
    elif (palabraPunto >= 5):
        return 10 * multiplicador
    else:
        return 5 * multiplicador

#se utiliza la letra al  azar y las listas de las categorias para hacer que la maquina regrese una palabra corresponiente con la letra elegida,
def juegaCompu(letraAzar, listaDeTodo):
    listaCompu = []
    for categoria in listaDeTodo:
        palabrasCorrectas =  [palabra for palabra in categoria if palabra[0] == letraAzar]
        if palabrasCorrectas:
            posiblePalabra = random.choice(palabrasCorrectas)
        else:
            posiblePalabra = "Palabra no encontrada"           
        listaCompu.append(randomCompu(posiblePalabra))
    return listaCompu

#la palabra que regresa es aleatoria y la maquina tiene un 33,33 de posibilidad de fallar
def randomCompu(cadena):
    if 1 == random.randint(1, 10):
        return "No llegué"
    return cadena

#lee los archivos para generar las listas que posteriormente se van a utilizar para saber si las respuestas del usuario son correctas
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
