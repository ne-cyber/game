import pygame
import random

pygame.init()

main_display = pygame.display.set_mode((800, 600))

playing = True

FPS = pygame.time.Clock()

ball = pygame.Surface((10,10))
ball.fill('green')
ball_rect = pygame.Rect(0,0,10,10)

ball_speed = [1,1]

while playing:

    main_display.fill('black')

    main_display.blit(ball, ball_rect)

    pygame.display.flip()

    ball_rect = ball_rect.move(ball_speed)


    # 
    # ДОМАШКА begin
    #
    if ball_rect.left < 0:
        ball_speed = [1, random.random()*2 - 1]
    if ball_rect.right > 800:
        ball_speed = [-1, random.random()*2 - 1]
    #
    # ДОМАШКА end
    #


    if ball_rect.top < 0:
        ball_speed = [random.random()*2 - 1, 1]
    if ball_rect.bottom > 600:
        ball_speed = [random.random()*2 - 1, -1]


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False
    
    FPS.tick(120)

