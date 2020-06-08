#!/usr/bin/env python3

import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #fondo del juego


    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    puntos = 0
    candidata = ""

    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    items=["colores","paises","animales","nombres","verduras","frutas"]

##  #se ingresan los archivos y se utiliza la funcion "leerArchivo()" para leer los .txt que se le ingresen

    colores = leerArchivo("colores.txt")
    paises = leerArchivo("paises.txt")
    animales = leerArchivo("animales.txt")
    nombres = leerArchivo("nombres.txt")
    frutas = leerArchivo("frutas.txt")
    verduras = leerArchivo("verduras.txt")

    listaDeTodo=[colores,paises,animales,nombres,verduras,frutas]
    print(colores)
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]

##Cargo sonido
    pygame.mixer.music.load('Sonido_POP.mp3')



    i=0
    while i < len(items):


        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        fps = 3

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        pygame.mixer.music.play()
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, letraAzar, listaDeTodo[i])
                        puntos+=sumar
                        palabraUsuario=""
                        i=i+1

        segundos = pygame.time.get_ticks() / 1000

        # limpiar pantalla anterior
        fondo = pygame.image.load("fondoJuego.jpg")

        screen.blit(fondo,[-150,-22])

        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
        else:
            pygame.mixer.music.load('Aplauso.mp3')
            pygame.mixer.music.play()
            eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundos)
        pygame.display.flip()



    while True:


        for e in pygame.event.get():

            if e.type == QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
