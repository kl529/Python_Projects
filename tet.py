import sys , os , math , random
import pygame
from pygame. locals import *

def main():
	intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        pygame.draw.rect(gameDisplay, red,(550,450,100,50))


        pygame.display.update()
        clock.tick(15)

def terminate():

    pygame.quit()
    sys.exit()	
	
if __name__ == '__min__':
	main()
