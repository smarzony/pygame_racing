import math
from time import time as now

FWD = True
BWD = False

class Motion():
    def __init__(self):
        self.in_motion = False
        self.speed_actual = 0
        self.speed_start = 0
        self.max_speed = 5
        self.start_accelerating_time = 0.0
        self.start_decelerating_time = 0.0
        self.direction = 0
        self.acceleration_ramp_seconds = 2

    def start(self):
        self.in_motion = True
        self.speed_start = self.speed_actual
        self.start_accelerating_time = now()

    def stop(self):
        self.speed_start = self.speed_actual        
        self.start_decelerating_time = now()

    def acceleration(self):
        # if now() - self.start_accelerating < self.acceleration_ramp:
        self.speed_actual = ((now() - self.start_accelerating_time)/ (self.acceleration_ramp_seconds - (self.speed_start/self.max_speed)*self.acceleration_ramp_seconds)) * self.max_speed    

    def deceleration(self):
        # if now() - self.start_accelerating < self.acceleration_ramp:
        self.speed_actual = self.speed_start - ((now() - self.start_accelerating_time)/ (self.acceleration_ramp_seconds - (self.speed_start/self.max_speed)*self.acceleration_ramp_seconds)) * self.max_speed  
        if self.speed_actual < 0:
            self.speed_actual = 0 

class Positions():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0

class Player_Class():
    def __init__(self, parent, window_size, height, width, pos_x, pos_y, rotation, color, img):
        self.parent = parent
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_speed = 5
        self.rotation_step = 0.5
        self.rotation = rotation
        self.window_size = window_size
        self.color = color
        self.img = img
        self.vector = [0, 0]
        self.in_motion = False
        self.direction = FWD
        self.check_boundaries()

    def check_boundaries(self):
        if self.pos_x > self.window_size[0] - 120:
            self.pos_x = self.window_size[0] - 120

        elif self.pos_x < 20:
            self.pos_x = 20

        if self.pos_y > self.window_size[1] - 120:
            self.pos_y = self.window_size[1] - 120

        elif self.pos_y < 20:
            self.pos_y = 20

        if self.rotation > 360:
            self.rotation -= 360

        elif self.rotation < 0:
            self.rotation += 360

    def set_pos(self, x, y):        
        self.pos_x += x
        self.pos_y += y
        self.check_boundaries()

    def rotate(self, dir):
        if dir == "L":
            self.rotation -= self.rotation_step
        else:
            self.rotation += self.rotation_step

        self.check_boundaries()


    def move(self):
        self.vector = [0, 0]
        self.vector[0] = self.max_speed * math.cos(math.radians(self.rotation - 90))
        self.vector[1] = self.max_speed * math.sin(math.radians(self.rotation - 90))

        if self.direction is FWD:            
            self.pos_x -= self.vector[0]
            self.pos_y += self.vector[1]
        else:            
            self.pos_x += self.vector[0]
            self.pos_y -= self.vector[1]

        self.check_boundaries()        
