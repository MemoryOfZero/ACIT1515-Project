import pygame
import sys
from time import sleep


pad_width = 480
pad_height = 640
gamePad = pygame.display.set_mode((pad_width, pad_height))
background = pygame.image.load('star_field.png')
fighter = pygame.image.load('iron.png')
missile = pygame.image.load('missile.png')
def draw_Object(obj, x,y ):
    global gamePad
    gamePad.blit(obj, (x,y))


def initGame():
    global gamePad, clock , background , fighter , missile
    pygame.init()
    gamePad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('pyShooting')


    clock = pygame.time.Clock()



def runGame():
    global gamePad, clock , background , fighter

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padwidth * 0.45
    y = pad_height * 0.9
    fighterX = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
        draw_Object(background, 0, 0)



        pygame.display.update()

        clock.tick(60)

    pygame.quit()


initGame()
runGame()