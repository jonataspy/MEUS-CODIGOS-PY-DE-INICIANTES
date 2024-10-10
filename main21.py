#importar pygame
import pygame 

#iniçiar pygame
pygame.init()

#iniçiando o pygame
pygame.mixer.music.load("xex.mp3")
pygame.mixer.music.play()
input()

#termino do programa e print 
pygame.event.wait()
print('programa rodando ')
