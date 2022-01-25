from cProfile import label
import pygame
import button
import random
import math
from pygame import mixer
import time

pygame.init()
mixer.init()
clock = pygame.time.Clock()

winWidth = 800
winHeight = 600
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Car Crash")
bgImg = pygame.image.load("CarCrash/resources/background.png")
bg = pygame.transform.scale(bgImg, (800,600))
i = 0 # background coordinate Y (which is going to change with a loop)

# Setting the app icon
iconImg = pygame.image.load("CarCrash/resources/icon.png")
pygame.display.set_icon(iconImg)

# Button images
startImg = pygame.image.load("CarCrash/resources/Start.png").convert_alpha()
changeColorImg = pygame.image.load("CarCrash/resources/ChangeColor.png").convert_alpha()
exitImg = pygame.image.load("CarCrash/resources/Exit.png").convert_alpha()
restartImg = pygame.image.load("CarCrash/resources/restart.png")

# Car images
blue = pygame.image.load("CarCrash/resources/myCarBlue.png")
black = pygame.image.load("CarCrash/resources/myCarBlack.png")
coffee = pygame.image.load("CarCrash/resources/myCarCoffee.png")
darkBrown = pygame.image.load("CarCrash/resources/myCarDarkBrown.png")
darkGrey = pygame.image.load("CarCrash/resources/myCarDarkGrey.png")
darkPink = pygame.image.load("CarCrash/resources/myCarDarkPink.png")
lightBlue = pygame.image.load("CarCrash/resources/myCarLightBlue.png")
lightGrey = pygame.image.load("CarCrash/resources/myCarLightGrey.png")
openBlue = pygame.image.load("CarCrash/resources/myCarOpenBlue.png")
purple = pygame.image.load("CarCrash/resources/myCarPurple.png")
red = pygame.image.load("CarCrash/resources/myCarRed.png")

# enemy car images
car1 = pygame.image.load("CarCrash/resources/car2.png")
car2 = pygame.image.load("CarCrash/resources/car3.png")
amb = pygame.image.load("CarCrash/resources/ambulance.png")
taxi = pygame.image.load("CarCrash/resources/taxi.png")

Cars = [blue, black, coffee, darkBrown, darkGrey, darkPink, lightBlue, lightGrey, openBlue, purple, red]
carsNumber = len(Cars)

# Changing the sizes of the images of the cars 
carWidth = 220
carHeight = 220
carsResized = [pygame.transform.scale(i, (carWidth,carHeight)) for i in Cars]

# Car coordinates
x = 230
y = 380

# Enemy
enemyX_spawns = [105, 230, 355, 480]
enemyImg = [car1,car2,amb,taxi]
enemyX = []
enemyY = -220
enemyY_change = 0 #difficulty (it is zero before the start button is pressed)
#numOfEnemies = 1
enemyImgRes = [pygame.transform.scale(i,(carWidth,carHeight)) for i in enemyImg]

enemyX.append(random.choice(enemyX_spawns))


# Drawing Enemy         
def enemyDraw(image, x, y):
        win.blit(image,(x,y))

# game over text 
overFont = pygame.font.Font("freesansbold.ttf", 64)
def gameOverText():
        overText = overFont.render("GAME OVER", True, (0,0,0))
        win.blit(overText, (200,250))


        
       





# Level text 
level = pygame.font.Font("freesansbold.ttf", 25)
def levelDisplay(labelsGone):
        levelText = level.render("Level: "+str(levelNumber), True, (0,0,0))
        
        if labelsGone: 
                win.blit(levelText, (-100,-100))
        else:
                win.blit(levelText, (4,10))

# score text 
score = pygame.font.Font("freesansbold.ttf", 25)
def scoreDisplay(labelsGone):
        scoreText = score.render("Score: "+str(scoreNumber), True, (0,0,0))
        
        if labelsGone:
                win.blit(scoreText, (-100,-100))
        else:
                win.blit(scoreText, (4,70))

# Collision 
def isCollision(enemyX,enemyY,carX,carY):
        distance = math.sqrt(math.pow(enemyX - carX, 2) + math.pow(enemyY - carY,2))
        if distance < 125:
                return True
        else:
                return False


# Creating Buttons
startBtn = button.Button(50, 150, startImg, 0.3)
exitBtn = button.Button(50, 250, exitImg, 0.3)
colorBtn = button.Button(50,200,changeColorImg, 0.3)
restartBtn = button.Button(-1000,-1000,restartImg, 4)

car = 0     

# Choosing a random enemy to spawn first 
enemy = random.choice(enemyImgRes) # random enemy car
enemy_x = random.choice(enemyX_spawns) # random spawn x coordinate
enemy_y = enemyY # fixed y spawn 

# Ending picture
endPicNormal = pygame.image.load("CarCrash/resources/flashyCar.png")
endPic = pygame.transform.scale(endPicNormal,(winWidth,winHeight))


bgMove = 0 # how fast the background is running

over = False
gameWin = False
showEndPic = False
labelsGone = False
bringRestart = False
scoreNumber = 0
levelNumber = 1
                                
