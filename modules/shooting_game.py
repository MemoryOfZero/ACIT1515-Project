import pygame
import sys
from time import sleep
import random

rock_image = ['assets/rock01.png','assets/rock02.png','assets/rock03.png','assets/rock04.png']
pad_width = 480
pad_height = 640
gamePad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption('shooting_game')
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

def writescore(count):
    global gamePad
    font = pygame.font.Font(None, 25)
    text1 = font.render("Destroyed: " + str(count), True, red)
    gamePad.blit(text1, (60, 0))

def writepassed(count):
    global gamePad
    font = pygame.font.Font(None, 25)
    text = font.render("Passed: " + str(count), True, red)
    gamePad.blit(text, (320, 0))

def writemessage(text):
    textfont = pygame.font.Font(None,25)
    text = textfont.render(text,True, red)
    textpos = text.get_rect()
    textpos.center = (pad_width/2, pad_height/2)
    gamePad.blit(text,textpos)
    pygame.display.update()

def gameover():
    global gamePad
    writemessage('Game over')
    sleep(15)
    runGame()

def draw_object(obj, x,y ):                                 # drawing objects
    global gamePad
    gamePad.blit(obj, (x,y))

def initGame():
    global gamePad, clock , background , fighter , missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((pad_width, pad_height))

    background = pygame.image.load('assets/background.png')
    fighter = pygame.image.load('assets/fighter.png')
    missile = pygame.image.load('assets/missile.png')
    explosion = pygame.image.load('assets/explosion.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock , background , fighter , missile, explosion

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = pad_width * 0.45
    y = pad_height * 0.9
    fighterX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rock_image))
    rocksize = rock.get_rect().size
    rockwidth = rocksize[0]
    rock_height = rocksize[1]

    rock_x = random.randrange(0, pad_width - rockwidth)
    rock_y = 0
    rockspeed = 2

    isshot = False   # if missile hits rock, True
    shotcount = 0
    rockpassed = 0

    ongame = False
    while not ongame:

        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:            # Move plane to left
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:          # Move plane to right
                    fighterX += 5

                elif event.key == pygame.K_SPACE:                   #shooting missile
                    missile_x = x + fighterWidth/2
                    missile_y = y - fighterHeight
                    missileXY.append([missile_x, missile_y])

            if event.type in [pygame.KEYUP]:                  # do not move
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        draw_object(background, 0, 0)

        x += fighterX
        if x <0:
            x = 0
        elif x > pad_width - fighterWidth:
            x = pad_width - fighterWidth

        draw_object(fighter, x ,y)

        if len(missileXY) != 0:
            for i,bxy in enumerate(missileXY):                 #repetition of missiles
                bxy[1] -= 10                                   # y - 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rock_y:                                         #hit the rock
                    if bxy[0] > rock_x and bxy[0] < rock_x + rockwidth:
                        missileXY.remove(bxy)
                        isshot = True
                        shotcount += 1

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                draw_object(missile, bx, by)

        writescore(shotcount)
        rock_y += rockspeed

        if rock_y > pad_height:                                        # if it hit earth
            rock = pygame.image.load(random.choice(rock_image))
            rocksize = rock.get_rect().size
            rockwidth = rocksize[0]
            rock_height = rocksize[1]
            rock_x = random.randrange(0, pad_width - rockwidth)
            rock_y = 0
            rockpassed += 1

        writepassed(rockpassed)

        if rockpassed == 3:
            gameover()

        if isshot:
            draw_object(explosion, rock_x, rock_y)

            rock = pygame.image.load(random.choice(rock_image))
            rocksize = rock.get_rect().size
            rockwidth = rocksize[0]
            rock_height = rocksize[1]
            rock_x = random.randrange(0, pad_width - rockwidth)
            rock_y = 0
            isshot = False

            rockspeed += 0.2

            if rockspeed >= 10:
                rockspeed = 10

        draw_object(rock,rock_x, rock_y)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

def start():
    initGame()
    runGame()

if __name__ == '__main__':
    start()

