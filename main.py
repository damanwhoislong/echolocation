import pygame
import time
import random



def game_intro():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("ECHOLOCATION")

    while True:
        screen.fill((0, 0, 0))
        logo = pygame.image.load("logo4.png")

        screen.blit(logo,(250-84,30))
        titleFont = pygame.font.SysFont('Courier New', 40)  # font size and stuff
        titleText = titleFont.render("P  i  !  N  G", True, (255, 255, 255))  # colour and the text that it displays
        text_rect = titleText.get_rect(center=(500 / 2, 500 / 2))  # centers the text

        screen.blit(titleText, text_rect)
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                import movement

    pygame.quit()

game_intro()