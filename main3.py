import pygame
import random

pygame.init()

main_display = pygame.display.set_mode((800, 600))

playing = True

FPS = pygame.time.Clock()

EVENT_CREATE_ENEMY = pygame.USEREVENT + 1
# Домашка EVENT_CREATE_BONUS begin
EVENT_CREATE_BONUS = pygame.USEREVENT + 2
# Домашка EVENT_CREATE_BONUS end

pygame.time.set_timer(EVENT_CREATE_ENEMY, 2000)
# Домашка set_timer EVENT_CREATE_BONUS begin
pygame.time.set_timer(EVENT_CREATE_BONUS, 300)
# Домашка set_timer EVENT_CREATE_BONUS end

player = pygame.image.load('./resource/player.png')
player_rect = pygame.Rect(0, 0, player.get_width(), player.get_height())

def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load('./resource/enemy.png'), (205/2,72/2))

    enemy_size = (enemy.get_width(), enemy.get_height())

    enemy_rect = pygame.Rect(800, random.randint(0, 600), *enemy_size)

    enemy_move = [random.randint(-6, -1),0]

    return [enemy, enemy_rect, enemy_move]

enemies = []

# Домашка create_bonus begin
def create_bonus():
    bonus = pygame.transform.scale(pygame.image.load('./resource/bonus.png'), (179//3,298//3))
    
    bonus_size = (bonus.get_width(), bonus.get_height())

    bonus_rect = pygame.Rect(random.randint(0, 800), 0, *bonus_size)

    bonus_move = [0,random.randint(2, 5)]
    return [bonus, bonus_rect, bonus_move]
# Домашка create_bonus end

# Домашка коллекция bonuses
bonuses = []

while playing:

    main_display.fill('black')

    main_display.blit(player, player_rect)


    for en in enemies:
        main_display.blit(en[0], en[1])


    #Домашка прорисовка bonuses begin
    for bn in bonuses:
        main_display.blit(bn[0], bn[1])
    #Домашка прорисовка bonuses end


    pygame.display.flip()


    for en in enemies:
        en[1] = en[1].move(en[2])

    #Домашка move bonuses begin
    for bn in bonuses:
        bn[1] = bn[1].move(bn[2])
    #Домашка move bonuses end


    keys = pygame.key.get_pressed()


    
    if keys[pygame.K_RIGHT] and player_rect.right < 800:
        player_rect = player_rect.move([4,0])
    if keys[pygame.K_DOWN] and player_rect.bottom < 600:
        player_rect = player_rect.move([0,4])

    # 
    # Домашка K_UP, K_LEFT begin
    #
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect = player_rect.move([0,-4])
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move([-4,0])
    # 
    # Домашка K_UP, K_LEFT end
    #
    


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False

        if event.type == EVENT_CREATE_ENEMY:
            enemies.append(create_enemy())

        #Домашка EVENT_CREATE_BONUS begin
        if event.type == EVENT_CREATE_BONUS:
            bonuses.append(create_bonus())
        #Домашка EVENT_CREATE_BONUS end

    for en in enemies:
        if player_rect.colliderect(en[1]):
            playing = False

        if en[1].left < 0:
            enemies.pop(enemies.index(en))

    #Домашка удаление bonus'a который упал за границы begin
    for bn in bonuses:
        if bn[1].bottom > 600:
            bonuses.pop(bonuses.index(bn))
    #Домашка удаление bonus'a который упал за границы end


    
    FPS.tick(120)

