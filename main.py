import pygame
from time import time as now
from player_class import Player_Class

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# wyświetlanie okna gry
pygame.display.set_caption("Moja Gra")
player = Player_Class(width=100, height=100, pos_x=0, pos_y=0, rotation=0, window_size=(SCREEN_WIDTH, SCREEN_HEIGHT))


run = True
# pętla główna
#definiujemy zmienne
KOLOR = (255, 0, 0)
x = 10
y = 30
rect_width = 100
rect_height = 100
rect_small = False
krok = 1

rect_pulse_timer = now()
screen_refresh_timer = now()

while run:
    win.fill((0,0,0))
    actual_time = now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        player.move(-player.pos_step, 0)
        pygame.time.delay(1)
    if keys[pygame.K_RIGHT] :
        player.move(player.pos_step, 0)
        pygame.time.delay(1)
    if keys[pygame.K_UP] :
        player.move(0, -player.pos_step)
        pygame.time.delay(1)
    if keys[pygame.K_DOWN] :
        player.move(0, player.pos_step)
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

    pygame.draw.rect(win, KOLOR, (player.pos_x, player.pos_y, player.width, player.height))

    if actual_time - screen_refresh_timer > 1/60:
        screen_refresh_timer = actual_time
        
        pygame.display.update()