import pygame
from pygame.locals import *

# Inicializa todos os módulos do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
