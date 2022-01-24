from random import random
import pygame as py 
import random
import time
import button

py.init()

winWidth = 800
winHeight = 600

window = py.display.set_mode((winWidth, winHeight))
py.display.set_caption("CarCrash")

clock = py.time.Clock()

carWidth = 130
carImg = py.image.load("CarCrash/resources/myCarLightGrey.png")

def yellowLine(x,y,w,h,color):
    py.draw.rect(window,color,[x, y, w, h])


oppCar = py.image.load("CarCrash/resources/Car2.png")
def comp(x ,y, w, h, color):
    #py.draw.rect(window, color, [x, y, w, h])
    window.blit(oppCar, (x,y))

def car(x, y):
    window.blit(carImg, (x,y))

black = (0,0,0)
white = (255,255,255)
yellow = (228,208,10)

def labels(text, font):
    label = font.render(text, True, black)
    return label, label.get_rect()

def messageDisplay(text):
    message = py.font.Font("freesansbold.ttf", 115)
    messageSurf, messageRect = labels(text, message)
    messageRect.center = ((winWidth/2),(winHeight/2))
    window.blit(messageSurf,messageRect)

    py.display.update()

    time.sleep(2)
    gameLoop()

def crash():
    messageDisplay("CarCrash")    

def gameLoop():
    
    x = winWidth * 0.45
    y = winHeight * 0.74

    xChange = 0

    compStartX = random.randrange(0, winWidth)
    compStartY = -600
    compSpeed = 10
    compWidth = 56
    compHeight = 111

    lineX = 400
    lineY = 0
    lineSpeed = 10
    lineWidth = 30
    lineHeight = 100


    gameExit = False

    while not gameExit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    xChange = -10
                if event.key == py.K_RIGHT:
                    xChange =  10
            
            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    xChange = 0
        
        x += xChange
 
        darkGrey = (169, 169, 169)
        window.fill(darkGrey)


        yellowLine(lineX,lineY,lineWidth,lineHeight,yellow)
        lineY += lineSpeed

    


        comp(compStartX, compStartY,compWidth,compHeight, black)
        compStartY += compSpeed


        if lineY > winHeight- lineHeight:
            lineY = 0 - lineHeight
        
        
        car(x,y)


        if x > winWidth - carWidth or x < -50: 
            crash()
        
        if compStartY > winHeight:
            compStartY = 0 - compHeight
            compStartX = random.randrange(0, winWidth)
        

        if y < compStartY + compHeight :

            print("obstacle pass")


        py.display.update()
        clock.tick(60)


gameLoop()
py.quit()
quit()




            







