import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init() # Inicio juego

ventana = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Primer programa Pygame")

icono = pygame.image.load("utn_icono.jpg")
pygame.display.set_icon(icono)

gatito = pygame.image.load("gatito.jpeg")
#gatito = pygame.transform.scale(gatito, DIMENSION_VENTANA)
gatito = pygame.transform.scale(gatito, (100,100))

gatito_rectangulo = gatito.get_rect()
#gatito_rectangulo.topleft = (50,50)
gatito_rectangulo.x = 50
gatito_rectangulo.y = 50

fuente = pygame.font.SysFont("consolas", 20)
texto = fuente.render("Anashe miau", False, ROJO, VERDE)

bandera = True
bandera_mensaje = False

while bandera:
    for evento in pygame.event.get():   
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if gatito_rectangulo.collidepoint(evento.pos):
                bandera_mensaje = True
            
    ventana.fill(AZUL_CLARO)

    #ventana.blit(gatito,(0,0))
    ventana.blit(gatito, gatito_rectangulo)
    
    if bandera_mensaje == True:
        ventana.blit(texto, (100,100))
    


    pygame.display.update()



pygame.quit() # Fin juego