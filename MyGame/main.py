from random import randint
import pygame
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 72)

    score = 0
    timeInt = 1.0
    step_time = time.localtime(timeInt)
    first_time = time.localtime(time.time())
    possibleXY = [[1,1],[3,1],[5,1],[1,3],[3,3],[5,3],[1,5],[3,5],[5,5]]
    existing_squares = [0,0,0,0,0,0,0,0,0]
    matrix = []

    while True:
        local_time = time.localtime(time.time())
        if (time.mktime(local_time) - time.mktime(first_time)) > time.mktime(step_time):
            numerSquare= randint(0, 7)
            if(existing_squares[numerSquare] == 0):
                matrix.append([possibleXY[numerSquare][0]*100, possibleXY[numerSquare][1]*100, numerSquare])
                existing_squares[numerSquare] = 1
            first_time = time.localtime(time.time())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEMOTION:
                mause_position = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    for aim in matrix:
                        if(mause_position[0]>=aim[0] and mause_position[0]<= (aim[0]+100) and mause_position[1]>=aim[1] and mause_position[1]<= (aim[1]+100)):
                            existing_squares[aim[2]] = 0
                            matrix.remove(aim)
                            score = score +1

        screen.fill((0, 0, 0))
        if (matrix != None and len(matrix) > 0):
            for square in matrix:
                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(square[0], square[1], 100, 100))
        text = font.render(str(score), True, (0, 128, 0))
        screen.blit(text, (50 - text.get_width() // 2, 50 - text.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)


main()