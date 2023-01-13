import math

class Player_Class():
    def __init__(self, parent, window_size, height, width, pos_x, pos_y, rotation, color, img):
        self.parent = parent
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_step = 1
        self.rotation_step = 0.5
        self.rotation = rotation
        self.window_size = window_size
        self.color = color
        self.img = img
        self.vector = [0, 0]
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


    def move(self, direction):
        self.vector = [0, 0]
        self.vector[0] = self.pos_step * math.cos(math.radians(self.rotation - 90))
        self.vector[1] = self.pos_step * math.sin(math.radians(self.rotation - 90))

        if direction == 'FWD':            
            self.pos_x -= self.vector[0]
            self.pos_y += self.vector[1]
        else:            
            self.pos_x += self.vector[0]
            self.pos_y -= self.vector[1]

        self.check_boundaries()        
