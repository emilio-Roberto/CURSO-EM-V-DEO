#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Poze do Rodo.mp3')
pygame.music.play()
input()
pygame.event.wait()
#Corrigido