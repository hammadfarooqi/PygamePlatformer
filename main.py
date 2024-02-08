"""
Hammad Farooqi
Pygame Platformer
"""
import pygame
from Levels import *
from SaveFile import *
from Player import *
from Enemies import *
from Visuals import *
from load import *
pygame.init()

screenWidth = 1152
screenHeight = 640

def refresh(worldNum, levelNum, platforms, bgCount):
    win.blit(bg, (int(-16 * bgCount), 0))
    man.draw(win, animations)
    for bullet in bullets:
        if not(bullet.hide):
            bullet.draw(win)
    for platform in platforms:
        platform.draw(win)
    for badGuy in badGuys:
        badGuy.draw(win, animations, levelNum, worldNum)
    man.draw(win, animations)
    glob.draw(win, animations, man, levelNum, worldNum)
    glob.drawHealth(win, levelNum, worldNum)
    glob.attack(win, animations, levelNum, worldNum)
    for i in range(man.lives):
        win.blit(heart, (2 + (64 * i), 64 * 9 + 4))
    #pygame.draw.rect(win, (255, 0, 0), [man.x + man.hitbox[0], man.y + man.hitbox[1], man.hitbox[2], man.hitbox[3]], 1) # For testing
    pygame.display.update()

def runGame(bgCount, worldNum, levelNum, bullets, bulletsNum):
    levelReset = True
    run = True
    while run:
        clock.tick(30)

        #Creating platforms for the specific level when you progress a level
        if man.x + man.hitbox[0] + 8 > screenWidth:
            levelNum += 1
            if levelNum > len(levels[worldNum-1]):
                levelNum = 1
                worldNum += 1
            bullets.clear()
            bulletsNum = 0
            man.x = 8 - man.hitbox[0] - man.hitbox[2]
            bgCount += 72
            level = levels[worldNum-1][levelNum - 1]
            platforms = loadPlatforms(level)

        #Redraws the level if the level changes
        if levelReset == True:
            level = levels[worldNum-1][levelNum - 1]
            platforms = loadPlatforms(level)
            
            levelReset = False

        #Respawning
        if man.dead:
            if worldNum == 1 and levelNum == 1:
                man.x = 41
                man.y = -90
            elif worldNum == 1 and levelNum == 5:
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
                if badGuy.world == worldNum and badGuy.level == levelNum:
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
        if worldNum != 1 or levelNum != 5 or (levelNum == 5 and glob.start):
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
            if keys[pygame.K_w]:        
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
        if keys[pygame.K_d] and not keys[pygame.K_a] and not(man.rightWall):
            man.x += man.xVel
            man.left = False
            man.right = True
            man.isMoving = True

        #Move left on left key
        elif keys[pygame.K_a] and man.x + man.hitbox[0] >= man.xVel and not keys[pygame.K_d] and not(man.leftWall):
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
            if not(badGuy.dead) and badGuy.world == worldNum and badGuy.level == levelNum:
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
        if worldNum == 1 and levelNum == 5 and not(glob.dead):
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
                    levels[0][4][7][0] = 2
                    levels[0][4][8][0] = 2
                    levelReset = True
            if glob.health <= 0:
                levels[0][4][7][17] = 0
                levels[0][4][8][17] = 1
                levelReset = True
        
        #Keeps the clouds moving
        bgCount += 0.125
        if bgCount >= 144:
            bgCount -= 144

        #Game Over
        if man.lives == 0:
            run = False
            file = open("PygamePlatformer2SaveFile.py", "w")
            file.write("worldNum = "+str(worldNum)+ "\n")
            file.write("levelNum = 1\n")
            file.write("lives = 5")
            file.close()
        
        #Draws everything and refreshes the screen
        refresh(worldNum, levelNum, platforms, bgCount)

        #X or Escape button to close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                global runEverything
                runEverything = False
                file = open("PygamePlatformer2SaveFile.py", "w")
                file.write("worldNum = "+str(worldNum)+ "\n")
                file.write("levelNum = "+str(levelNum)+ "\n")
                file.write("lives = "+str(man.lives))
                file.close()
        if keys[pygame.K_ESCAPE]:
            run = False
            runEverything = False
            file = open("PygamePlatformer2SaveFile.py", "w")
            file.write("worldNum = "+str(worldNum)+ "\n")
            file.write("levelNum = "+str(levelNum)+ "\n")
            file.write("lives = "+str(man.lives))
            file.close()
    return worldNum


#________________________________________________________________

man = player(41, -90, 96, 96, 31, 36, 32, 60)
badGuys = [baddy(8, 8, 2, 1),
           baddy(2, 5, 9, 2), baddy(3, 8, 9, 2), baddy(3, 2, 9, 2), 
           baddy(4, 6, 1, 3), baddy(8, 4, 1, 3), baddy(12, 6, 1, 3),
           baddy(12, 5, 2, 4), baddy(6, 6, 2, 4)]
glob = glob(screenWidth)
bullets = []

bgCount = 0

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

        continueGame.active = True
        if levelNum == 1 and worldNum == 1 and lives == 5:
            continueGame.active = False
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                isMainMenu, runEverything = False

            if event.type == pygame.MOUSEMOTION:
                if play.isOver(pos):
                    play.show = True
                else:
                    play.show = False
                if continueGame.isOver(pos) and continueGame.active:
                    continueGame.show = True
                else:
                    continueGame.show = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.isOver(pos):
                    isMainMenu = False
                    isGame = True
                    play.show = False
                    levelNum = 1
                    worldNum = 1
                    lives = 5
                if continueGame.isOver(pos) and continueGame.active:
                    isMainMenu = False
                    isGame = True
                    continueGame.show = False
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isMainMenu = False
            runEverything = False
            
        if play.show:
            win.blit(playButton, (play.x, play.y))
        if continueGame.active:
            win.blit(continueButton[0], (continueGame.x, continueGame.y))
        if continueGame.show:
            win.blit(continueButton[1], (continueGame.x, continueGame.y))
            
        pygame.display.update()

    if isGame:
        if worldNum == 1 and levelNum == 1:
            man.x = 41
            man.y = -90
        elif worldNum == 1 and levelNum == 5:
            man.x = 64 * 9 - man.hitbox[0] - man.hitbox[2] // 2
            man.y = 32
        else:
            man.x = -23
            man.y = 64 * 8 - man.hitbox[1] - man.hitbox[3] - 5
        man.yVel = 0
        man.lives = lives
        bulletsNum = 0

        level = levels[worldNum-1][levelNum-1]
        
        #Reseting World 1 Hostiles
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
        levels[0][4][7][0] = 0
        levels[0][4][8][0] = 1
        
        worldNum = runGame(bgCount, worldNum, levelNum, bullets, bulletsNum)
        levelNum = 1
        lives = man.maxLives

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
