import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
user_location = [50,50]
move_ticker = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if move_ticker == 0:
            move_ticker = 600
            user_location[0] -= 1
            print(user_location)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if move_ticker == 0:
            move_ticker = 600
            user_location[0] += 1
            print(user_location)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if move_ticker == 0:
            move_ticker = 600
            user_location[1] -= 1
            print(user_location)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if move_ticker == 0:
            move_ticker = 600
            user_location[1] += 1
            print(user_location)
    screen.fill(black)
    pygame.display.flip()

    if move_ticker > 0:
        move_ticker -= 1

