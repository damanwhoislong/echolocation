import maze
import pygame
import time
import sys
import random
import math
import qwer


def move_player(buttons, p_spd, ang, walls, siz):
    global posX, posY, stepDelay
    direction = [0, 0]  # y, x

    velX = math.cos(ang * 1) / 60
    velY = math.sin(ang * 1) / 60

    newX = posX + velX
    newY = posY + velY
    grid_position = [int(round(newX)), int(round(newY))]
    if grid_position in wallList or grid_position[0] < 0 or grid_position[0] >= siz or grid_position[1] < 0 or grid_position[1] >= siz:
        pass
    else:
        posX += velX
        posY += velY

    stepDelay += -1


# set up pygame
pygame.mixer.pre_init(22050, -16, 4, 512)
pygame.mixer.init()
pygame.init()
pygame.font.init()
time.sleep(1)

# setup the screen and main clock
screen = pygame.display.set_mode((500, 500))
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
    # get da angle
    angle = qwer.get_angle()

    pygame.draw.circle(screen, (255, 0, 0), (int(posY * (500/maze.size)), int(posX * (500/maze.size))), 4)

    # moving
    pressed = pygame.key.get_pressed()
    move_player(pressed, moveSpeed, angle, wallList, maze.size)
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
        stepDelay = 20

    # hit boxes
    if posToGrid == [8, 9]:
        print("YOU WIN")

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            qwer.stahp()
            sys.exit()



qwer.stahp()

