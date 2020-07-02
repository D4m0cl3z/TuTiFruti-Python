import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, letra, item, palabraUsuario, puntos, segundos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Tiempo restante: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL if segundos <5 else COLOR_TEXTO)
    ren3 = defaultFontMUYGRANDE.render(item, 1, COLOR_TEXTO)
    ren4 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_LETRA)

    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO//2-((len(item)//2)*TAMANO_LETRA_GRANDE), ALTO//2))
    screen.blit(ren4, (ANCHO//2-TAMANO_LETRA_GRANDE, 50))


def dibujarSalida(screen, letra, items, eleccionUsuario, eleccioncompu, puntos, segundos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Tiempo total: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL if segundos > 30 else COLOR_TEXTO)
    ren3 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_LETRA)


    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO//2-TAMANO_LETRA_GRANDE, 10))


    y=80
    for palabra in items:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_TEXTO), (10, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=80
    for palabra in eleccionUsuario:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRA), (ANCHO//2, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=80
    for palabra in eleccioncompu:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_LETRAS), (ANCHO-200, y))
        y=y+TAMANO_LETRA_GRANDE*2




