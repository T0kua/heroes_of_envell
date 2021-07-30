import pygame
import os
from pygame.locals import *
width = 1920
height = 1016
fps = 30
black = (0,0,0)
screen = pygame.display.set_mode((width,height))
game = True
file = os.path.abspath(__file__)
folder = os.path.dirname(__file__)
img = os.path.join(folder,'db_art')
menu = pygame.image.load(os.path.join(img,'menu.jpg'))
def flip() :
 pygame.display.flip()
def lvl() :
    return("start " + file[:-14] + "/heroes_of_envell.py")
while game == True :
    pos = pygame.mouse.get_pos()
    screen.blit(menu,(0,0))
    flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            game = False;
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1800 > pos[0] > 1360 and 500 < pos[1]  < 600 :
            os.system(lvl())
            exit()
pygame.quit()