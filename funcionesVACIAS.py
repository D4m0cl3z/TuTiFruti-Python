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
    if palabraUsuario == sacaTildes(PalabraCompu):
        multiplicador = 2

    if (palabraPunto >= 8 ):
        return 15 * multiplicador
    elif (palabraPunto >= 5):
        return 10 * multiplicador
    else:
        return 5 * multiplicador


def sumaPuntosCompu(eleccionCompu):
    puntos=0
    for palabra in eleccionCompu:
        if palabra != NONEPBASE and palabra != NLLEGUE:
            puntos+=Puntos(palabra,VACIO)
    return puntos


#se utiliza la letra al  azar y las listas de las categorias para hacer que la maquina regrese una palabra corresponiente con la letra elegida,
def juegaCompu(letraAzar, listaDeTodo):
    listaCompu = []
    for categoria in listaDeTodo:
        palabrasCorrectas =  [sacaTildes(palabra) for palabra in categoria if palabra[0] == letraAzar]
        if palabrasCorrectas:
            posiblePalabra = random.choice(palabrasCorrectas)
        else:
            posiblePalabra = NONEPBASE          
        listaCompu.append(randomCompu(posiblePalabra))
    return listaCompu

#la palabra que regresa es aleatoria y la maquina tiene un 33,33 de posibilidad de fallar
def randomCompu(cadena):
    if 1 == random.randint(1, 5):
        return NLLEGUE
    return cadena

#lee los archivos para generar las listas que posteriormente se van a utilizar para saber si las respuestas del usuario son correctas
def leerArchivo(archivo):
    archivo_txt = open(archivo, "r", encoding='utf-8')
    listaCategoria = archivo_txt.readlines()
    listaCategoriaCorregida = borrarSobra(listaCategoria)
    listaCategoriaCorregida = [sacaTildes(palabra.lower()) for palabra in listaCategoriaCorregida]
    return listaCategoriaCorregida

#gracias al uso del strip se va eliminando el sobrante "\n" para mejorar la lista
def borrarSobra(lista):
    listaCategoria = []
    for i in range(0, len(lista)):
        listaCategoria.append(lista[i].strip("\n"))
    return listaCategoria

def sacaTildes(cadena):
    vocalesConTildes=["á","é","í","ó","ú","ñ","Á","É","Í","Ó","Ú","Ñ"]
    vocalesSinTildes=["a","e","i","o","u","n","A","E","I","O","U","N"]
    salida=""
    for letra in cadena:
        if letra in vocalesConTildes:
            salida += vocalesSinTildes[vocalesConTildes.index(letra)]
        else:
            salida +=letra
    return salida

def presentacion(screen, pg):
    fondo = pygame.image.load("pcarga.jpg")

    presentacion = True
    while presentacion == True:
        screen.blit(fondo,[-80,-80])
        pg.display.flip()
        time.sleep(3)
        presentacion = False



# def presentacion(screen, pg):
#     fondo = pygame.image.load("pcarga.jpg")
#     i=0
#     presentacion = True
#     cargaText = "Cargando"

#     while presentacion == True :
#         screen.blit(fondo,[-100,-100])
#         pg.display.flip()
#         dibujoText = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE).render(cargaText, 1, COLOR_ROJO)
#         screen.blit(dibujoText , (-10, -10))
#         time.sleep(1)
#         i+=1
#         if i == 4:
#             cargaText+= " . "   
#             presentacion = False