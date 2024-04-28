import pygame # type: ignore
from math import sin,cos,radians 

import cv2 as cv #type:ignore
import mediapipe.python.solutions.hands as mp_hands # type: ignore
import mediapipe.python.solutions.drawing_utils as drawing # type: ignore
import mediapipe.python.solutions.drawing_styles as drawing_styles # type: ignore

# Initialize pygame
pygame.init()

#Constants
HEIGHT,WITDH = 800,800
BLACK =(0,0,0)
WHITE =(255,255,255)

VIDEO_WIDTH = 400
VIDEO_HEIGHT = 400




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



hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands = 1,
    min_detection_confidence =0.5,

)
cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, VIDEO_HEIGHT)

    

while cam.isOpened() and run:
    success, frame = cam.read()
    if not success:
        print("Camera frame not available")
        continue

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    hands_detected = hands.process(frame)

    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)


    hand_X = 0

    if( hands_detected.multi_hand_landmarks):
        for hand_landmarks in hands_detected.multi_hand_landmarks:

            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style()

            )



            normalizedLandmark = hand_landmarks.landmark[0].x
    
            hand_X =  normalizedLandmark * VIDEO_WIDTH

    cv.imshow("Show video",frame)
    

    if (cv.waitKey(20) & 0xff == ord('q') or  not run):
        break
    
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

    theta =  ((hand_X* 2)/WITDH) * 90
    generateFractalTree(INIT_POS,200,90,theta,9,WHITE) 



    # update the screen
    pygame.display.flip()


pygame.quit()

cv.destroyAllWindows()
cam.release()