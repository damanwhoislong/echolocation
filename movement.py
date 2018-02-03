import maze
import pygame
import time
import sys
import random
import math


def move_player(buttons, p_spd):
    global posX, posY, stepDelay
    direction = [0, 0]  # y, x

    # redoing dis shit, num[0] = x movement, num[1] = y movement
    if buttons[pygame.K_w]:
        direction[1] = - p_spd
    elif buttons[pygame.K_s]:
        direction[1] = p_spd
    if buttons[pygame.K_d]:
        direction[0] = p_spd
    elif buttons[pygame.K_a]:
        direction[0] = - p_spd

    # move da player
    if direction[0] and direction[1] != 0:
        posX += direction[1] * 0.7
        posY += direction[0] * 0.7
    else:
        posX += direction[1]
        posY += direction[0]

    if direction[0] != 0 or direction[1] != 0:
        stepDelay += -1

# set up pygame
pygame.mixer.pre_init(22050, -16, 4, 512)
pygame.mixer.init()
pygame.init()
pygame.font.init()
time.sleep(1)

# setup the screen and main clock
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("your title here")
clock = pygame.time.Clock()

# sounds
moveSound1 = pygame.mixer.Sound("sounds/step1.wav")
moveSound2 = pygame.mixer.Sound("sounds/step2.wav")
moveSound3 = pygame.mixer.Sound("sounds/step3.wav")
moveSound4 = pygame.mixer.Sound("sounds/step4.wav")

stepDelay = 30

# position X AND Y ARE SWAPPED KINDA
posX = 1.0
posY = 0.0

# coordinates of the walls
wallList = []
for i in range(len(maze.grid)):
    for j in range(len(maze.grid[i])):
        if maze.grid[i][j] == "W":
            wallList.append([i, j])

print(wallList)
# stats
moveSpeed = 1.0 / 60  # grid tiles per second / 60 frames per second

while True:
    # moving
    pressed = pygame.key.get_pressed()
    move_player(pressed, moveSpeed)
    posToGrid = [int(round(posX)), int(round(posY))]

    print(posToGrid)

    # play the movement sound
    if stepDelay <= 0:
        num = random.randint(1,4)
        if num == 1:
            moveSound1.play()
        if num == 2:
            moveSound2.play()
        if num == 3:
            moveSound3.play()
        if num == 4:
            moveSound4.play()
        stepDelay = 30

    # hit boxes
    if posToGrid in wallList:
        print("HITTING WALL")

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



