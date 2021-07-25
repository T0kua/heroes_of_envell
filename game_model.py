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
ico = pygame.image.load(os.path.join(sprite_folder, 'envell.png'))
playerList = [player_img,player_img1] 
location = pygame.image.load(os.path.join(location_folder,'location1.jpg'))
#! переменные
width = 760
height = 480
fps = 30
black = (0,0,0)
color = [black]
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
game = True
pygame.display.set_caption("heroes of envell")
pygame.display.set_icon(ico)
#! функции и классы
def flip() :
 pygame.display.flip()
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
all_sprites = pygame.sprite.Group()
player = player()
all_sprites.add(player)
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