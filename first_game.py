import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Corinna's First Game")



# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')




#creating and moving a character
x = 50
y = 400
width = 40
height = 60
vel = 5
#velocity is the speed of the character moving

clock = pygame.time.Clock()


isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
        # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    
    global walkCount

    win.blit(bg,(0,0)) #This will draw our background
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left: #If we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))# We integer divide walkCounr by 3 to ensure each
        walkCount += 1   # image is shown 3 times every animation
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))# If the character is standing still
        walkCount = 0
        
    
    pygame.display.update()

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        #This will loop through a list of any keyboard or mouse evnts
        if event.type == pygame.QUIT: #check if red button in corner is clicked
            run = False #End of game loop

    keys = pygame.key.get_pressed() #dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:# Making sure the top right corner of our character is less than the screen width - its width 
        x+= vel
        left = False
        right = True
    else: #If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
        left = False
        right = False
        walkCount = 0

        
    if not(isJump): #Checks if user is not jumping
        if keys[pygame.K_SPACE]:
            isJump = True
            right: False
            left: False
            walkCount = 0
    else:
       #This is what will happen if we are jumping
        if jumpCount >= -10:
           y -= (jumpCount * abs(jumpCount)) * 0.5
           jumpCount -= 1
        else: #This will execute if your jump is finished
            jumpCount  = 10
            isJump = False
            #Resetting our variables
    redrawGameWindow()         

            




            
pygame.quit()
        
