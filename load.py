import pygame
from Engine.Visuals import *
from Engine.Player import *
from Engine.Enemies import *


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
    return platforms

pygame.init()

screenWidth = 1152
screenHeight = 640
win = pygame.display.set_mode((1152, 640))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

# Load background images
mainMenu = [pygame.image.load('Images/Backgrounds/MainMenu/MainMenu1.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu2.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu3.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu4.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu5.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu6.png').convert(), pygame.image.load('Images/Backgrounds/MainMenu/MainMenu7.png').convert()]
bg = pygame.image.load('Images/Backgrounds/bg.png').convert()
gameOver = pygame.image.load('Images/Backgrounds/GameOver.png').convert()

# Load button images
playButton = pygame.image.load('Images/Buttons/PlayButton.png').convert_alpha()
menuAboutButton = pygame.image.load('Images/Buttons/MenuAboutButton.png').convert_alpha()
continueButton = [pygame.image.load('Images/Buttons/ContinueButtonDark.png').convert_alpha(), pygame.image.load('Images/Buttons/ContinueButtonLight.png').convert_alpha()]
playAgainButton = pygame.image.load('Images/Buttons/PlayAgainButton.png').convert_alpha()
gameOverAboutButton = pygame.image.load('Images/Buttons/GameOverAboutButton.png').convert_alpha()

# Load buttons
play = button(128, 272, 240, 80)
menuAbout = button(128, 400, 304, 80)
continueGame = button(128, 176, 496, 80)
playAgain = button(16, 448, 304, 176)
gameOverAbout = button(832, 544, 288, 80)

# Load block images
blockImages = {}
blockImages["grass"] = pygame.image.load('Images/Environment/GrassBlock.png').convert_alpha()
blockImages["dirt"] = pygame.image.load('Images/Environment/DirtBlock.png').convert()
blockImages["brick"] = pygame.image.load('Images/Environment/Brick.png').convert()
blockImages["brickFloor"] = pygame.image.load('Images/Environment/BrickFloor.png').convert()
# blockImages["spike"] = pygame.image.load('Images/Environment/Spike.png').convert_alpha()
heart = pygame.image.load('Images/Man/Heart.png').convert_alpha()

# Load all animations
animations = {}

# Load player animations
animations["runRight"] = [pygame.image.load('Images/Man/Running/RRun1.png').convert_alpha(), pygame.image.load('Images/Man/Running/RRun2.png').convert_alpha(), pygame.image.load('Images/Man/Running/RRun3.png').convert_alpha(), pygame.image.load('Images/Man/Running/RRun4.png').convert_alpha(), pygame.image.load('Images/Man/Running/RRun5.png').convert_alpha()]
animations["runLeft"] = [pygame.image.load('Images/Man/Running/LRun1.png').convert_alpha(), pygame.image.load('Images/Man/Running/LRun2.png').convert_alpha(), pygame.image.load('Images/Man/Running/LRun3.png').convert_alpha(), pygame.image.load('Images/Man/Running/LRun4.png').convert_alpha(), pygame.image.load('Images/Man/Running/LRun5.png').convert_alpha()]
animations["idleRight"] = [pygame.image.load('Images/Man/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Images/Man/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Images/Man/Idle/RIdle3.png').convert_alpha(), pygame.image.load('Images/Man/Idle/RIdle4.png').convert_alpha()]
animations["idleLeft"] = [pygame.image.load('Images/Man/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Images/Man/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Images/Man/Idle/LIdle3.png').convert_alpha(), pygame.image.load('Images/Man/Idle/LIdle4.png').convert_alpha()]
animations["jumpRight"] = [pygame.image.load('Images/Man/Jumping/RUp.png').convert_alpha(), pygame.image.load('Images/Man/Jumping/RDown.png').convert_alpha()]
animations["jumpLeft"] = [pygame.image.load('Images/Man/Jumping/LUp.png').convert_alpha(), pygame.image.load('Images/Man/Jumping/LDown.png').convert_alpha()]

# Load baddy animations
animations["baddyWalkRight"] = [pygame.image.load('Images/Baddy/Walking/RWalk1.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/RWalk2.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/RWalk3.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/RWalk4.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/RWalk5.png').convert_alpha()]
animations["baddyWalkLeft"] = [pygame.image.load('Images/Baddy/Walking/LWalk1.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/LWalk2.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/LWalk3.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/LWalk4.png').convert_alpha(), pygame.image.load('Images/Baddy/Walking/LWalk5.png').convert_alpha()]
animations["baddyIdleRight"] = [pygame.image.load('Images/Baddy/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/RIdle3.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/RIdle4.png').convert_alpha()]
animations["baddyIdleLeft"] = [pygame.image.load('Images/Baddy/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/LIdle3.png').convert_alpha(), pygame.image.load('Images/Baddy/Idle/LIdle4.png').convert_alpha()]

# Load boss animations
animations["globIdleRight"] = [pygame.image.load('Images/GlobMonster/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/RIdle3.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/RIdle4.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/RIdle5.png').convert_alpha()]
animations["globIdleLeft"] = [pygame.image.load('Images/GlobMonster/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/LIdle3.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/LIdle4.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Idle/LIdle5.png').convert_alpha()]
animations["globDeath"] = [pygame.image.load('Images/GlobMonster/Death/Death1.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Death/Death2.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Death/Death3.png').convert_alpha()]
animations["globAttackIdle"] = [pygame.image.load('Images/GlobMonster/Attack/Idle1.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Idle2.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Idle3.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Idle4.png').convert_alpha()]
animations["globAttackActive"] = [pygame.image.load('Images/GlobMonster/Attack/Active1.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Active2.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Active3.png').convert_alpha(), pygame.image.load('Images/GlobMonster/Attack/Active4.png'), pygame.image.load('Images/GlobMonster/Attack/Active5.png'), pygame.image.load('Images/GlobMonster/Attack/Active6.png').convert_alpha()]

# Load bot animations (not used)
# animations["botIdleRight"] = [pygame.image.load('Images/Bot/Idle/RIdle1.png').convert_alpha(), pygame.image.load('Images/Bot/Idle/RIdle2.png').convert_alpha(), pygame.image.load('Images/Bot/Idle/RIdle3.png').convert_alpha()]
# animations["botIdleLeft"] = [pygame.image.load('Images/Bot/Idle/LIdle1.png').convert_alpha(), pygame.image.load('Images/Bot/Idle/LIdle2.png').convert_alpha(), pygame.image.load('Images/Bot/Idle/LIdle3.png').convert_alpha()]
# animations["botTalkRight"] = [pygame.image.load('Images/Bot/Talking/RTalk1.png').convert_alpha(), pygame.image.load('Images/Bot/Talking/RTalk2.png').convert_alpha(), pygame.image.load('Images/Bot/Talking/RTalk3.png').convert_alpha()]
# animations["botTalkLeft"] = [pygame.image.load('Images/Bot/Talking/LTalk1.png').convert_alpha(), pygame.image.load('Images/Bot/Talking/LTalk2.png').convert_alpha(), pygame.image.load('Images/Bot/Talking/LTalk3.png').convert_alpha()]

man = player(41, -90, 96, 96, 31, 36, 32, 60)
badGuys = [baddy(8, 8, 2, 1),
           baddy(2, 5, 9, 2), baddy(3, 8, 9, 2), baddy(3, 2, 9, 2), 
           baddy(4, 6, 1, 3), baddy(8, 4, 1, 3), baddy(12, 6, 1, 3),
           baddy(12, 5, 2, 4), baddy(6, 6, 2, 4)]
glob = glob(screenWidth)
bullets = []