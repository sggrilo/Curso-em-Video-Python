# TOCANDO UM MP3 — Faça um programa em Python que abra e reproduza áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
input('')
pygame.event.wait()

# import playsound
# playsound.playsound('')
