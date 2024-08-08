#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Ex_021.mp3')

print(f'\n{'- A seguir uma bela canção -':^33}\n')

pygame.mixer.music.play()
input()
pygame.event.wait()
