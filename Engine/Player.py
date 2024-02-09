import pygame

class player():
    def __init__(self, x, y, width, height, widthAdjustment, heightAdjustment, hitboxWidth, hitboxHeight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = [widthAdjustment, heightAdjustment, hitboxWidth, hitboxHeight]

        self.xVel = 8
        self.yVel = 0
        self.onGround = False
        self.onCieling = False
        self.rightWall = False
        self.leftWall = False
        self.left = False
        self.right = True
        self.isMoving = False
        self.walkCount = 0
        self.idleCount = 0
        self.gunCount = 0
        self.dead = False
        self.maxLives = 5
        self.lives = self.maxLives
        
    def draw(self, win, animations):
        if self.walkCount >= 15:
            self.walkCount = 0
        if self.idleCount >= 24:
            self.idleCount = 0
        if self.isMoving and self.onGround:
            if self.left:
                win.blit(animations["runLeft"][self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(animations["runRight"][self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        elif self.yVel >= 0 and not(self.onGround):
            if self.left:
                win.blit(animations["jumpLeft"][0], (self.x, self.y))
            elif self.right:
                win.blit(animations["jumpRight"][0], (self.x, self.y))
        elif self.yVel < 0 and not(self.onGround):
            if self.left:
                win.blit(animations["jumpLeft"][1], (self.x, self.y))
            elif self.right:
                win.blit(animations["jumpRight"][1], (self.x, self.y))
        else:
            if self.left:
                win.blit(animations["idleLeft"][self.idleCount//6], (self.x, self.y))
                self.idleCount+=1
            else:
                win.blit(animations["idleRight"][self.idleCount//6], (self.x, self.y))
                self.idleCount+=1

class projectile():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        
        self.vel = 12 * direction
        self.hitBlock = False
        self.hide = False
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
