#pygame
import pygame
import sys
import math

## IGNORE STUFF BETWEEN HERE...

# Get things up and running

pygame.init()

# Create a window where stuff can happen

my_screen = pygame.display.set_mode( ( 800 , 600 ) , 5 )

# Load a font so that we can write something

my_font = pygame.font.SysFont( 'monospace' , 36 )

# This creates a loop that only ends when you close the window

still_looping = True
pi = math.pi
def rad(degree):
    return degree*pi/180
thickness = 45
while still_looping:
# This looks to see whether the close button has been pressed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_looping = False            


## ...AND HERE. IT IS JUST WHAT IS NEEDED TO MAKE THINGS WORK.

            


# This is the only piece of code that actually does anything interesting!

## vvv YOUR CODE IS HERE vvv

    pygame.display.update()
    my_screen.fill((255,255,255))

    #google logo that looks spray painted
    pygame.draw.arc( my_screen, (234,66,53), (400,300,200,200), rad(40), rad(150), thickness)
    pygame.draw.arc( my_screen, (250,188,5), (400,300,200,200), rad(149), rad(210), thickness)
    pygame.draw.arc( my_screen, (52,168,83), (400,300,200,200), rad(209), rad(300), thickness)
    pygame.draw.arc( my_screen, (66,134,245), (400,300,200,200), rad(299), rad(360), thickness)
    pygame.draw.rect( my_screen, (66,134,245), (500,399,55,25))
    
    #japan logo
    pygame.draw.rect( my_screen, (0,0,0), (0,0,162,100), 2)
    pygame.draw.circle( my_screen, (255,0,0), (81,50), 35)



## ^^^ YOUR CODE IS HERE ^^^

    


## IGNORE FROM HERE ONWARD

# Finish things off
pygame.quit()
sys.exit()