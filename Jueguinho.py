import pygame,sys
pygame.init()

# Colores

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 255)
BLUE = (0,0,255)

size = (300, 300)

# crear pantalla

screen = pygame.display.set_mode(size)

cord_x = 200
cord_y = 200

speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    # Color 
    screen.fill(RED)
    # Actualizar pantalla
    pygame.draw.aaline(screen,BLACK,[0,0],[400,400],5)
    pygame.draw.rect(screen,BLUE,(200,200,40,80))
    pygame.draw.circle(screen,BLACK,(100,100),50)

    pygame.display.flip()

