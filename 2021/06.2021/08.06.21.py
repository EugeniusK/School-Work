import pygame
import sys
import time
## IGNORE STUFF BETWEEN HERE...

# Get things up and running

pygame.init()

# Create a window where stuff can happen

my_screen = pygame.display.set_mode( ( 800 , 600 ) , 5 )

# Load a font so that we can write something

my_font = pygame.font.SysFont( 'monospace' , 36 )

# This creates a loop that only ends when you close the window

x_coordinate = 400
y_coordinate = 300
still_looping = True

while still_looping:

# This looks to see whether the close button has been pressed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            still_looping = False

## ...AND HERE. IT IS JUST WHAT IS NEEDED TO MAKE THINGS WORK.

            


# This is the only piece of code that actually does anything interesting!

## vvv YOUR CODE IS HERE vvv

    some_text = my_font.render( 'Hello World' , 1 , ( 0 , 0 , 200 ) )
    
    my_screen.blit( some_text , ( x_coordinate, y_coordinate ) )
    

    pygame.display.update()

    my_screen.fill((100,100,150))
    pygame.draw.circle(my_screen,(200,0,0),(200,200),100)
    pygame.draw.rect(my_screen,(0,0,120),(0,0,600,600),5)

    some_time = my_font.render('Time: ' + time.strftime('%x %X'), 1, (200, 200, 200))
    my_screen.blit(some_time, (50, 50))

    my_keys = pygame.key.get_pressed()
    if my_keys[pygame.K_LEFT]:
        x_coordinate -= 1
    elif my_keys[pygame.K_RIGHT]:
        x_coordinate += 1
    elif my_keys[pygame.K_UP]:
        y_coordinate -= 1
    elif my_keys[pygame.K_DOWN]:
        y_coordinate += 1
## ^^^ YOUR CODE IS HERE ^^^

    


## IGNORE FROM HERE ONWARD

# Finish things off
pygame.quit()
sys.exit()