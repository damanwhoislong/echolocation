import random

def create_maze(size):

    grid = []
    wall = "W"
    path = "P"
    start = "S"
    finish = "F"

    for y in range(size):
        grid.append([])
        for x in range(size):
            grid[y].append(wall)

    pathRight = (size-1)*2-2
    pathDown = (size-1)*2-2

    pathUp = (size-1)
    pathLeft = (size-1)

    yCoord = 1
    xCoord = 1
    grid[1][1] = path


    while pathRight > 0 or pathDown > 0 or pathUp > 0 or pathDown > 0:
        dir = random.randint(0,5)
        if (dir == 0 or dir == 4) and pathDown > 0 and xCoord >= 1 and xCoord < (size-2):
            xCoord += 1
            grid[yCoord][xCoord] = path
            pathDown -= 1
        elif (dir == 1 or dir == 5) and pathRight > 0 and yCoord >= 1 and yCoord < (size-2):
            yCoord += 1
            grid[yCoord][xCoord] = path
            pathRight -= 1
        elif dir == 2 and pathUp > 0 and xCoord > 1 and xCoord <= (size-2):
            xCoord -= 1
            grid[yCoord][xCoord] = path
            pathUp -= 1
        elif dir == 3 and pathLeft > 0 and yCoord > 1 and yCoord <= (size-2):
            yCoord -= 1
            grid[yCoord][xCoord] = path
            pathLeft -= 1

    grid[1][0] = start
    grid[size-2][size-1] = finish
    print(grid)
    return grid



