from random import randint
import pygame
import time

possibleXY = [[1, 1], [3, 1], [5, 1], [1, 3], [3, 3], [5, 3], [1, 5], [3, 5], [5, 5]]

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 72)

    existing_squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    score = 0
    timeInt = 2.0
    step_time = timeInt*1000.0
    first_time = time.time()*1000.0
    matrix = []
    nextLevel = False
    gameOver = False

    while True:
        local_time = time.time()*1000
        if ((local_time - first_time) >= step_time):
            while (not gameOver): #do while emulate
                numerSquare= randint(0, 8)
                if(existing_squares[numerSquare] == 0):
                    matrix.append([possibleXY[numerSquare][0]*100, possibleXY[numerSquare][1]*100, numerSquare])
                    existing_squares[numerSquare] = 1
                    break
            first_time = time.time()*1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEMOTION:
                mause_position = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    if(not gameOver):
                        for aim in matrix:
                            if(mause_position[0]>=aim[0] and mause_position[0]<= (aim[0]+100) and mause_position[1]>=aim[1] and mause_position[1]<= (aim[1]+100)):
                                existing_squares[aim[2]] = 0
                                matrix.remove(aim)
                                score = score +1
                    else:
                       main()
                       return

        screen.fill((0, 0, 0))
        if (matrix != None and len(matrix) > 0):
            for square in matrix:
                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(square[0], square[1], 100, 100))
        if(score % 10 == 0 and timeInt > 0 and nextLevel):
            timeInt = 0.8*timeInt
            step_time = timeInt*1000.0
            nextLevel = False
        if (score % 10 != 0 and not gameOver):
            nextLevel = True
        if len(matrix) >= 9:
            gameOver = True
            textGM = font.render("GAME OVER!", True, (128, 0, 0))
            screen.blit(textGM, (350- textGM.get_width() // 2, 350 - textGM.get_height() // 2))
            textGM2 = font.render("Click to try again!", True, (128, 0, 0))
            screen.blit(textGM2, (325 - textGM2.get_width() // 2, 450 - textGM2.get_height() // 2))

        text = font.render(str(score), True, (0, 128, 0))
        screen.blit(text, (50 - text.get_width() // 2, 50 - text.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)

main()