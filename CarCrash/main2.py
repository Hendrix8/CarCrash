import pygame
import button
import random

pygame.init()

clock = pygame.time.Clock()

winWidth = 800
winHeight = 600
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Car Crash")
bgImg = pygame.image.load("CarCrash/resources/background.png")
bg = pygame.transform.scale(bgImg, (800,600))
i = 0 # background coordinate Y (which is going to change with a loop)

# Button images
startImg = pygame.image.load("CarCrash/resources/Start.png").convert_alpha()
changeColorImg = pygame.image.load("CarCrash/resources/ChangeColor.png").convert_alpha()
exitImg = pygame.image.load("CarCrash/resources/Exit.png").convert_alpha()

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
enemyY_change = 10 #difficulty 
numOfEnemies = 1

for i in range(numOfEnemies):
        enemyImgRes = [pygame.transform.scale(i,(carWidth,carHeight)) for i in enemyImg]
        enemyX.append(random.choice(enemyX_spawns))


# Drawing Enemy         
def enemyDraw(image, x, y):
        win.blit(image,(x,y))



# Creating Buttons
startBtn = button.Button(50, 100, startImg, 0.3)
exitBtn = button.Button(50, 200, exitImg, 0.3)
colorBtn = button.Button(50,300,changeColorImg, 0.3)
car = 0     

# Choosing a random enemy to spawn first 
enemy = random.choice(enemyImgRes) # random enemy car
enemy_x = random.choice(enemyX_spawns) # random spawn x coordinate
enemy_y = enemyY # fixed y spawn 

running = True 
while running:

        selectedCar = carsResized[car]
        
        for event in pygame.event.get():
                # quiting window if red cross is pressed
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                x -= 125
                        if event.key == pygame.K_RIGHT:
                                x += 125


        win.fill((0,0,0)) # filling window with black color behind the bg
        win.blit(bg, (0, i)) # setting the background with a moving height parameter
        win.blit(bg, (0, -winHeight +i)) # readding the picture a second time

        
        # changing the color of the car when the button is pressed
        if colorBtn.draw(win):
                car = (car + 1)%carsNumber

        if i == winHeight:
                win.blit(bg, (0, -winHeight + i)) # readding the picture in a loop so that the bg doesn't black out
                i = 0

        i += 5


        if startBtn.draw(win):
                print("Start")
                
        
        enemyDraw(enemy, enemy_x,enemy_y)
        enemy_y += enemyY_change #difficulty 

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

        if exitBtn.draw(win):
                running = False
        pygame.display.update()


clock.tick(60)
pygame.quit()
quit()
