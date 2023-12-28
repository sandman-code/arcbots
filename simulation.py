from kinematics import fk, ik

# Example file showing a basic pygame "game loop"
import pygame
import sys
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
THETA = 0
R_X = WINDOW_WIDTH /2
R_Y = WINDOW_HEIGHT / 2

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    VEL_X = 0
    VEL_Y = 0
    while True:
        drawGrid()
        drawBot(VEL_X, VEL_Y)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    VEL_Y -= 1
                    print('Left shift was in a pressed state when this event '
                      'occurred.')
                if event.key == pygame.K_s:
                    VEL_Y += 1
                if event.key == pygame.K_d:
                    VEL_X += 1
                if event.key == pygame.K_a:
                    VEL_X -= 1


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.display.flip()

def drawGrid():
    blockSize = 50 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def drawBot(VEL_X, VEL_Y):
    pygame.draw.circle(SCREEN,"purple", (R_X, R_Y), 80)
    drawVector(VEL_X, VEL_Y)


    w_omega = fk(0, VEL_X, VEL_Y)

    angle = -np.pi/2
    pygame.draw.circle(SCREEN, "gray", (80 * np.cos(angle) + R_X, 80 * np.sin(angle) + R_Y), 30)
    drawWheelVector(angle, w_omega[0])
    angle += 2.0944
    pygame.draw.circle(SCREEN, "gray", (80 * np.cos(angle) + R_X, 80 * np.sin(angle) + R_Y), 30)
    drawWheelVector(angle, w_omega[1])
    angle += 2.0944
    pygame.draw.circle(SCREEN, "gray", (80 * np.cos(angle) + R_X, 80 * np.sin(angle) + R_Y), 30)
    drawWheelVector(angle, w_omega[2])

def drawVector(VEL_X, VEL_Y):
    pygame.draw.line(SCREEN, "red", (R_X, R_Y), (VEL_X + R_X, VEL_Y + R_Y), 5 )
    pygame.draw.circle(SCREEN, "red", (VEL_X + R_X, VEL_Y + R_Y), 5)


def translate(x,y):
    mat = np.eye(3)
    mat[0,2] = x
    mat[1,2] = y
    return mat

def rotate(angle):
    return np.array([[np.cos(angle), np.sin(angle), 0],
                     [-np.sin(angle), np.cos(angle), 0],
                     [0,0,1],])

def drawWheelVector(angle, w):
    origin_x = 80 * np.cos(angle) + R_X
    origin_y = 80 * np.sin(angle) + R_Y

    v_0 = np.array([origin_x, origin_y, 1])
    new_axis = translate(origin_x, origin_y) @ rotate(angle)
    pass


main()