import pygame
pygame.mixer.init()
pygame.mixer.music.load('matheusinho_fofinho.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar a musica... \n\n')

'''Outra forma de fazer: '''

pygame.init()
pygame.mixer.music.load('matheusinho_fofinho.mp3')
pygame.mixer.music.play()
pygame.event.wait()