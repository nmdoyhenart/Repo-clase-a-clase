import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

# Tamaño de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

# Inicio Pygame
pygame.init() 

ventana_ppa1 = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Cuadro de texto")

fuente = pygame.font.SysFont("consolas", 20)

input = pygame.Rect(50,50,200,32)
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""


flag_run = True

while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    texto = ""
                else:
                    texto += evento.unicode
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                activo = not activo
            color = color_activo if activo else color_inactivo
            
    ventana_ppa1.fill(BLANCO)
    texto_superficie = fuente.render(texto, False, NEGRO)

    ventana_ppa1.blit(texto_superficie, (input.x + 5, input.y + 5))
    pygame.draw.rect(ventana_ppa1, color, input, 2)
    
    pygame.display.update()

pygame.quit()