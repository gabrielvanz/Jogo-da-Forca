import pygame
pygame.init()

TELA_LARGURA=int(800)
TELA_ALTURA= int ( TELA_LARGURA*0.8)

tela= pygame.display.set_mode(TELA_ALTURA,TELA_LARGURA)
pygame.display.set_caption("Jooj em pygame")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit