import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Teste")
clock = pygame.time.Clock()
textFont = pygame.font.Font(None, 50)

textSurface = textFont.render("ta funcionando", False, 'White')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
	
    screen.blit(textSurface,(250,150))
    
    pygame.display.update()
    clock.tick(60)