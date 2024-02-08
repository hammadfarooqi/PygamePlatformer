import pygame
from Visuals import *

def loadPlatforms(level):
    platforms = []
    for i in range(10):
        for j in range(18):
            if level[i][j] == 1:
                platforms.append(block(64*j, 64*i - 4, "grass"))
            elif level[i][j] == 2:
                platforms.append(block(64*j, 64*i, "dirt"))
            elif level[i][j] == 3:
                platforms.append(block(64*j, 64*i, "brickFloor"))
            elif level[i][j] == 4:
                platforms.append(block(64*j, 64*i, "brick"))


pygame.init()

win = pygame.display.set_mode((1152, 640))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

# Load background images
mainMenu = [pygame.image.load('Backgrounds/MainMenu/MainMenu1.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu2.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu3.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu4.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu5.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu6.png').convert(), pygame.image.load('Backgrounds/MainMenu/MainMenu7.png').convert()]
bg = pygame.image.load('Backgrounds/bg.png').convert()
gameOver = pygame.image.load('Backgrounds/GameOver.png').convert()

# Load button images
playButton = pygame.image.load('Buttons/PlayButton.png').convert_alpha()
menuAboutButton = pygame.image.load('Buttons/MenuAboutButton.png').convert_alpha()
continueButton = [pygame.image.load('Buttons/ContinueButtonDark.png').convert_alpha(), pygame.image.load('Buttons/ContinueButtonLight.png').convert_alpha()]
playAgainButton = pygame.image.load('Buttons/PlayAgainButton.png').convert_alpha()
gameOverAboutButton = pygame.image.load('Buttons/GameOverAboutButton.png').convert_alpha()

# Load buttons
play = button(128, 272, 240, 80)
menuAbout = button(128, 400, 304, 80)
continueGame = button(128, 176, 496, 80)
playAgain = button(16, 448, 304, 176)
gameOverAbout = button(832, 544, 288, 80)

# Load block images
blockImages = {}
blockImages["grass"] = pygame.image.load('Environment/GrassBlock.png').convert_alpha()
blockImages["dirt"] = pygame.image.load('Environment/DirtBlock.png').convert()
blockImages["brick"] = pygame.image.load('Environment/Brick.png').convert()
blockImages["brickFloor"] = pygame.image.load('Environment/BrickFloor.png').convert()
# blockImages["spike"] = pygame.image.load('Environment/Spike.png').convert_alpha()
heart = pygame.image.load('Man/Heart.png').convert_alpha()

# Load all animations
animations = {}

# Load player animations
animations["runRight"] = [pygame.image.load('Man/Running/RRun1.png').convert_alpha(), pygame.image.load('Man/Running/RRun2.png').convert_alpha(), pygame.image.load('Man/Running/RRun3.png').convert_alpha(), pygame.image.load('Man/Running/RRun4.png').convert_alpha(), pygame.image.load('Man/Running/RRun5.png').convert_alpha()]
animations["runLeft"] = [pygame.image.load('Man/Running/LRun1.png').convert_alpha(), pygame.image.load('Man/Running/LRun2.png').convert_alpha(), pygame.image.load('Man/Running/LRun3.png').convert_alpha(), pygame.image.load('Man/Running/LRun4.png').convert_alpha(), pygame.image.load('Man/Running/LRun5.png').convert_alpha()]
animations["idleRight"] = [pygame.image.load('Man/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Man/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Man/Idle/RIdle3.png').convert_alpha(), pygame.image.load('Man/Idle/RIdle4.png').convert_alpha()]
animations["idleLeft"] = [pygame.image.load('Man/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Man/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Man/Idle/LIdle3.png').convert_alpha(), pygame.image.load('Man/Idle/LIdle4.png').convert_alpha()]
animations["jumpRight"] = [pygame.image.load('Man/Jumping/RUp.png').convert_alpha(), pygame.image.load('Man/Jumping/RDown.png').convert_alpha()]
animations["jumpLeft"] = [pygame.image.load('Man/Jumping/LUp.png').convert_alpha(), pygame.image.load('Man/Jumping/LDown.png').convert_alpha()]

# Load baddy animations
animations["baddyWalkRight"] = [pygame.image.load('Baddy/Walking/RWalk1.png').convert_alpha(), pygame.image.load('Baddy/Walking/RWalk2.png').convert_alpha(), pygame.image.load('Baddy/Walking/RWalk3.png').convert_alpha(), pygame.image.load('Baddy/Walking/RWalk4.png').convert_alpha(), pygame.image.load('Baddy/Walking/RWalk5.png').convert_alpha()]
animations["baddyWalkLeft"] = [pygame.image.load('Baddy/Walking/LWalk1.png').convert_alpha(), pygame.image.load('Baddy/Walking/LWalk2.png').convert_alpha(), pygame.image.load('Baddy/Walking/LWalk3.png').convert_alpha(), pygame.image.load('Baddy/Walking/LWalk4.png').convert_alpha(), pygame.image.load('Baddy/Walking/LWalk5.png').convert_alpha()]
animations["baddyIdleRight"] = [pygame.image.load('Baddy/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Baddy/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Baddy/Idle/RIdle3.png').convert_alpha(), pygame.image.load('Baddy/Idle/RIdle4.png').convert_alpha()]
animations["baddyIdleLeft"] = [pygame.image.load('Baddy/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Baddy/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Baddy/Idle/LIdle3.png').convert_alpha(), pygame.image.load('Baddy/Idle/LIdle4.png').convert_alpha()]

# Load boss animations
animations["globIdleRight"] = [pygame.image.load('GlobMonster/Idle/RIdle1.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/RIdle2.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/RIdle3.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/RIdle4.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/RIdle5.png').convert_alpha()]
animations["globIdleLeft"] = [pygame.image.load('GlobMonster/Idle/LIdle1.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/LIdle2.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/LIdle3.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/LIdle4.png').convert_alpha(), pygame.image.load('GlobMonster/Idle/LIdle5.png').convert_alpha()]
animations["globDeath"] = [pygame.image.load('GlobMonster/Death/Death1.png').convert_alpha(), pygame.image.load('GlobMonster/Death/Death2.png').convert_alpha(), pygame.image.load('GlobMonster/Death/Death3.png').convert_alpha()]
animations["globAttackIdle"] = [pygame.image.load('GlobMonster/Attack/Idle1.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Idle2.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Idle3.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Idle4.png').convert_alpha()]
animations["globAttackActive"] = [pygame.image.load('GlobMonster/Attack/Active1.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Active2.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Active3.png').convert_alpha(), pygame.image.load('GlobMonster/Attack/Active4.png'), pygame.image.load('GlobMonster/Attack/Active5.png'), pygame.image.load('GlobMonster/Attack/Active6.png').convert_alpha()]

# Load bot animations (not used)
# animations["botIdleRight"] = [pygame.image.load('Bot/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Bot/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Bot/Idle/RIdle3.png').convert_alpha()]
# animations["botIdleLeft"] = [pygame.image.load('Bot/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Bot/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Bot/Idle/LIdle3.png').convert_alpha()]
# animations["botTalkRight"] = [pygame.image.load('Bot/Talking/RTalk1.png').convert_alpha(), pygame.image.load('Bot/Talking/RTalk2.png').convert_alpha(), pygame.image.load('Bot/Talking/RTalk3.png').convert_alpha()]
# animations["botTalkLeft"] = [pygame.image.load('Bot/Talking/LTalk1.png').convert_alpha(), pygame.image.load('Bot/Talking/LTalk2.png').convert_alpha(), pygame.image.load('Bot/Talking/LTalk3.png').convert_alpha()]
