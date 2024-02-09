"""
Hammad Farooqi
Pygame Platformer
"""
import pygame
pygame.init()

win = pygame.display.set_mode((1152, 640))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

mainMenu = [pygame.image.load('Backgrounds/MainMenu/MainMenu1.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu2.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu3.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu4.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu5.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu6.png'), pygame.image.load('Backgrounds/MainMenu/MainMenu7.png')]
bg = pygame.image.load('Backgrounds/bg.png')
gameOver = pygame.image.load('Backgrounds/GameOver.png')

playButton = pygame.image.load('Buttons/PlayButton.png')
menuAboutButton = pygame.image.load('Buttons/MenuAboutButton.png')
playAgainButton = pygame.image.load('Buttons/PlayAgainButton.png')
gameOverAboutButton = pygame.image.load('Buttons/GameOverAboutButton.png')

grass = pygame.image.load('Environment/GrassBlock.png')
dirt = pygame.image.load('Environment/DirtBlock.png')
spike = pygame.image.load('Environment/Spike.png')
heart = pygame.image.load('Man/Heart.png')

runRight = [pygame.image.load('Man/Running/RRun1.png'), pygame.image.load('Man/Running/RRun2.png'), pygame.image.load('Man/Running/RRun3.png'), pygame.image.load('Man/Running/RRun4.png'), pygame.image.load('Man/Running/RRun5.png')]
runLeft = [pygame.image.load('Man/Running/LRun1.png'), pygame.image.load('Man/Running/LRun2.png'), pygame.image.load('Man/Running/LRun3.png'), pygame.image.load('Man/Running/LRun4.png'), pygame.image.load('Man/Running/LRun5.png')]
idleRight = [pygame.image.load('Man/Idle/RIdle1.png'), pygame.image.load('Man/Idle/RIdle2.png'), pygame.image.load('Man/Idle/RIdle3.png'), pygame.image.load('Man/Idle/RIdle4.png')]
idleLeft = [pygame.image.load('Man/Idle/LIdle1.png'), pygame.image.load('Man/Idle/LIdle2.png'), pygame.image.load('Man/Idle/LIdle3.png'), pygame.image.load('Man/Idle/LIdle4.png')]
jumpRight = [pygame.image.load('Man/Jumping/RUp.png'), pygame.image.load('Man/Jumping/RDown.png')]
jumpLeft = [pygame.image.load('Man/Jumping/LUp.png'), pygame.image.load('Man/Jumping/LDown.png')]

baddyWalkRight = [pygame.image.load('Baddy/Walking/RWalk1.png'), pygame.image.load('Baddy/Walking/RWalk2.png'), pygame.image.load('Baddy/Walking/RWalk3.png'), pygame.image.load('Baddy/Walking/RWalk4.png'), pygame.image.load('Baddy/Walking/RWalk5.png')]
baddyWalkLeft = [pygame.image.load('Baddy/Walking/LWalk1.png'), pygame.image.load('Baddy/Walking/LWalk2.png'), pygame.image.load('Baddy/Walking/LWalk3.png'), pygame.image.load('Baddy/Walking/LWalk4.png'), pygame.image.load('Baddy/Walking/LWalk5.png')]
baddyIdleRight = [pygame.image.load('Baddy/Idle/RIdle1.png'), pygame.image.load('Baddy/Idle/RIdle2.png'), pygame.image.load('Baddy/Idle/RIdle3.png'), pygame.image.load('Baddy/Idle/RIdle4.png')]
baddyIdleLeft = [pygame.image.load('Baddy/Idle/LIdle1.png'), pygame.image.load('Baddy/Idle/LIdle2.png'), pygame.image.load('Baddy/Idle/LIdle3.png'), pygame.image.load('Baddy/Idle/LIdle4.png')]

