import pygame
import os
import random
import math
from pygame.math import Vector2


pygame.init()
#H+W Screen
Width = 1920
Height = 1080

#Color
Pink = (255,153,204)
RED = (255,0,0)
White = (255,255,255)
Black = (0,0,0)
Darkslateblue = (72,61,139)
Indigo = (75,0,130)
Rebeccapurple = (102,51,153)
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Test')
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,'ให้หนุน')
direction = 0
FPS = 30
clock = pygame.time.Clock()
background_pic = os.path.join(img_folder,'MC','2x','x2.jpeg')
background = pygame.image.load(background_pic)

######################################Seeker_class
 
class Seeker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Seeker_idle = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.image = pygame.image.load(Seeker_idle).convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        ##################################Seeker_position
        self.rect.centerx = Width / 2
        self.rect.bottom = Height / 2

    def update(self):
        Seeker_left = os.path.join(img_folder,'MC','x3','ไฟล์_001.png')
        Seeker_right = os.path.join(img_folder,'MC','x3','ไฟล์_000.png')
        Seeker_up = os.path.join(img_folder,'MC','x3','ไฟล์_003.png')
        Seeker_down = os.path.join(img_folder,'MC','x3','ไฟล์_002.png')
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.image = pygame.image.load(Seeker_left).convert()
            self.image.set_colorkey(Black)
            self.speedx = -5
        
        if keystate[pygame.K_d]:
            self.image = pygame.image.load(Seeker_right).convert()
            self.image.set_colorkey(Black)
            self.speedx = 5
            
        if keystate[pygame.K_s]:
            self.image = pygame.image.load(Seeker_down).convert()
            self.image.set_colorkey(Black)
            self.speedy = 5
            
        if keystate[pygame.K_w]:
            self.image = pygame.image.load(Seeker_up).convert()
            self.image.set_colorkey(Black)
            self.speedy = -5
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > Width + 10:
            self.rect.right = Width + 10
        
        if self.rect.left < -10:
            self.rect.left = -10
        
        if self.rect.top < 4:
            self.rect.top = 4
        
        if self.rect.bottom > Height:
            self.rect.bottom = Height

        
    
    def attack(self):
        all_sprites.add(attack_effect)
        attack_effects.add(attack_effect)

class HP1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 60
        self.rect.bottom = 70

class HP2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 120
        self.rect.bottom = 70

class HP3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(Pink)
        self.rect =self.image.get_rect()
        self.rect.left = 180
        self.rect.bottom = 70

def lose_hp():
    if char_hit_count == 1:
        hp1.image.fill(Black)
    elif char_hit_count == 2:
        hp2.image.fill(Black)
    elif char_hit_count == 3:
        hp3.image.fill(Black)

#########################################Enemy_class
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Enemy_idle = os.path.join(img_folder,'x2','สไลม โจมตีระยะประชิด','SLIME_STAND.png')
        self.image = pygame.image.load(Enemy_idle).convert()
        self.image.set_colorkey(Black)
        self.rect =self.image.get_rect()
        ###############################################Enemy position
        self.rect.top = random.randrange(169,900)
        self.rect.centerx = random.randrange(267,1500) 
    
    

class Attack_effect(Seeker):

    def __init__(self , x, y,width, height,speed,targetx,targety):
        super().__init__()
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        print('Angle in degrees:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect =self.image.get_rect()
        self.speedy = -5

    def update(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        #self.rect.y += self.speedy


seeker = Seeker()
############all_sprites funtion
all_sprites = pygame.sprite.Group(seeker)
all_sprites.add(seeker)
enemy = pygame.sprite.Group()
hps = pygame.sprite.Group
attack_effects = pygame.sprite.Group()
#attack_effects = []
#leaderboard = Leaderboard()
#all_sprites.add(leaderboard)

hp1 = HP1()
all_sprites.add(hp1)
hps.add(hp1)
hp2 = HP2()
all_sprites.add(hp2)
hps.add(hp2)
hp3 = HP3()
all_sprites.add(hp3)
hps.add(hp3)

em_count = 0
wave = 1
for i in range(5):
    em = Enemy()
    all_sprites.add(em)
    enemy.add(em)
    em_count += 1

Game_running = True
char_hit_status = False
char_hit_count = 0
score_p1 = 0




while Game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                attack_effect = Attack_effect(seeker.rect.centerx,seeker.rect.centery,20,20,20,x,y)
                seeker.attack()
            elif event.key == pygame.K_t:
                print("mic on")
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x,y)
            attack_effect = Attack_effect(seeker.rect.centerx,seeker.rect.centery,20,20,20,x,y)
            #a_e = Attack_effect(seeker.rect.centerx,seeker.rect.centery,x,y)
            #a_e = Attack_effect(seeker.rect.centerx, seeker.rect.centery, 20, x,y)
            seeker.attack()            



        all_sprites.update()
        hits_em = pygame.sprite.groupcollide(enemy,attack_effects,True,True)
        if hits_em:
            if hits_em:
                em_count -= 1
                score_p1 += 50
            if em_count <= 0:
                wave += 1
                for i in range(5*wave):
                    em = Enemy()
                    all_sprites.add(em)
                    enemy.add(em)
                    em_count += 1

        print("top =" , seeker.rect.top)
        print("bottom =" , seeker.rect.bottom)
        print("left =" , seeker.rect.left)
        print("right =" , seeker.rect.right)
        print("direction =", direction)
        print("seeker.image =", seeker.image)
        print("seeker.rect =", seeker.rect)

       
                                
            
        
        #check HP if HP run out,seeker will die
        
        if pygame.sprite.spritecollide(seeker,enemy,False):
            if not char_hit_status :
                char_hit_status = True
                char_hit_count += 1
                lose_hp()
                score_p1 -= 100
        else :
            char_hit_status = False
        if char_hit_count >= 3:
            Game_running=False
           
        clock.tick(FPS)
        
        screen.blit(background,background.get_rect(center = (Width/2, Height/2)))
        #screen.blit(Score_p1,250,250)
        print(img_folder)

        all_sprites.draw(screen)
        pygame.display.flip()
        
        

        


pygame.quit()