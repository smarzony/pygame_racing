class Player_Class():
    def __init__(self, height, width, pos_x, pos_y, rotation, window_size):
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_step = 1
        self.rotation = rotation
        self.window_size = window_size

    def move(self, x, y):        
        self.pos_x += x
        self.pos_y += y

        if self.pos_x > self.window_size[0] - 120:
            self.pos_x = self.window_size[0] - 120

        elif self.pos_x < 20:
            self.pos_x = 20

        if self.pos_y > self.window_size[1] - 120:
            self.pos_y = self.window_size[1] - 120

        elif self.pos_y < 20:
            self.pos_y = 20

    def rotate(self, angle):
        self.rotation += angle