globIdleRight = [pygame.image.load('GlobMonster/Idle/RIdle1.png'), pygame.image.load('GlobMonster/Idle/RIdle2.png'), pygame.image.load('GlobMonster/Idle/RIdle3.png'), pygame.image.load('GlobMonster/Idle/RIdle4.png'), pygame.image.load('GlobMonster/Idle/RIdle5.png')]
globIdleLeft = [pygame.image.load('GlobMonster/Idle/LIdle1.png'), pygame.image.load('GlobMonster/Idle/LIdle2.png'), pygame.image.load('GlobMonster/Idle/LIdle3.png'), pygame.image.load('GlobMonster/Idle/LIdle4.png'), pygame.image.load('GlobMonster/Idle/LIdle5.png')]
globDeath = [pygame.image.load('GlobMonster/Death/Death1.png'), pygame.image.load('GlobMonster/Death/Death2.png'), pygame.image.load('GlobMonster/Death/Death3.png')]
globAttackIdle = [pygame.image.load('GlobMonster/Attack/Idle1.png'), pygame.image.load('GlobMonster/Attack/Idle2.png'), pygame.image.load('GlobMonster/Attack/Idle3.png'), pygame.image.load('GlobMonster/Attack/Idle4.png')]
globAttackActive = [pygame.image.load('GlobMonster/Attack/Active1.png'), pygame.image.load('GlobMonster/Attack/Active2.png'), pygame.image.load('GlobMonster/Attack/Active3.png'), pygame.image.load('GlobMonster/Attack/Active4.png'), pygame.image.load('GlobMonster/Attack/Active5.png'), pygame.image.load('GlobMonster/Attack/Active6.png')]

botIdleRight = [pygame.image.load('Bot/Idle/RIdle1.png'), pygame.image.load('Bot/Idle/RIdle2.png'), pygame.image.load('Bot/Idle/RIdle3.png')]
botIdleLeft = [pygame.image.load('Bot/Idle/LIdle1.png'), pygame.image.load('Bot/Idle/LIdle2.png'), pygame.image.load('Bot/Idle/LIdle3.png')]
botTalkRight = [pygame.image.load('Bot/Talking/RTalk1.png'), pygame.image.load('Bot/Talking/RTalk2.png'), pygame.image.load('Bot/Talking/RTalk3.png')]
botTalkLeft = [pygame.image.load('Bot/Talking/LTalk1.png'), pygame.image.load('Bot/Talking/LTalk2.png'), pygame.image.load('Bot/Talking/LTalk3.png')]

