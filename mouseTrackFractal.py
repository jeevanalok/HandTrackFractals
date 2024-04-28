import pygame # type: ignore
from math import sin,cos,radians 

# Initialize pygame
pygame.init()

#Constants
HEIGHT,WITDH = 800,800
BLACK =(0,0,0)
WHITE =(255,255,255)


# Set the height and width of the screen
size = [HEIGHT,WITDH]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Fractal Trees")

theta=0
INIT_POS = (WITDH//2,HEIGHT)

# Loop until the user clicks the close button.
run = True
clock = pygame.time.Clock()

def generateFractalTree(pos,length,angle,turn_angle,depth,color):
    
    if depth ==0:
        return
    
    x, y = pos


    # new points for the rotated branch
    new_x = x + cos(radians(angle)) * length
    new_y = y - sin(radians(angle)) * length

    pygame.draw.line(screen,color,pos,(int(new_x),int(new_y)))

    new_pos =  (new_x,new_y)
    length  = 0.66 * length # 2/3 of prev branch

    generateFractalTree(new_pos, length,(angle+turn_angle), turn_angle, depth-1,color)
    generateFractalTree(new_pos, length,(angle-turn_angle), turn_angle, depth-1,color)


while run:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False  

    # Clear the screen and set the screen background
    screen.fill("black")

    
    # theta +=0.01
    mouse_X,mouse_Y = pygame.mouse.get_pos()

    theta =  (mouse_X/WITDH) * 90
    generateFractalTree(INIT_POS,200,90,theta,9,WHITE) 

   

    # update the screen
    pygame.display.flip()


pygame.quit()