whoosh = mixer.Sound("CarCrash/resources/whoosh.wav")
victory = mixer.Sound("CarCrash/resources/victory.wav")


running = True 
while running:
        
        selectedCar = carsResized[car]
        
        for event in pygame.event.get():
                # quiting window if red cross is pressed
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN and not over:
                        if event.key == pygame.K_LEFT:
                                whoosh.play()
                                x -= 125
                        if event.key == pygame.K_RIGHT:
                                whoosh.play()
                                x += 125
                        if event.key == pygame.K_SPACE:
                                horn = mixer.Sound("CarCrash/resources/Horn.wav")
                                horn.play()
                                

        win.fill((0,0,0)) # filling window with black color behind the bg
        win.blit(bg, (0, i)) # setting the background with a moving height parameter
        win.blit(bg, (0, -winHeight +i)) # readding the picture a second time
        
        # changing the color of the car when the button is pressed
        if colorBtn.draw(win):
                car = (car + 1)%carsNumber

        if i == winHeight:
                win.blit(bg, (0, -winHeight + i)) # readding the picture in a loop so that the bg doesn't black out
                i = 0

        i += bgMove

        # Starting the game when the button start is pressed
        if startBtn.draw(win):
                enemyY_change = 12
                bgMove = 8
                startBtn.rect.topleft = (-100,-100)
                colorBtn.rect.topleft = (-100,-100)
                exitBtn.rect.topleft = (-100,-100)
                bgMusic = mixer.music.load("CarCrash/resources/bgMusic.wav")
                mixer.music.play(-1)
                mixer.music.set_volume(0.4)
                

        
        
        
        enemyDraw(enemy, enemy_x,enemy_y)
        enemy_y += enemyY_change #difficulty 

        # restarting the enemy cars that go passed the player car
        if enemy_y > winHeight:
                enemy_y = 0 - carHeight
                enemy_x = random.choice(enemyX_spawns)
                enemy = random.choice(enemyImgRes)

                                  
        win.blit(selectedCar, (x,y))

        # Border checking
        if x <= 105:
                x = 105
        if x >= 480: 
                x = 480

        # Enemy Colission
        if isCollision(enemy_x,enemy_y,x,y):
                gameOverText()
                if not over:
                        crash = mixer.Sound("CarCrash/resources/crash.wav")
                        crash.set_volume(0.6)
                        crash.play()
                
                enemyY_change = 0
                bgMove = 0
                over = True     
                mixer.music.fadeout(2000)
                bringRestart = True
                if restartBtn.draw(win):
                        over = False
                        enemy_x = random.choice(enemyX_spawns)
                        enemy_y = 0 - carHeight
                        x = 230
                        scoreNumber = 0 
                        levelNumber = 1
                        mixer.music.play(-1)
                        enemyY_change = 12
                        bgMove = 8
                        restartBtn.rect.topleft = (-1000,-1000)

        # Bringing restart button
        if bringRestart:
                restartBtn.rect.topleft = (-100,350)
                restartBtn.draw(win) 
                bringRestart = False
        
        # level change and difficulty increase
        
        if enemy_y > y + 208:
                scoreNumber += 1
                
        if scoreNumber  == 15: # scoreNumber counts how many cars have been passed without crashing
                levelNumber = 2 #2
                enemyY_change = 13  
                bgMove = 8
        if scoreNumber == 30:
                levelNumber = 3
                enemyY_change = 14 
        if scoreNumber == 45: 
                levelNumber = 4
                enemyY_change = 15 
        if scoreNumber == 60: 
                levelNumber = 5
                enemyY_change = 16 
        if scoreNumber == 75: 
                levelNumber = 6
                enemyY_change = 17 
        if scoreNumber == 90: 
                levelNumber = 7
                enemyY_change = 18 
        if scoreNumber == 105:
                levelNumber = 8
                enemyY_change = 19 
        if scoreNumber == 120:
                levelNumber = 9
                enemyY_change = 20 
        if scoreNumber ==  135:
                gameWin = True
                
                
        if gameWin:
                victory.set_volume(0.5)
                victory.play(0)
                mixer.music.fadeout(1000)
                levelNumber = 10
                bgMove = 0
                enemy_y = -1000
                enemyY_change = 0
                gameWin = False
                showEndPic = True
                labelsGone = True
                scoreNumber += 1
        
        if showEndPic:
                win.blit(endPic,(0,0))

        
        '''# CPU PLAY ---- uncomment this code to let the computer play perfectly -----
        if enemy_x == 105 and x == 105:
                x = 230
        elif enemy_x == 230 and x == 230:
                x = random.choice([355,105])
        elif enemy_x == 355 and x == 355:
                x = random.choice([480,230])
        elif enemy_x == 480 and x == 480:
                x = 355
'''

        levelDisplay(labelsGone)
        scoreDisplay(labelsGone)

        if exitBtn.draw(win):
                running = False


        pygame.display.update()


clock.tick(60)
pygame.quit()
quit()
