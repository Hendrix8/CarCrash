import pygame
import button

pygame.init()

clock = pygame.time.Clock()

winWidth = 800
winHeight = 600
win = pygame.display.set_mode((800,600))
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

Cars = [blue, black, coffee, darkBrown, darkGrey, darkPink, lightBlue, lightGrey, openBlue, purple, red]
carsNumber = len(Cars)

# Changing the sizes of the images of the cars 
carsResized = [pygame.transform.scale(i, (220,220)) for i in Cars]

#Car coordinates
x = 230
y = 380



# Creating Buttons
startBtn = button.Button(50, 100, startImg, 0.3)
exitBtn = button.Button(50, 200, exitImg, 0.3)
colorBtn = button.Button(50,300,changeColorImg, 0.3)
car = 0     
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
                win.blit(bg, (0, i))       
                                  
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
