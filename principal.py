#!/usr/bin/env python3
#agregar seleccion o alta de un usuario
#ranking de puntos
#modos de juego
#punto por dificultad de palabra
#mas listas de cosas
#que se retroalimente, es decir q al finalizar el juego te muestre una pantalla para confirmar el agregado de palabras
#mas tardas, menos puntos. tipo un "jugas por"
#

import math, os, random, sys
import pygame
import time
import datetime
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    puntos = 0

    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ##items=["colores","paises","animales","nombres"]
    items=["colores","paises","animales"]
    ##colores= lectura("colores")
    ##paises= lectura("paises")
    ##animales= lectura("animales")
    ##nombres= lectura("nombres")

    paises2=lectura2("paises")
    animales2=lectura2("animales")
    colores2=lectura2("colores")
    listaDeTodo=[colores2,paises2,animales2]
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
    i=0
    auxTime=0
    now = datetime.datetime.now()
##    parcial=datetime.datetime.now()
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
                        now=datetime.datetime.now()
                        eleccionUsuario.append(palabraUsuario.upper())
                        sumar=esCorrecta(palabraUsuario, letraAzar, i, items, listaDeTodo,eleccionCompu)
                        puntos+=sumar
                        palabraUsuario=""
                        i=i+1
        segundostot = pygame.time.get_ticks() / 1000
        segundos=now.second - datetime.datetime.now().second + 15
        if segundos ==0:
            now=datetime.datetime.now()
            eleccionUsuario.append("")
            i=i+1

        # limpiar pantalla anterior
        screen.fill(COLOR_FONDO)
        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
        else:
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundostot)
        pygame.display.flip()

    while True:
        for e in pygame.event.get():
            le=e.type
            if e.type == QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
