#TODO: Update this example showing how to use a temporary surface and pygame.transform.flip(tempSurface,True,False)
import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    #----------------------Set up the game------------#  

    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    spriteSheet = pygame.transform.scale2x(spriteSheet)
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    #These are needed for the image animation
    lizardRect = [176,236,16,28]  #Old Values
    lizardRect = [352,472,32,56]  #New values are doubled since I doubled the scale
    lizardPatchNumber = 0         #Start at the initial patch从最初的补丁开始
    lizardNumPatches = 5          #Only use 4 patches只使用4个补丁
    lizardFrameCount = 0          #Start at intial frame从第一帧开始
    lizardFrameRate = 10         #How often to re-draw the lizard多久重新画一次蜥蜴
    lizardDirection = 'Right'     #Control which direction lizard is facing控制蜥蜴的方向
    lizardSpeed = 0.5
    
    lizardMove = False            #Control whether the lizard can move控制蜥蜴是否能移动
    
    while True:
        
        #----------------------Check all the events to see if anything is happening------------#  

        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:          #Add some key handling to make space change lizard's direction添加一些关键处理，使空间改变蜥蜴的方向
            if ev.key == pygame.K_a:
                lizardDirection = 'Left'
                lizardMove = True
            elif ev.key == pygame.K_d:
                lizardDirection = 'Right'
                lizardMove = True
        elif ev.type == pygame.KEYUP:
            lizardMove = False


 

        #----------------------Game Logic Goes After Here----------------------------#  
        # Update your game objects and data structures here...

        #Game logic for the lizard
        if (lizardMove):  #Check if the lizard should move检查蜥蜴是否应该移动
            #Move the Dino
            if lizardDirection =='Right': #Lizard goes right蜥蜴向右走
                lizardPos[0] += lizardSpeed     #update the x for the lizard
            else:                               #Lizard goes left
                lizardPos[0] -= lizardSpeed     #update the x for the lizard
            
            if (frameCount % lizardFrameRate == 0):    #Only change the animation frame once every {lizardFrameRate} frames#每隔{lizardFrameRate}帧只改变一次动画帧。
                if (lizardPatchNumber < lizardNumPatches-1) :
                    lizardPatchNumber += 1
                    lizardRect[0] += lizardRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image将 "显示窗口 "沿着精灵表向右移动，宽度为图像的宽度。
                else:
                    lizardPatchNumber = 0           #Reset back to first patch重置回第一个补丁
                    lizardRect[0] -= lizardRect[2]*(lizardNumPatches-1)  #Reset the rect position of the rect back too将矩形的位置也重新设置为矩形的位置
                    #self.imageRect = copy.copy(self.origImageRect)
                
                print(f"Patch Number: {lizardPatchNumber}   Image Rect: {lizardRect}  ")
          
          
          
        #Game Logic for the wizard
        wizardPos[0] += 0.5   #update the x for the wizard
        
        
        
        #----------------------Draw all the images----------------------------#  
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))
        
        #Draw the image of the wizard sprite using the rect
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint
        
        
        #Draw the image of the lizard sprite using the rect
        #mainSurface.blit(spriteSheet, lizardPos, lizardRect)  #Positions found using msPaint使用msPaint找到的位置
        tempSurface = pygame.Surface( (lizardRect[2], lizardRect[3]) ) #Make a temp Surface using the width and height of the rect用矩形的宽度和高度做一个临时的表面
        tempSurface.fill((1,255,1))
        tempSurface.set_colorkey((1,255,1))                                      #Set the color black to be transparent设置黑色为透明的颜色
        tempSurface.blit(spriteSheet, (0,0),  lizardRect)                      #Copy the lizard image to the temp surface将蜥蜴图像复制到临时表面
#         
        if lizardDirection == 'Left':  #设置反转图像的条件
            tempSurface = pygame.transform.flip(tempSurface,True,False)
        
        mainSurface.blit(tempSurface, lizardPos)  #Positions found using msPaint使用msPaint找到的位置
        
        
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        #----------------------Set your frame rate----------------------------#  

        frameCount += 1;
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
