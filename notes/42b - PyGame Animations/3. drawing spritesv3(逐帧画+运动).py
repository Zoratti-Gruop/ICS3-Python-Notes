import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 10                #Slowing down the program
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    #These are needed for the image animation这些是图像动画所需要的
    lizardRect = [128,236,16,28]
    lizardPatchNumber = 0        #Start at the initial patch从最初的补丁开始
    lizardNumPatches = 4         #Only use 4 patches只使用4个补丁

    
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...在这里更新你的游戏对象和数据结构...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Move the Dino
        wizardPos[0] += 0.5   #update the x for the lizard
        lizardPos[0] += 0.5   #update the x for the wizard
#         
        if (lizardPatchNumber < lizardNumPatches-1) :
            lizardPatchNumber += 1
            lizardRect[0] += lizardRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image将 "显示窗口 "沿着精灵片向右移动，宽度为图像的宽度。
        else:
            lizardPatchNumber = 0           #Reset back to first patch重置到第一个补丁
            lizardRect[0] -= lizardRect[2]*(lizardNumPatches-1)  #Reset the rect position of the rect back too将矩形的位置也重新设置为矩形的位置
        
        print(f"Patch Number: {lizardPatchNumber}   Image Rect: {lizardRect}  ")
        
        #Draw the image of the sprite using the rect使用矩形绘制精灵的图像
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint使用msPaint找到的位置
        mainSurface.blit(spriteSheet, lizardPos, lizardRect)  #Positions found using msPaint
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
