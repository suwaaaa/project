import pygame
import sys

pygame.init()
size = width, height = 600, 400
# vinfo = pygame.display.Info()
# size = width,height = vinfo.current_w,vinfo.current_h
speed = [1, 1]  # ?????
title = "My first game!!"
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption(title)
surface = pygame.image.load("C:\\Users\\12645\\Pictures\\Camera Roll\\000.jpg")
pygame.display.set_icon(surface)
ball = pygame.image.load("D://files//ball.gif")
ballrect = ball.get_rect()

fps = 500
fclock = pygame.time.Clock()
fclock.tick(fps)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])  # ???
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0] - 1)) * int(speed[0] / abs((speed[0])))
        elif event.type == pygame.K_RIGHT:
            speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
        elif event.type == pygame.K_UP:
            speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
        elif event.key == pygame.K_DOWN:
            speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1] - 1)) * int(speed[1] / abs((speed[1])))
        elif event.type == pygame.K_ESCAPE:
            sys.exit()

    if event.type == pygame.VIDEORESIZE:
        size = width, height = event.w, event.h
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    if pygame.display.get_active():
        ballrect = ballrect.move(speed[0], speed[1])

    color = 0, 0, 0
    screen.fill(color)
    screen.blit(ball, ballrect)

    pygame.display.update()
