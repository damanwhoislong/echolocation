import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

def game_intro():
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("ECHOLOCATION")
    while True:
        titleFont = pygame.font.SysFont('Helvetica', 40)  # font size and stuff
        titleText = titleFont.render("BIING", True, (50, 255, 50))  # colour and the text that it displays
        text_rect = titleText.get_rect(center=(500 / 2, 500 / 2))  # centers the text

        screen.blit(titleText, text_rect)
        pygame.display.update()
        clock.tick(60)
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                import movement

game_intro()