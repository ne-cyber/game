import pygame
import random
import os

pygame.init()

main_display = pygame.display.set_mode((800, 600))

playing = True

FPS = pygame.time.Clock()

EVENT_CREATE_ENEMY = pygame.USEREVENT + 1
EVENT_CREATE_BONUS = pygame.USEREVENT + 2
EVENT_CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(EVENT_CREATE_ENEMY, 2000)
pygame.time.set_timer(EVENT_CREATE_BONUS, 300)
pygame.time.set_timer(EVENT_CHANGE_IMAGE, 100)

font = pygame.font.SysFont('Verdana', 36)

#
# player animation begin
#
PLAYER_IMAGES_NAMES = os.listdir("./resource/Goose")

player_images = []
for name in PLAYER_IMAGES_NAMES:
    original_image = pygame.image.load(os.path.join("./resource/Goose", name))
    resized_image = pygame.transform.scale(original_image, (original_image.get_width() * 2, original_image.get_height() * 2))
    
    #sсохранить картинку в списке
    player_images.append(resized_image)

image_index = 0
PLAYER_IMAGES_COUNT = len(PLAYER_IMAGES_NAMES)
#
# player animation end
#



player = player_images[0]

player_rect = pygame.Rect(0, 0, player_images[0].get_width(), player_images[0].get_height())

bg = pygame.transform.scale(pygame.image.load('./resource/background.png'), (800,600))

bg_x1 = 0
bg_x2 = 800
bg_move = 3

def create_enemy():
    #enemy = pygame.Surface((20, 20))
    #enemy.fill('red')
    enemy = pygame.transform.scale(pygame.image.load('./resource/enemy.png'), (205/2,72/2))
    

    enemy_size = (enemy.get_width(), enemy.get_height())

    enemy_rect = pygame.Rect(800, random.randint(0, 600), *enemy_size)

    enemy_move = [random.randint(-6, -1),0]

    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    #bonus = pygame.Surface((30,30))
    #bonus.fill('gold')
    bonus = pygame.transform.scale(pygame.image.load('./resource/bonus.png'), (179//3,298//3))
    

    bonus_size = (bonus.get_width(), bonus.get_height())    

    bonus_rect = pygame.Rect(random.randint(0, 800), 0, *bonus_size)

    bonus_move = [0,random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

enemies = []

bonuses = []

score = 0

while playing:
    
    bg_x1 -= bg_move
    bg_x2 -= bg_move

    if bg_x1 < -800:
        bg_x1 = 800
    if bg_x2 < -800:
        bg_x2 = 800

    main_display.blit(bg, (bg_x1,0))
    main_display.blit(bg, (bg_x2,0))
    main_display.blit(player, player_rect)

    for en in enemies:
        main_display.blit(en[0], en[1])

    for bn in bonuses:
        main_display.blit(bn[0], bn[1])

    main_display.blit(font.render(str(score), True, 'cyan'), (800 - 100, 30))

    pygame.display.flip()

    for en in enemies:
        en[1] = en[1].move(en[2])

    for bn in bonuses:
        bn[1] = bn[1].move(bn[2])


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move([-4,0])
    if keys[pygame.K_RIGHT] and player_rect.right < 800:
        player_rect = player_rect.move([4,0])

    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect = player_rect.move([0,-4])
    if keys[pygame.K_DOWN] and player_rect.bottom < 600:
        player_rect = player_rect.move([0,4])



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False

        if event.type == EVENT_CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == EVENT_CREATE_BONUS:
            bonuses.append(create_bonus())

        if event.type == EVENT_CHANGE_IMAGE:
            image_index += 1

            if image_index >= PLAYER_IMAGES_COUNT:
                image_index = 0

            player = player_images[image_index]


    for en in enemies:
        if player_rect.colliderect(en[1]):
            playing = False

        if en[1].left < 0:
            enemies.pop(enemies.index(en))

    for bn in bonuses:
        if player_rect.colliderect(bn[1]):
            score = score + 150
            bonuses.pop(bonuses.index(bn))

    
    for bn in bonuses:
        if bn[1].bottom > 600:
            bonuses.pop(bonuses.index(bn))
    


    
    FPS.tick(120)

