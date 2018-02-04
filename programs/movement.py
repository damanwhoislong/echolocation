# Movement.py
# Purpose: Provides movement functionality for the user.

'''
ingameMusic = pygame.mixer.Sound('sounds/background music.wav')
pygame.mixer.set_num_channels(10)
channel0 = pygame.mixer.Channel(0)
channel0.play(ingameMusic, loops=-1)
'''

import math
import maze
import pygame
import random
import sys
import time


import connect_myo


def move_player(buttons, p_spd, ang, walls, siz):
    global posX, posY, stepDelay, angle, initial_calibration

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

        fullDiagonal = math.sqrt((siz)**2 + siz**2)
        curDiagonal = math.sqrt((siz-posX)**2 + ((siz-1)-posY)**2)
        minDistFinishRatio = curDiagonal/fullDiagonal
        avg_loudness = (1.1 - minDistFinishRatio) / 3.5

        Ux = posY
        Dx = siz - 2
        Uy = siz - posX
        Dy = 2
        Uangle = angle * 180 / math.pi - 90

        if Dx == Ux:
            Dx += 0.001
        dest_bearing = math.atan((Dy - Uy) / (Dx - Ux)) * 180 / math.pi
        # print(Ux, Dx, Uy, Dy, dest_bearing, angle * 180 / math.pi)

        stepDelay += -1


def do_music(siz):
    global angle
    fullDiagonal = math.sqrt((siz) ** 2 + siz ** 2)
    curDiagonal = math.sqrt((siz - posX) ** 2 + ((siz - 1) - posY) ** 2)
    minDistFinishRatio = curDiagonal / fullDiagonal
    # avg_loudness = (1.1 - minDistFinishRatio) / 1
    avg_loudness = -0.49 * minDistFinishRatio + 0.5
    # avg_loudness = 0.25 / (10 * minDistFinishRatio + 0.5)
    Ux = posY
    Dx = siz - 2
    Uy = siz - posX
    Dy = 2
    Uangle = angle * 180 / math.pi - 90

    if Dx == Ux:
        Dx += 0.001
    dest_bearing = math.atan((Dy - Uy) / (Dx - Ux)) * 180 / math.pi

    theta = Uangle - dest_bearing

    vol_left = - avg_loudness * math.sin(math.pi / 180 * theta) + avg_loudness
    vol_right = avg_loudness * math.sin(math.pi / 180 * theta) + avg_loudness

    # print(theta, avg_loudness, vol_left, vol_right)

    music_ch1.set_volume(vol_left, 0.0)
    music_ch2.set_volume(0.0, vol_right)


def update_out_ping(dir, siz, loudness = 1.0):
    global angle
    Ux = posY
    Uy = siz - posX
    Uangle = angle * 180 / math.pi - 90
    theta = Uangle - dir
    vol_left = min(- loudness * math.sin(math.pi / 180 * theta) + loudness, 1.0)
    vol_right = min(loudness * math.sin(math.pi / 180 * theta) + loudness, 1.0)
    channel1.set_volume(vol_left, 0.0)
    channel2.set_volume(0.0, vol_right)


def update_echo(x, y, loudness, siz):
    global angle
    Ux = posY
    Uy = siz - posX
    Uangle = angle * 180 / math.pi - 90
    if x == Ux:
        x += 0.001
    dest_bearing = math.atan((y - Uy) / (x - Ux)) * 180 / math.pi

    theta = Uangle - dest_bearing
    # print(x, y)
    # print(Uangle, dest_bearing)
    vol_left = min(- loudness * math.sin(math.pi / 180 * theta) + loudness, 1.0)
    vol_right = min(loudness * math.sin(math.pi / 180 * theta) + loudness, 1.0)
    ping_ch1.set_volume(vol_left, 0.0)
    ping_ch2.set_volume(0.0, vol_right)


