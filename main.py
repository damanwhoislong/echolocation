import pygame
import time
import random

size = 1

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

        levelFont = pygame.font.SysFont('Courier New', 20)  # font size and stuff
        levelText = levelFont.render("Press 1-4 to select level", True, (255, 255, 255))  # colour and the text that it displays
        text_rect2 = levelText.get_rect(center=(500 / 2, 200 + 500 / 2))  # centers the text


        screen.blit(titleText, text_rect)
        screen.blit(levelText, text_rect2)
        clock.tick(60)
        pygame.display.update()

        levelSelect = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                levelSelect = pygame.key.get_pressed()
                if levelSelect[pygame.K_2]:
                    size = 10
                elif levelSelect[pygame.K_3]:
                    size = 15
                elif levelSelect[pygame.K_4]:
                    size = 20
                else:
                    size = 6
                print(size)
                # GENERATE MAZE
                import maze
                import movement
                movement.run(size, maze.create_maze(size))

    pygame.quit()

game_intro()