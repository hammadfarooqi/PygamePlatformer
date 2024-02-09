class button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.show = False
        self.active = True

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            return True
        return False
    
class block():
    def __init__(self, x, y, img, state = 1):
        self.x = x
        self.y = y
        self.img = img
        self.state = state
        self.verticalBuffer = 0

        # means the grass is 4 pixels too tall
        if self.img == "grass":
            self.verticalBuffer = 4

    def draw(self, win, images):
        win.blit(images[self.img], (self.x, self.y))
