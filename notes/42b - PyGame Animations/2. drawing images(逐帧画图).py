import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Move the Dino移动恐龙
        wizardPos[0] += 0.5   #update the x for the lizard更新蜥蜴的X
        lizardPos[0] += 0.5   #update the x for the wizard更新魔法师的X值
#         
        #Draw the whole sheet绘制整张纸
        #mainSurface.blit(spriteSheet, lizardPos)
        
        #Kinda fun to have EVERY Image, but let's just get the patches we need拥有每张图片都挺有趣的，但我们还是要得到我们需要的补丁。
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint使用msPaint找到的位置
        mainSurface.blit(spriteSheet, lizardPos, [127,330,16,28])  #Positions found using msPaint((左右，上下,长，宽))
        
        
        # Now the surface is ready, tell pygame to display it!现在，表面已经准备好了，告诉pygame来显示它。
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
