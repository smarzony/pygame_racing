import pygame
from time import time as now
from player_class import Player_Class

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
KOLOR = (255, 0, 0)

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# wyświetlanie okna gry
pygame.display.set_caption("Moja Gra")

img_path = 'img/player1.png'
playerImg = pygame.image.load(img_path)

player = Player_Class(parent=win, width=100, height=100, pos_x=0, pos_y=0, rotation=0, window_size=(SCREEN_WIDTH, SCREEN_HEIGHT), color=KOLOR, img=playerImg)
playerImg = pygame.transform.scale(playerImg, (player.width, player.height))

run = True
rect_small = False

player.pos_step = 0.2

rect_pulse_timer = now()
screen_refresh_timer = now()
print_debug_timer = now()

while run:
    win.fill((0,0,0))
    actual_time = now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if True in keys:
        if keys[pygame.K_LEFT] :
            # player.set_pos(-player.pos_step, 0)
            player.rotate("R")            

        if keys[pygame.K_RIGHT] :
            # player.set_pos(player.pos_step, 0)
            player.rotate("L")

        if keys[pygame.K_UP] :
            # player.set_pos(0, -player.pos_step)
            player.move('FWD')

        if keys[pygame.K_DOWN] :
            # player.set_pos(0, player.pos_step)
            player.move('BWD')

        # if keys[pygame.K_RCTRL] :
        #     # player.rotate("R")

        # if keys[pygame.K_KP0] :
        #     # player.rotate("L")

        pygame.time.delay(1)



    if actual_time - rect_pulse_timer > 1:
        rect_pulse_timer = actual_time
        rect_small = not rect_small

    if rect_small:
        player.width = 90
        player.height = 100
    else:
        player.width = 100
        player.height = 90


    if actual_time - print_debug_timer > 0.5:
        print_debug_timer = actual_time
        # print('rotation:', player.rotation)



    if actual_time - screen_refresh_timer > 1/60:
        screen_refresh_timer = actual_time
        
        playerImg = pygame.image.load(img_path)
        playerImg = pygame.transform.scale(playerImg, (player.width, player.height))
        playerImg = pygame.transform.rotate(playerImg, player.rotation)
        win.blit(playerImg, (player.pos_x, player.pos_y))
        pygame.display.update()