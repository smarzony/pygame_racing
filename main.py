import pygame
from time import time as now

from lib.player import Player_Class, FWD, BWD

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
KOLOR = (255, 0, 0)

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# wyświetlanie okna gry
pygame.display.set_caption("Arrow Racer")

img_path = 'img/player_transparent.png'
playerImg = pygame.image.load(img_path)

car = Player_Class(parent=win, width=100, height=100, pos_x=0, pos_y=0, rotation=0, window_size=(SCREEN_WIDTH, SCREEN_HEIGHT), color=KOLOR, img=playerImg)
playerImg = pygame.transform.scale(playerImg, (car.motion.width, car.motion.height))

run = True
rect_small = False

speed_last = 0


rect_pulse_timer = now()
tick_timer = now()
print_debug_timer = now()

while run:
    win.fill((100,100,100))
    actual_time = now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:               
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                car.motion.start()
                print("Accelerating ", end='')
                if event.key == pygame.K_UP:
                    car.motion.direction = FWD
                    print("FWD")
                else:
                    car.motion.direction = BWD
                    print("BWD") 

        if event.type == pygame.KEYUP:               
            # checking if key "A" was pressed
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                # car.motion.in_motion = False
                print("Stopping")
                car.motion.stop()

    keys = pygame.key.get_pressed()
    if True in keys:
        if keys[pygame.K_LEFT] :
            # car.set_pos(-car.pos_step, 0)
            car.motion.rotate("L")            

        if keys[pygame.K_RIGHT] :
            # car.set_pos(car.pos_step, 0)
            car.motion.rotate("R")

        pygame.time.delay(1)





    if actual_time - rect_pulse_timer > 1:
        rect_pulse_timer = actual_time
        rect_small = not rect_small

    if rect_small:
        car.motion.width = 90
        car.motion.height = 100
    else:
        car.motion.width = 100
        car.motion.height = 90


    if actual_time - print_debug_timer > 0.5:
        print_debug_timer = actual_time
        # print('rotation:', car.rotation)
        if speed_last != car.motion.speed_actual:
            print("speed:", car.motion.speed_actual, "in motion:", car.motion.in_motion)

        speed_last = car.motion.speed_actual


    if actual_time - tick_timer > 1/60:
        tick_timer = actual_time

        if car.motion.in_motion:
            car.motion.calculate_speed()
            car.motion.calculate_movement_vector()
            car.motion.set_new_position()



            # car.move()
        
        # playerImg = pygame.image.load(img_path)
        playerImg = pygame.image.load(img_path).convert_alpha(win)
        playerImg = pygame.transform.scale(playerImg, (car.motion.width, car.motion.height))
        playerImg = pygame.transform.rotate(playerImg, car.motion.rotation)
        win.blit(playerImg, (car.motion.x, car.motion.y))
        pygame.display.update()