# set up pygame
pygame.mixer.pre_init(22050, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.set_num_channels(12)
pygame.mixer.set_reserved(6)
pygame.init()
pygame.font.init()
time.sleep(1)

# setup the screen and main clock
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("your title here")
clock = pygame.time.Clock()

# sounds
music = pygame.mixer.Sound("sounds/looping_radio_mix.wav")
finishMusic = pygame.mixer.Sound("sounds/Splashing_Around.wav")
# music.play(loops=-1)
moveSound1 = pygame.mixer.Sound("sounds/step1.wav")
moveSound2 = pygame.mixer.Sound("sounds/step2.wav")
moveSound3 = pygame.mixer.Sound("sounds/step3.wav")
moveSound4 = pygame.mixer.Sound("sounds/step4.wav")

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(5)
ping_ch1 = pygame.mixer.Channel(1)
ping_ch2 = pygame.mixer.Channel(2)
music_ch1 = pygame.mixer.Channel(3)
music_ch2 = pygame.mixer.Channel(4)
music_ch1.play(music, loops=-1)
music_ch2.play(music, loops=-1)

stepDelay = 30

# music.set_volume(0.01)

# the pings
pingDelay = 0
pingSound = pygame.mixer.Sound("sounds/ping1_best.wav")
pingX = -5
pingY = -5
pingActive = False
pingAng = 0
pingVelX = 0
pingVelY = 0
pingPos = [-5, -5]
frames = 0

# position X AND Y ARE SWAPPED KINDA
posX = 1.0
posY = 0.0

initial_calibration = connect_myo.calculate_yaw_from_myo() - (math.pi / 2)

# coordinates of the walls
wallList = []
for i in range(len(maze.grid)):
    for j in range(len(maze.grid[i])):
        if maze.grid[i][j] == "W":
            wallList.append([i, j])

# stats
moveSpeed = 1.0 / 60  # grid tiles per second / 60 frames per second

# toggle
# debounce = False
previous = False
actual = True

out_ping_active = False
out_ping_dir = 0

echo_active = False
sonar_loudness = 0
realPingX = realPingY = 0

tick = 0

while True:
    screen.fill([190, 190, 190])

    pingDelay += -1

    # get da angle
    angle = connect_myo.calculate_yaw_from_myo() - initial_calibration
    # ping when mouse is pressed and if there are no pings rn
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == 1 and pingActive == False and pingDelay <= 0:
        pingSound.set_volume(1.0)
        channel1.play(pingSound)
        channel1.set_volume(0.0)
        channel2.play(pingSound)
        channel2.set_volume(0.0)
        pingX = posX
        pingY = posY
        pingAng = angle
        out_ping_dir = angle * 180 / math.pi - 90
        pingVelX = math.cos(pingAng) * 3 / 60
        pingVelY = math.sin(pingAng) * 3 / 60
        pingActive = True
        out_ping_active = True
        pingDelay = 10
        pingPos = [int(round(pingX)), int(round(pingY))]

    newPingX = newPingY = 0
    if pingActive:
        frames += 1
        pingX += pingVelX
        pingY += pingVelY
        newPingX = pingX
        newPingY = pingY
        pingPos = [int(round(newPingX)), int(round(newPingY))]

        if pingPos in wallList or pingPos[0] < 0 or pingPos[0] >= maze.size or pingPos[1] < 0 or pingPos[1] >= maze.size:
            if (1.1 / (frames / 30)) <= 0.15:
                sonar_loudness = 0.15
                # print(0.15)
            else:
                sonar_loudness = (1.1 / (frames / 30))
                # print(1.1 / (frames / 10))
            ping_ch1.play(pingSound)
            ping_ch1.set_volume(0.0)
            ping_ch2.play(pingSound)
            ping_ch2.set_volume(0.0)
            sound_active = True
            frames = 0
            pingActive = False

    # if connect_myo.sonarActivated:
    #    print("BEEP")

    for i in range(len(wallList)):
        pygame.draw.rect(screen, (25, 25, 25), (wallList[i][1] * (500 / maze.size) - (250 / maze.size), (wallList[i][0] - 1) * (500 / maze. size) + (250 / maze.size), 500 / maze.size, 500 / maze.size), 4)

    pygame.draw.circle(screen, (255, 0, 0), (int(posY * (500/maze.size)), int(posX * (500/maze.size))), 7)
    pygame.draw.circle(screen, (155, 155, 255), (int(pingY * (500 / maze.size)), int(pingX * (500 / maze.size))), 5)

    # moving
    pressed = pygame.key.get_pressed()
    if mouse[2]:
        move_player(pressed, moveSpeed, angle, wallList, maze.size)
    posToGrid = [int(round(posX)), int(round(posY))]

    if mouse[1]:  # recalibrate using middle mouse click
        initial_calibration = connect_myo.calculate_yaw_from_myo() - (math.pi / 2)

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
    # play music
    do_music(maze.size)
    # update sonar sounds
    if channel1.get_busy():
        update_out_ping(out_ping_dir, maze.size)
    if ping_ch1.get_busy() or ping_ch2.get_busy():
        if newPingX != 0 and newPingY != 0:
            realPingX = newPingX
            realPingY = newPingY
        update_echo(realPingY, maze.size - realPingX, sonar_loudness, maze.size)
    # hit boxes
    if posToGrid == [8, 9]:
        print("YOU WIN")
        finishMusic.play()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if not previous:
            actual = not actual
        previous = True
    else:
        previous = False

    if actual:
        screen.fill([0, 0, 0])

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            connect_myo.close_connection_to_myo()
            sys.exit()

    # if tick == 59:
    #     tick = 0
    # else:
    #     tick += 1

