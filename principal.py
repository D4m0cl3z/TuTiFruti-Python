#!/usr/bin/env python3

import math, os, random, sys
import time
import pygame
from pygame.locals import *
import datetime
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
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    items = ["colores","paises","animales","nombres","verduras","frutas"]

    ##se ingresan los archivos y se utiliza la funcion "leerArchivo()" para leer los .txt que se le ingresen
    colores = leerArchivo("colores.txt")
    paises = leerArchivo("paises.txt")
    animales = leerArchivo("animales.txt")
    nombres = leerArchivo("nombres.txt")
    frutas = leerArchivo("frutas.txt")
    verduras = leerArchivo("verduras.txt")

    listaDeTodo=[colores,paises,animales,nombres,verduras,frutas]
    letraAzar = unaAlAzar(abc)
    palabraUsuario = ""
    eleccionUsuario = []
    eleccionCompu = juegaCompu(letraAzar, listaDeTodo)

    # Cargo el sonido que suena por cada evento
    pygame.mixer.music.load('Sonido_POP.mp3')

    i = 0
    segaux = 0
    segpar = 0
    puntos = 0

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
                        segaux = segundostot
                        pygame.mixer.music.play()
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar = esCorrecta(palabraUsuario.lower(), letraAzar, listaDeTodo[i], i, letraAzar,eleccionCompu)
                        puntos += sumar
                        palabraUsuario = ""
                        i += 1

        # se usa un contador el cual si pasan 15 segundos sigue a la siguiente categoria
        segundostot = pygame.time.get_ticks() / 1000
        segpar = 15 - int(segundostot-segaux)
        if segpar == 0:
            pygame.mixer.music.play()
            segaux = segundostot
            eleccionUsuario.append("Tiempo vencido")
            i += 1

        # limpiar pantalla anterior
        fondo = pygame.image.load("fondoJuego.jpg")

        screen.blit(fondo,[-150,-22])

        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segpar)
        else:
            if puntos > 15:
                fondo = pygame.image.load("IMG1.jpg")
                pygame.mixer.music.load('Aplauso.mp3')
                pygame.mixer.music.play()
            else:
                fondo = pygame.image.load("IMG2.jpg")
            screen.blit(fondo,[-80,10])


            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundostot)

        pygame.display.flip()

    while True:

        for e in pygame.event.get():
            le = e.type
            if e.type == QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
