import math
from time import time as now

FWD = True
BWD = False

class Motion():
    def __init__(self, window_size):
        self.speed_actual = 0
        self.speed_max = 5
        self.direction = FWD
        self.rotation = 0
        self.rotation_step = 0.5
        self.vector = [0, 0]
        self.accelerate = False

        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.window_size = window_size

    def acceleration(self):
        if self.speed_actual < self.speed_max:
            self.speed_actual += 0.05
    
    def deceleration(self):
        if self.speed_actual > -self.speed_max:
            print('self.speed_actual: ', self.speed_actual)

            self.speed_actual -= 0.05

    def stopping(self):
        if self.speed_actual > 0.1:
            self.speed_actual -= 0.01

        elif self.speed_actual < -0.1:
            self.speed_actual += 0.01

        if abs(self.speed_actual) < 0.1:
            self.speed_actual = 0

    def calculate_speed(self):
        if self.accelerate:
            if self.direction is FWD:
                self.acceleration()
            else:
                self.deceleration()
        else:
            self.stopping()

    def calculate_movement_vector(self):
        self.vector = [0, 0]
        self.vector[0] = self.speed_actual * math.cos(math.radians(self.rotation - 90))
        self.vector[1] = self.speed_actual * math.sin(math.radians(self.rotation - 90))

    def set_new_position(self):
        self.x -= self.vector[0]
        self.y += self.vector[1] 

        self.check_boundaries() 


    def rotate(self, dir):
        if abs(self.speed_actual) > 0:
            if dir == "R":
                self.rotation -= self.rotation_step* (1-((0.8*abs(self.speed_actual))/self.speed_max))
            else:
                self.rotation += self.rotation_step* (1-((0.8*abs(self.speed_actual))/self.speed_max))

        self.check_boundaries()

    def check_boundaries(self):
        if self.x > self.window_size[0] - 120:
            self.x = self.window_size[0] - 120
            self.speed_actual *= .9

        elif self.x < 20:
            self.x = 20
            self.speed_actual *= .9

        if self.y > self.window_size[1] - 120:
            self.y = self.window_size[1] - 120
            self.speed_actual *= .9

        elif self.y < 20:
            self.y = 20
            self.speed_actual *= .9

        if self.rotation > 360:
            self.rotation -= 360

        elif self.rotation < 0:
            self.rotation += 360

        if self.speed_actual > self.speed_max:
            self.speed_actual = self.speed_max

        elif self.speed_actual < -self.speed_max:
            self.speed_actual = -self.speed_max

class Player_Class():
    def __init__(self, parent, window_size, height, width, pos_x, pos_y, rotation, color, img):
        self.parent = parent
        self.window_size = window_size
        self.color = color
        self.img = img
        self.motion = Motion(window_size)

      
