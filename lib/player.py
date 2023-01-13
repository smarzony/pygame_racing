import math
from time import time as now

FWD = True
BWD = False

class Motion():
    def __init__(self, window_size):
        self.in_motion = False
        self.speed_actual = 0
        self.speed_start = 0
        self.speed_max = 5
        self.start_accelerating_time = 0.0
        self.start_decelerating_time = 0.0
        self.direction = FWD
        self.acceleration_ramp_seconds = 2
        self.rotation = 0
        self.rotation_step = 0.5
        self.vector = [0, 0]
        self.stopping = False

        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.window_size = window_size

    def start(self):
        self.in_motion = True
        self.stopping = False
        print('self.in_motion : ', self.in_motion )
        self.speed_start = self.speed_actual
        self.start_accelerating_time = now()

    def stop(self):
        self.speed_start = self.speed_actual  
        self.stopping = True      
        self.start_decelerating_time = now()

    def acceleration(self):
        if self.speed_actual < self.speed_max:
            self.speed_actual += 0.05
        # # if now() - self.start_accelerating < self.acceleration_ramp:
        # self.speed_actual = ((now() - self.start_accelerating_time)/ (self.acceleration_ramp_seconds - (self.speed_start/self.speed_max)*self.acceleration_ramp_seconds)) * self.speed_max    
        # # if self.speed_actual == self.max_speed:
        # #     self.speed_top
    
    def deceleration(self):
        if self.speed_actual > 0:
            self.speed_actual -= 0.03
        else:
            self.speed_actual = 0
            self.in_motion = False
            print('Decel self.in_motion: ', self.in_motion)




        # # if now() - self.start_accelerating < self.acceleration_ramp:
        # self.speed_actual = self.speed_start - ((now() - self.start_accelerating_time)/ (self.acceleration_ramp_seconds - (self.speed_start/self.speed_max)*self.acceleration_ramp_seconds)) * self.speed_max  
        # if self.speed_actual < 0:
        #     self.speed_actual = 0 
        #     self.stopping = False

    def calculate_speed(self):
        if self.in_motion:
            if self.stopping is False:
                self.acceleration()
            else:
                self.deceleration()

    def calculate_movement_vector(self):
        self.vector = [0, 0]
        if self.speed_actual > 0:
            self.vector[0] = self.speed_actual * math.cos(math.radians(self.rotation - 90))
            self.vector[1] = self.speed_actual * math.sin(math.radians(self.rotation - 90))

    def set_new_position(self):
        if self.direction is FWD:            
            self.x -= self.vector[0]
            self.y += self.vector[1]
        else: 
            print("Set position with - vector")                
            self.x += self.vector[0]
            self.y -= self.vector[1]

        self.check_boundaries() 

    def rotate(self, dir):
        if dir == "R":
            self.rotation -= self.rotation_step
        else:
            self.rotation += self.rotation_step

        self.check_boundaries()

    def check_boundaries(self):
        if self.x > self.window_size[0] - 120:
            self.x = self.window_size[0] - 120

        elif self.x < 20:
            self.x = 20

        if self.y > self.window_size[1] - 120:
            self.y = self.window_size[1] - 120

        elif self.y < 20:
            self.y = 20

        if self.rotation > 360:
            self.rotation -= 360

        elif self.rotation < 0:
            self.rotation += 360

        if self.speed_actual > self.speed_max:
            self.speed_actual = self.speed_max

        elif self.speed_actual < 0:
            self.speed_actual = 0

class Player_Class():
    def __init__(self, parent, window_size, height, width, pos_x, pos_y, rotation, color, img):
        self.parent = parent
        self.window_size = window_size
        self.color = color
        self.img = img
        self.motion = Motion(window_size)

      
