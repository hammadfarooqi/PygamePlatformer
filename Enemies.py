
import pygame
class baddy():
    def __init__(self, x, y, distance, myLevel, myWorld = 1):
        self.x = 64 * x - 22
        self.y = 64 * y - 96
        self.width = 96
        self.height = 96
        
        self.vel = 4
        self.right = True
        self.hitbox = [33, 51, 27, 45]
        self.path = [(64 * x - 22), (64 * x - 22) + (64 * distance + 18)]
        self.level = myLevel
        self.world = myWorld
        self.walkCount = 0
        self.dead = False
        
    def draw(self, win, animations, levelNum, worldNum):
        if worldNum == self.world and levelNum == self.level:
            if not(self.dead):
                if self.walkCount >= 20:
                    self.walkCount = 0
                    
                if self.right:
                    if self.x < self.path[1]:
                        self.x += self.vel
                        self.walkCount += 1
                    else:
                        self.right = False
                        self.walkCount = 0

                    win.blit(animations["baddyWalkRight"][self.walkCount//5], (self.x, self.y))
                    
                else:
                    if self.x > self.path[0]:
                        self.x -= self.vel
                        self.walkCount += 1
                    else:
                        self.right = True
                        self.walkCount = 0

                    win.blit(animations["baddyWalkLeft"][self.walkCount//5], (self.x, self.y))

class globAttack():
    def __init__(self, x, y):
        self.x = x * 64
        self.y = y * 64
        self.hitbox = [0, 40, 64, 24]
        self.active = False
        
    def draw(self, win, animations, state, count):
        if state == 1:
            win.blit(animations["globAttackIdle"][count], (self.x, self.y))
            self.active = False
        else:
            win.blit(animations["globAttackActive"][count], (self.x, self.y))
            self.active = True

class glob():
    def __init__(self, screenWidth):
        self.width = 256
        self.height = 256
        self.hitbox = [76, 40, 108, 172]
        self.hitboxTwo = [4, 192, 248, 20]
        self.hitboxThree = [112, 40, 36, 172]
        self.x = screenWidth // 2 - self.width // 2
        self.y = 64 * 8 - self.hitbox[1] - self.hitbox[3]
        self.idleCount = 0
        self.left = True
        self.level = 5
        self.health = 50
        self.start = False
        self.dead = False
        self.deathCount = 0

        self.attackRight = False
        self.attackTime = 100
        self.attackCount = 0
        self.attackIdleCount = 0
        self.attackActiveCount = 0
        self.leftList = [globAttack(1, 7), globAttack(2, 7), globAttack(3, 7), globAttack(4, 7), globAttack(5, 7), globAttack(6, 7), globAttack(2, 5), globAttack(3, 5), globAttack(5, 3), globAttack(6, 3)]
        self.rightList = [globAttack(11, 7), globAttack(12, 7), globAttack(13, 7), globAttack(14, 7), globAttack(15, 7), globAttack(16, 7), globAttack(14, 5), globAttack(15, 5), globAttack(11, 3), globAttack(12, 3)]

    def draw(self, win, animations, man, levelNum, worldNum):
        if worldNum == 1 and levelNum == self.level:
            if self.health <= 0 and self.deathCount < 12:
                self.dead = True
                win.blit(animations["globDeath"][self.deathCount//4], (self.x, self.y))
                self.deathCount += 1
            elif self.health > 0:
                if self.idleCount >= 20:
                    self.idleCount = 0
                if man.x + man.hitbox[0] + (man.hitbox[2] // 2) < self.x + (self.width // 2):
                    self.left = True
                    win.blit(animations["globIdleLeft"][self.idleCount//4], (self.x, self.y))
                else:
                    self.left = False
                    win.blit(animations["globIdleRight"][self.idleCount//4], (self.x, self.y))
                self.idleCount += 1

    def drawHealth(self, win, levelNum, worldNum):
        if self.start:
            if worldNum == 1 and levelNum == self.level and self.health > 0:
                pygame.draw.rect(win, (100, 100, 100), [self.x + self.hitbox[0] + self.hitbox[2] // 2 - 50, self.y + self.hitbox[1] - 18, 100, 10])
                pygame.draw.rect(win, (255, 0, 0), [self.x + self.hitbox[0] + self.hitbox[2] // 2 - 50, self.y + self.hitbox[1] - 18, self.health*2, 10])

    def attack(self, win, animations, levelNum, worldNum):
        if self.start:
            if worldNum == 1 and levelNum == self.level and not(self.dead):
                if self.health <= 10:
                    self.attackTime = 48
                elif self.health <= 20:
                    self.attackTime = 60
                elif self.health <= 30:
                    self.attackTime = 72
                elif self.health <= 40:
                    self.attackTime = 84
                else:
                    self.attackTime = 96

                if self.attackCount < self.attackTime:
                    #Left Idle
                    self.attackRight = False
                    if self.attackIdleCount >= 12:
                        self.attackIdleCount = 0
                    for item in self.leftList:
                        item.draw(win, animations, 1, self.attackIdleCount // 3)
                    self.attackIdleCount += 1
                elif self.attackCount < self.attackTime * 2:
                    #Left Attack
                    if self.attackActiveCount >= 18:
                        self.attackActiveCount = 0
                    for item in self.leftList:
                        item.draw(win, animations, 2, self.attackActiveCount // 3)
                    self.attackActiveCount += 1
                elif self.attackCount < self.attackTime * 3:
                    #Right Idle
                    self.attackRight = True
                    if self.attackIdleCount >= 12:
                        self.attackIdleCount = 0
                    for item in self.rightList:
                        item.draw(win, animations, 1, self.attackIdleCount // 3)
                    self.attackIdleCount += 1
                elif self.attackCount < self.attackTime * 4:
                    #Right Attack
                    if self.attackActiveCount >= 18:
                        self.attackActiveCount = 0
                    for item in self.rightList:
                        item.draw(win, animations, 2, self.attackActiveCount // 3)
                    self.attackActiveCount += 1
                else:
                    self.attackCount = 0
                self.attackCount += 1
