import maze
import pygame
import time
import sys


def move_player(buttons, p_spd):
    global posX, posY
    direction = [0, 0]

    # redoing dis shit, num[0] = x movement, num[1] = y movement
    if buttons[pygame.K_w]:
        direction[0] = - p_spd
    elif buttons[pygame.K_s]:
        direction[0] = p_spd
    if buttons[pygame.K_d]:
        direction[1] = p_spd
    elif buttons[pygame.K_a]:
        direction[1] = - p_spd

    # move da player
    if num[0] and num[1] != 0:
        posX += direction[1] * 0.7
        posY += direction[0] * 0.7
    else:
        posX += direction[1]
        posY += direction[0]



pygame.mixer.pre_init(22050, -16, 6, 512)
pygame.mixer.init()
pygame.init()
pygame.font.init()
time.sleep(1)

# setup the screen and main clock
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("your title here")
clock = pygame.time.Clock()



# note: maze x and y are flipped, player starts at 1,0 and not 0, 1
# player starts at [1, 0]

posX = 1.0
posY = 0.0

moveSpeed = 1.0 / 60  # grid tiles / sec
num = [0, 0]



while True:
    pressed = pygame.key.get_pressed()
    move_player(pressed, moveSpeed)
    print("x:", posX, "y:", posY)

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