screenWidth = 1152
screenHeight = 640

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
        
    def draw(self, win):
        if self.walkCount >= 15:
            self.walkCount = 0
        if self.idleCount >= 24:
            self.idleCount = 0
        if self.isMoving and self.onGround:
            if self.left:
                win.blit(runLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(runRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        elif self.yVel >= 0 and not(self.onGround):
            if self.left:
                win.blit(jumpLeft[0], (self.x, self.y))
            elif self.right:
                win.blit(jumpRight[0], (self.x, self.y))
        elif self.yVel < 0 and not(self.onGround):
            if self.left:
                win.blit(jumpLeft[1], (self.x, self.y))
            elif self.right:
                win.blit(jumpRight[1], (self.x, self.y))
        else:
            if self.left:
                win.blit(idleLeft[self.idleCount//6], (self.x, self.y))
                self.idleCount+=1
            else:
                win.blit(idleRight[self.idleCount//6], (self.x, self.y))
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

class baddy():
    def __init__(self, x, y, distance, myLevel):
        self.x = 64 * x - 22
        self.y = 64 * y - 96
        self.width = 96
        self.height = 96
        
        self.vel = 4
        self.right = True
        self.hitbox = [33, 51, 27, 45]
        self.path = [(64 * x - 22), (64 * x - 22) + (64 * distance + 18)]
        self.level = myLevel
        self.walkCount = 0
        self.dead = False
        
    def draw(self, win, levelNum):
        if levelNum == self.level:
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

                    win.blit(baddyWalkRight[self.walkCount//5], (self.x, self.y))
                    
                else:
                    if self.x > self.path[0]:
                        self.x -= self.vel
                        self.walkCount += 1
                    else:
                        self.right = True
                        self.walkCount = 0

                    win.blit(baddyWalkLeft[self.walkCount//5], (self.x, self.y))

class globAttack():
    def __init__(self, x, y):
        self.x = x * 64
        self.y = y * 64
        self.hitbox = [0, 40, 64, 24]
        self.active = False
        
    def draw(self, state, count):
        if state == 1:
            win.blit(globAttackIdle[count], (self.x, self.y))
            self.active = False
        else:
            win.blit(globAttackActive[count], (self.x, self.y))
            self.active = True

class glob():
    def __init__(self):
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

    def draw(self, levelNum):
        if levelNum == self.level:
            if self.health <= 0 and self.deathCount < 12:
                self.dead = True
                win.blit(globDeath[self.deathCount//4], (self.x, self.y))
                self.deathCount += 1
            elif self.health > 0:
                if self.idleCount >= 20:
                    self.idleCount = 0
                if man.x + man.hitbox[0] + (man.hitbox[2] // 2) < self.x + (self.width // 2):
                    self.left = True
                    win.blit(globIdleLeft[self.idleCount//4], (self.x, self.y))
                else:
                    self.left = False
                    win.blit(globIdleRight[self.idleCount//4], (self.x, self.y))
                self.idleCount += 1

    def drawHealth(self, levelNum):
        if self.start:
            if levelNum == self.level and self.health > 0:
                pygame.draw.rect(win, (100, 100, 100), [self.x + self.hitbox[0] + self.hitbox[2] // 2 - 50, self.y + self.hitbox[1] - 18, 100, 10])
                pygame.draw.rect(win, (255, 0, 0), [self.x + self.hitbox[0] + self.hitbox[2] // 2 - 50, self.y + self.hitbox[1] - 18, self.health*2, 10])

    def attack(self, levelNum):
        if self.start:
            if levelNum == self.level and not(self.dead):
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
                        item.draw(1, self.attackIdleCount // 3)
                    self.attackIdleCount += 1
                elif self.attackCount < self.attackTime * 2:
                    #Left Attack
                    if self.attackActiveCount >= 18:
                        self.attackActiveCount = 0
                    for item in self.leftList:
                        item.draw(2, self.attackActiveCount // 3)
                    self.attackActiveCount += 1
                elif self.attackCount < self.attackTime * 3:
                    #Right Idle
                    self.attackRight = True
                    if self.attackIdleCount >= 12:
                        self.attackIdleCount = 0
                    for item in self.rightList:
                        item.draw(1, self.attackIdleCount // 3)
                    self.attackIdleCount += 1
                elif self.attackCount < self.attackTime * 4:
                    #Right Attack
                    if self.attackActiveCount >= 18:
                        self.attackActiveCount = 0
                    for item in self.rightList:
                        item.draw(2, self.attackActiveCount // 3)
                    self.attackActiveCount += 1
                else:
                    self.attackCount = 0
                self.attackCount += 1
    
class block():
    def __init__(self, x, y, img, state = 1):
        self.x = x
        self.y = y
        self.img = img
        self.state = state
        self.verticalBuffer = 0
        if self.img == grass:
            self.verticalBuffer = 4

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

class button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.show = False

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            return True
        return False

def refresh(levelNum, bgCount):
    win.blit(bg, (int(-16 * bgCount), 0))
    man.draw(win)
    for bullet in bullets:
        if not(bullet.hide):
            bullet.draw(win)
    for platform in platforms:
        platform.draw(win)
    for badGuy in badGuys:
        badGuy.draw(win, levelNum)
    man.draw(win)
    glob.draw(levelNum)
    glob.drawHealth(levelNum)
    glob.attack(levelNum)
    for i in range(man.lives):
        win.blit(heart, (2 + (64 * i), 64 * 9 + 4))
    #pygame.draw.rect(win, (255, 0, 0), [man.x + man.hitbox[0], man.y + man.hitbox[1], man.hitbox[2], man.hitbox[3]], 1) # For testing
    pygame.display.update()

def runGame(bgCount, levelNum, bullets, bulletsNum):
    levelReset = False
    run = True
    while run:
        clock.tick(30)

        #Creating platforms for the specific level
        if man.x + man.hitbox[0] + 8 > screenWidth:
            levelNum += 1
            bullets.clear()
            bulletsNum = 0
            man.x = 8 - man.hitbox[0] - man.hitbox[2]
            bgCount += 72
            level = levels[levelNum - 1]
            for platform in platforms:
                del platform
            platforms.clear()
            for i in range(10):
                for j in range(18):
                    if level[i][j] == 1:
                        platforms.append(block(64*j, 64*i - 4, grass))
                    elif level[i][j] == 2:
                        platforms.append(block(64*j, 64*i, dirt))
                    elif level[i][j] == 3:
                        platforms.append(block(64*j, 64*i, spike, 2))

        #Redraws the level if the level changes
        if levelReset == True:
            level = levels[levelNum - 1]
            for platform in platforms:
                del platform
            platforms.clear()
            for i in range(10):
                for j in range(18):
                    if level[i][j] == 1:
                        platforms.append(block(64*j, 64*i - 4, grass))
                    elif level[i][j] == 2:
                        platforms.append(block(64*j, 64*i, dirt))
                    elif level[i][j] == 3:
                        platforms.append(block(64*j, 64*i, spike, 2))
            
            levelReset = False

        #Respawning
        if man.dead:
            if levelNum == 1:
                man.x = 41
                man.y = -90
            elif levelNum == 5:
                man.x = 64 * 9 - man.hitbox[0] - man.hitbox[2] // 2
                man.y = 32
            else:
                man.x = -23
                man.y = 64 * 8 - man.hitbox[1] - man.hitbox[3] - 5
            man.lives -=1
            man.yVel = 0
            man.dead = False
            man.right = True
            man.left = False
            bullets.clear()
            bulletsNum = 0
            for badGuy in badGuys:
                if badGuy.level == levelNum:
                    badGuy.dead = False
                    badGuy.right = True
                    badGuy.x = badGuy.path[0]

        #Bullet moves and disappears when hits a platform or goes off screen
        for bullet in bullets:
            for platform in platforms:
                if bullet.direction == 1:
                    if bullet.y - bullet.radius <= platform.y + 64 and bullet.y + bullet.radius >= platform.y and bullet.x - bullet.radius > platform.x and bullet.x - bullet.radius < platform.x + 20:
                        if not(bullet.hide):
                            bullet.hide = True
                            bulletsNum -= 1
                else:
                    if bullet.y - bullet.radius <= platform.y + 64 and bullet.y + bullet.radius >= platform.y and bullet.x + bullet.radius < platform.x + 64 and bullet.x + bullet.radius > platform.x + 44:
                        if not(bullet.hide):
                            bullet.hide = True
                            bulletsNum -= 1
            if bullet.x < screenWidth and bullet.x > 0:
                if not(bullet.hide):
                    bullet.x += bullet.vel
            else:
                if not(bullet.hide):
                    bullet.hide = True
                    bulletsNum -= 1

        keys = pygame.key.get_pressed()

        #Delays the user's shot
        if man.gunCount == 5:
            man.gunCount = 0
        if man.gunCount >= 1 and man.gunCount < 5:
            man.gunCount +=1

        #Shoots on space
        if levelNum != 5 or (levelNum == 5 and glob.start):
            if man.gunCount == 0:
                if keys[pygame.K_SPACE]:
                    if bulletsNum < 5:
                        if man.right:
                            direction = 1
                            bullets.append(projectile(man.x + man.hitbox[0] + man.hitbox[2], man.y + man.hitbox[1] + 35, 3, (0,0,0), direction))
                        else:
                            direction = -1
                            bullets.append(projectile(man.x + man.hitbox[0], man.y + man.hitbox[1] + 35, 3, (0,0,0), direction))
                        man.gunCount = 1
                        bulletsNum += 1

        #Figures out if touching a wall or ground
        man.onGround = False
        man.rightWall = False
        man.leftWall = False
        for platform in platforms:
            if man.y + man.hitbox[1] + man.hitbox[3] == platform.y + platform.verticalBuffer and man.x + man.hitbox[0] < platform.x + 64 and man.x + man.hitbox[0] + man.hitbox[2] > platform.x:
                man.onGround = True
                if platform.state == 2:
                    man.dead = True
            if man.y + man.hitbox[1] + man.hitbox[3] > platform.y + platform.verticalBuffer and man.y + man.hitbox[1] < platform.y + 64:
                if man.x + man.hitbox[0] >= platform.x + 40 and man.x + man.hitbox[0] <= platform.x + 70:
                    man.leftWall = True
                    if platform.state == 2:
                        man.dead = True
                    if man.x + man.hitbox[0] < platform.x + 64:
                        man.x += ((platform.x + 64)-(man.x + man.hitbox[0]))
                if man.x + man.hitbox[0] + man.hitbox[2] <= platform.x + 24 and man.x + man.hitbox[0] + man.hitbox[2] >= platform.x - 6:
                    man.rightWall = True
                    if platform.state == 2:
                        man.dead = True
                    if man.x + man.hitbox[0] + man.hitbox[2] > platform.x:
                        man.x -= ((man.x + man.hitbox[0] + man.hitbox[2])-(platform.x))

        #If off ground, constantly accelerating down
        #Jumps on up key
        if not(man.onGround):
            man.yVel -= 2
        else:
            if keys[pygame.K_UP]:        
                man.yVel = 24

        #Goes down unless he hits the ground
        if man.yVel<0:
            for i in range(man.yVel*-1):
                if not(man.onGround):
                    man.y += 1
                    for platform in platforms:
                        if man.y + man.hitbox[1] + man.hitbox[3] >= platform.y + platform.verticalBuffer and man.y + man.hitbox[1] + man.hitbox[3] <= platform.y + 8 and man.x + man.hitbox[0] < platform.x + 64 and man.x + man.hitbox[0] + man.hitbox[2] > platform.x:
                            man.onGround = True
                            if platform.state == 2:
                                man.dead = True
                            break
                else:
                    man.yVel=0
                    break
        #Goes up unless it hits the cieling
        else:
            for i in range(man.yVel):
                if not(man.onCieling):
                    man.y -= 1
                    if man.y + man.hitbox[1] <= 0:
                        man.yVel = 0
                        man.onCieling = True
                    for platform in platforms:
                        if man.y + man.hitbox[1] <= platform.y + 64  and man.y + man.hitbox[1] >= platform.y + 60 and man.x + man.hitbox[0] < platform.x + 64 and man.x + man.hitbox[0] + man.hitbox[2] > platform.x:
                            man.yVel = 0
                            man.onCieling = True
                            if platform.state == 2:
                                man.dead = True
                            break
            man.onCieling = False
        

        #Move right on right key
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not(man.rightWall):
            man.x += man.xVel
            man.left = False
            man.right = True
            man.isMoving = True

        #Move left on left key
        elif keys[pygame.K_LEFT] and man.x + man.hitbox[0] >= man.xVel and not keys[pygame.K_RIGHT] and not(man.leftWall):
            man.x -= man.xVel
            man.left = True
            man.right = False
            man.isMoving = True
        else:
            man.isMoving = False
            man.walkCount = 0

        #Dies if falls out of world
        if man.y + man.hitbox[1] > screenHeight:
            man.dead = True

        #Dies if touches a bad guy
        #Bullets kill bad guys
        for badGuy in badGuys:
            if not(badGuy.dead) and badGuy.level == levelNum:
                if badGuy.y + badGuy.hitbox[1] < man.y + man.hitbox[1] + man.hitbox[3] and badGuy.y + badGuy.hitbox[1] + badGuy.hitbox[3] > man.y + man.hitbox[1]:
                    if badGuy.x + badGuy.hitbox[0] < man.x + man.hitbox[0] + man.hitbox[2] and badGuy.x + badGuy.hitbox[0] + badGuy.hitbox[2] > man.x + man.hitbox[0]:
                        man.dead = True
                for bullet in bullets:
                    if not(bullet.hide):
                        if badGuy.y + badGuy.hitbox[1] < bullet.y + bullet.radius and badGuy.y + badGuy.hitbox[1] + badGuy.hitbox[3] > bullet.y - bullet.radius:
                            if badGuy.x + badGuy.hitbox[0] < bullet.x + bullet.radius and badGuy.x + badGuy.hitbox[0] + badGuy.hitbox[2] > bullet.x - bullet.radius:
                                bullet.hide = True
                                bulletsNum -= 1
                                badGuy.dead = True

        #First Boss Battle
        if levelNum == 5 and not(glob.dead):
            for bullet in bullets:
                if not(bullet.hide):
                    if glob.y + glob.hitboxThree[1] < bullet.y + bullet.radius and glob.y + glob.hitboxThree[1] + glob.hitboxThree[3] > bullet.y - bullet.radius:
                        if glob.x + glob.hitboxThree[0] < bullet.x + bullet.radius and glob.x + glob.hitboxThree[0] + glob.hitboxThree[2] > bullet.x - bullet.radius:
                            bullet.hide = True
                            bulletsNum -= 1
                            glob.health -= 1
            if (glob.y + glob.hitbox[1] < man.y + man.hitbox[1] + man.hitbox[3] and glob.y + glob.hitbox[1] + glob.hitbox[3] > man.y + man.hitbox[1] and glob.x + glob.hitbox[0] < man.x + man.hitbox[0] + man.hitbox[2] and glob.x + glob.hitbox[0] + glob.hitbox[2] > man.x + man.hitbox[0]) or (glob.y + glob.hitboxTwo[1] < man.y + man.hitbox[1] + man.hitbox[3] and glob.y + glob.hitboxTwo[1] + glob.hitboxTwo[3] > man.y + man.hitbox[1] and glob.x + glob.hitboxTwo[0] < man.x + man.hitbox[0] + man.hitbox[2] and glob.x + glob.hitboxTwo[0] + glob.hitboxTwo[2] > man.x + man.hitbox[0]):
                man.dead = True
            if glob.attackRight:
                for item in glob.rightList:
                    if item.active:
                        if (item.y + item.hitbox[1] < man.y + man.hitbox[1] + man.hitbox[3] and item.y + item.hitbox[1] + item.hitbox[3] > man.y + man.hitbox[1] and item.x + item.hitbox[0] < man.x + man.hitbox[0] + man.hitbox[2] and item.x + item.hitbox[0] + item.hitbox[2] > man.x + man.hitbox[0]):
                            man.dead = True
            else:
                for item in glob.leftList:
                    if item.active: 
                        if (item.y + item.hitbox[1] < man.y + man.hitbox[1] + man.hitbox[3] and item.y + item.hitbox[1] + item.hitbox[3] > man.y + man.hitbox[1] and item.x + item.hitbox[0] < man.x + man.hitbox[0] + man.hitbox[2] and item.x + item.hitbox[0] + item.hitbox[2] > man.x + man.hitbox[0]):
                            man.dead = True
            if not(glob.start):
                if man.x + man.hitbox[0] > 64:
                    glob.start = True
                    levels[4][7][0] = 2
                    levels[4][8][0] = 2
                    levelReset = True
            if glob.health <= 0:
                levels[4][7][17] = 0
                levels[4][8][17] = 1
                levelReset = True
        
        #Keeps the clouds moving
        bgCount += 0.125
        if bgCount >= 144:
            bgCount -= 144

        #Game Over
        if man.lives == 0:
            run = False
        
        #Draws everything and refreshes the screen
        refresh(levelNum, bgCount)

        #X or Escape button to close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                global runEverything
                runEverything = False
        if keys[pygame.K_ESCAPE]:
            run = False
            runEverything = False


#________________________________________________________________

man = player(41, -90, 96, 96, 31, 36, 32, 60)
badGuys = [baddy(8, 8, 2, 1),
           baddy(2, 5, 9, 2), baddy(3, 8, 9, 2), baddy(3, 2, 9, 2), 
           baddy(4, 6, 1, 3), baddy(8, 4, 1, 3), baddy(12, 6, 1, 3),
           baddy(12, 5, 2, 4), baddy(6, 6, 2, 4)]
glob = glob()
bullets = []

play = button(128, 272, 240, 80)
menuAbout = button(128, 400, 304, 80)
playAgain = button(16, 448, 304, 176)
gameOverAbout = button(832, 544, 288, 80)

level1_1 = [[2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
           [2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2]]

level1_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

level1_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0],
           [1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 1, 1],
           [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2]]

level1_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]]

level1_5 = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

level1_6 = [[2, 0, 2, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
           [2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
           [2, 0, 2, 0, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
           [2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
           [2, 0, 2, 0, 0, 0, 1, 1, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0],
           [2, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
           [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 1, 0, 2],
           [0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 1, 2],
           [1, 1, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2],
           [2, 2, 2, 0, 2, 1, 2, 1, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2]]

levels = [level1_1, level1_2, level1_3, level1_4, level1_5, level1_6]

bgCount = 0
platforms = []

isMainMenu = True
menuCount = 0
isGame = False
isGameOver = False

runEverything = True
while runEverything:
    while isMainMenu:
        clock.tick(30)
        if menuCount >= 21:
            menuCount = 0
        win.blit(mainMenu[menuCount//3], (0, 0))
        menuCount += 1
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                isMainMenu = False
                runEverything = False

            if event.type == pygame.MOUSEMOTION:
                if play.isOver(pos):
                    play.show = True
                else:
                    play.show = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.isOver(pos):
                    isMainMenu = False
                    isGame = True
                    play.show = False
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isMainMenu = False
            runEverything = False
            
        if play.show:
            win.blit(playButton, (play.x, play.y))
            
        pygame.display.update()

    if isGame:
        man.x = 41
        man.y = -90
        man.yVel = 0
        man.lives = man.maxLives
        bulletsNum = 0

        levelNum = 1
        level = levels[0]

        for platform in platforms:
            del platform
        platforms.clear()
        for i in range(10):
            for j in range(18):
                if level[i][j] == 1:
                    platforms.append(block(64*j, 64*i - 4, grass))
                elif level[i][j] == 2:
                    platforms.append(block(64*j, 64*i, dirt))
                elif level[i][j] == 3:
                    platforms.append(block(64*j, 64*i, spike, 2))
        
        for badGuy in badGuys:
            badGuy.dead = False
            badGuy.right = True
            badGuy.x = badGuy.path[0]
        glob.start = False
        glob.health = 50
        glob.dead = False
        glob.deathCount = 0
        glob.attackCount = 0
        for item in glob.leftList:
            item.active = False
        for item in glob.rightList:
            item.active = False
        levels[4][7][0] = 0
        levels[4][8][0] = 1
        
        runGame(bgCount, levelNum, bullets, bulletsNum)

        if runEverything:
            isGameOver = True
        isGame = False

    while isGameOver:
        win.blit(gameOver, (0, 0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                isGameOver = False
                runEverything = False

            if event.type == pygame.MOUSEMOTION:
                if playAgain.isOver(pos):
                    playAgain.show = True
                else:
                    playAgain.show = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgain.isOver(pos):
                    isGameOver = False
                    isMainMenu = True
                    playAgain.show = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isGameOver = False
            runEverything = False
        
        if playAgain.show:
            win.blit(playAgainButton, (playAgain.x, playAgain.y))
            
        pygame.display.update()

pygame.quit()
