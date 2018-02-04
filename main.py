import pygame
import time
import random

pygame.init()

def game_intro():
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("ECHOLOCATION")
    while True:
      ev = pygame.event.get()
      for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            import movement

game_intro()