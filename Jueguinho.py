import pygame
pygame.init()

L = 900
A = 600
screen = pygame.display.set_mode((L, A))
icono = pygame.image.load('images/ic_per.png') # Variable 'icono' cargando imagen
pygame.display.set_icon(icono) # Icono
pygame.display.set_caption('Dajji') # Titulo

correr = True
while correr:
    # Cerrar programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False

