import pygame
import random
import os
import cheat
#! загрузка изображений
folder = os.path.dirname(__file__)
sprite_folder = os.path.join(folder,'sprite')
location_folder = os.path.join(folder,'location')
player_img = pygame.image.load(os.path.join(sprite_folder, 'утюг2.png'))
player_img1 = pygame.image.load(os.path.join(sprite_folder, 'утюг1.2.png'))
player_img2 = pygame.image.load(os.path.join(sprite_folder, 'утюг1.png'))
player_img3 = pygame.image.load(os.path.join(sprite_folder, 'утюг3.png'))
mob = pygame.image.load(os.path.join(sprite_folder, 'злой_утюг.png'))
ico = pygame.image.load(os.path.join(sprite_folder, 'envell.png'))
playerList = [player_img,player_img1] 
location = pygame.image.load(os.path.join(location_folder,'location1.jpg'))
indicator = pygame.image.load(os.path.join(sprite_folder, 'screen.png'))
#! переменные
width = 760
height = 480
fps = 30
black = (0,0,0)
red = (255,0,0)
xp = 30
color = [black,red]
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
game = True
file = os.path.abspath(__file__)
pygame.display.set_caption("heroes of envell")
pygame.display.set_icon(ico)
#! функции и классы
def flip() :
 pygame.display.flip()
def lvl() :
    return("start " + file[:-19] + "game(menu).py")
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerList[0]
        self.rect = self.image.get_rect()
        self.rect.center = (90, 350)
    def update(self):
        random.shuffle(playerList)
        self.image = playerList[0]
        if self.rect.bottom > height :
            self.rect.bottom = height
        if self.rect.y < 0 :
            self.rect.top = 0
        if self.rect.right > width :
            self.rect.right = width
        if self.rect.x < 0 :
            self.rect.left = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
            #self.image = 
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
            self.image = player_img2
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
            self.image = player_img3
    def x(self) :
        return(self.rect.x)
    def y(self) :
        return(self.rect.y)
class Indicator(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = indicator
        self.rect = self.image.get_rect()
        self.rect.center = (170,440)
    def update(self):
        pygame.draw.rect(screen, color[1], (35, 455, xp, 10), 0)
        pygame.draw.rect(screen, color[1], (100, 455, xp, 10), 0)
        pygame.draw.rect(screen, color[1], (160, 455,xp, 10), 0)
        pygame.draw.rect(screen, color[1], (225, 455, xp, 10), 0)
        pygame.draw.rect(screen, color[1], (295, 455, xp, 10), 0)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob
        self.rect = self.image.get_rect()
        self.rect.center = (730,240)
    def update(self):
        global xp
        self.rect.x -= 5
        if self.rect.x < 0 :
            self.rect.x = 730
            self.rect.y = random.randint(0,height - 40)
        if self.rect.x <= player.x() <= self.rect.x + mob.get_width() and self.rect.y <= player.y() <= self.rect.y + mob.get_height() :
            self.rect.x = 730
            self.rect.y = random.randint(0,height - 40)
            xp += -3 
        if xp <= 0 :
             os.system(lvl())
             exit()           
all_sprites = pygame.sprite.Group()
player = player()
indicator = Indicator()
obstacle = Obstacle()
all_sprites.add(player,indicator,obstacle)
#! цикл
while game == True :
    clock.tick(fps)
    screen.blit(location,(0,0))
    all_sprites.update()
    all_sprites.draw(screen)
    flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            game = False;
pygame.quit()