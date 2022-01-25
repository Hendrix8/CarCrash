import pygame

# a class that represents the buttons
class Button():
        # Constructor: initializing the class fields
        def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False
        
        # function for drawing the buttons
        def draw(self,window):
                action = False

                pos = pygame.mouse.get_pos() # getting the position of the mouse 

                # checking for clicking 
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                self.clicked = True
                                action = True
                
                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False


                # drawing button
                window.blit(self.image, (self.rect.x, self.rect.y))
                
                return action