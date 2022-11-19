from email.mime import image
import pygame,sys
from pygame.locals import *
import random


pygame.init()

def finish(a):
    image10=pygame.image.load('gameover.png')
    image10=pygame.transform.scale(image10,(width,height))
    font = pygame.font.SysFont(pygame.font.get_default_font(),40)
    text = font.render(a+' win', True, (255,255,255))
    
    global x,x2
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(image10,(0,0))
            screen.blit(text, ((width - text.get_width())/2,270))
            pygame.display.update()
            if event.type== KEYDOWN and event.key== K_r:
                x2=200
                x=200
                return

x=200
x2=200

hp_har1=pygame.Rect(10,10,x,20)
hp_bar2=pygame.Rect(490,10,x2,20)
weapon_cooltime=0
weapon_cooltime2=0
weapon_fired=False
weapon_fired2=False
sword=5
Nuke=100
weapon=[sword,Nuke]
choice= random.randint(0,4)
width=700
height=500
j1=False
max=6
j1_cnt=max
j2=False
j2_cnt=max
isjump=False
isjump_2=False
rect2_weapon=[]
CLOCK= pygame.time.Clock()
rect1= pygame.Rect(19,300,20,20)
rect2= pygame.Rect(631,300,20,20)
rect2_weapon.append(weapon[0])
weapons=rect2_weapon[0]
swords=pygame.Rect(rect2.x,rect2.y,50,100)
sword_img=pygame.image.load('sword.png')
sword_img=pygame.transform.scale(sword_img,(50,100))
sword2=pygame.Rect(rect1.x,rect1.y,50,100)
sword_img_2=pygame.image.load('sword_red.png')
sword_img_2=pygame.transform.scale(sword_img_2,(50,100))
nuke=pygame.Rect(400,425,50,50)
nuke_img=pygame.image.load('Nuke.png')
nuke_img=pygame.transform.scale(nuke_img,(50,50))
r3= pygame.Rect(80,300,100,10)
r4=pygame.Rect(520,300,100,10)
wall=pygame.Rect(300,200,100,40)
img=pygame.image.load('다운로드 (1).png')
img= pygame.transform.scale(img,(100,40))


floor= pygame.Rect(0,445,700,55)

rects=[r3,floor]

bgImage = pygame.image.load('예비.png')
bgImage = pygame.transform.scale(bgImage, (width, height))
screen = pygame.display.set_mode((width,height))

on_air_2=True
on_air= True

while True:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    for i in [floor,r3]:
        if rect2.colliderect(floor):
            on_air=False
        elif rect2.colliderect(r3) and rect2.bottom>=200:
            on_air=False
        elif rect2.colliderect(r4) and rect2.bottom>=200:
            on_air=False
        elif rect2.colliderect(wall) and rect2.bottom>=100:
            on_air=False
        else:
            on_air=True

        if rect1.colliderect(floor):
            on_air_2=False
        elif rect1.colliderect(r3) and rect1.bottom>=200:
            on_air_2=False
        elif rect1.colliderect(r4) and rect1.bottom>=200:
            on_air_2=False
        elif rect1.colliderect(wall) and rect1.bottom>=100:
            on_air_2=False
        else:
            on_air_2=True
    
        if rect1.colliderect(swords) and weapon_fired==True:
            x-=1
            hp_har1=pygame.Rect(10,10,x,20)
    
        if rect2.colliderect(sword2) and weapon_fired2==True:
            x2-=1
            hp_bar2=pygame.Rect(490,10,x2,20)
    
    keyInput = pygame.key.get_pressed()
    
    for i in [r3]:
        if rect2.colliderect(r3) and rect2.bottom < 300:
            on_air=False

    for i in [r3]:
        if rect1.colliderect(r3) and rect1.bottom < 300:
            on_air_2=False

    if on_air_2:
        rect1.y+=11

    if rect1.colliderect(nuke):
        x-=10
        hp_har1=pygame.Rect(10,10,x,20)
    if rect2.colliderect(nuke):
        x2-=10
        hp_bar2=pygame.Rect(490,10,x2,20)

    if on_air:
        rect2.y +=11
    if  keyInput[K_SPACE] and KEYDOWN and weapon_cooltime<=0:
        weapon_fired=True
        weapon_cooltime=weapons

    if  keyInput[K_q] and KEYDOWN and weapon_cooltime2<=0:
        weapon_fired2=True
        weapon_cooltime2=weapons

    if keyInput[K_LEFT] and rect2.left >= 0:
        rect2.left -= 20
    elif keyInput[K_RIGHT] and rect2.right <= width:
        rect2.right += 20

    if weapon_fired==False:
        swords=pygame.Rect(rect2.x-30,rect2.y-50,50,100)

    else:
        swords.x-=10
    if swords.x<=0:
        weapon_fired=False

    if weapon_fired2==False:
        sword2=pygame.Rect(rect1.x+9,rect1.y-50,50,100)
        
    else:
        sword2.x+=10

    if swords.x<=0:
        weapon_fired=False

    if sword2.x>=700:
        weapon_fired2=False

    if keyInput[K_UP] and on_air == False:
        isjump = True

    if isjump:
        if j1_cnt > 0:
            rect2.top -= j1_cnt *10
            j1_cnt-=1
        else:
            isjump = False
            j1_cnt= max

    if keyInput[K_a] and rect1.left >= 0:
        rect1.left -= 20
    elif keyInput[K_d] and rect1.right <= width:
        rect1.right += 20

    
    if keyInput[K_w] and on_air_2 == False:
        isjump_2 = True

    if isjump_2:
        if j2_cnt > 0:
            rect1.top -= j2_cnt *10
            j2_cnt-=1
        else:
            isjump_2 = False
            j2_cnt= max

    if x2<=0:
        finish("red")
    if x<=0:
        finish("blue")
    weapon_cooltime-=1
    weapon_cooltime2-=1
    screen.blit(bgImage,(0,0))
    pygame.draw.rect(screen,(0,255,0),floor)
    pygame.draw.rect(screen,(255,0,0),rect1)
    pygame.draw.rect(screen,(0,0,255),rect2)
    pygame.draw.rect(screen, (255,0,0),hp_har1)
    pygame.draw.rect(screen, (255,0,0),hp_bar2)
    screen.blit(img,r3)
    screen.blit(img,r4)
    screen.blit(img,wall)
    screen.blit(sword_img,swords)
    screen.blit(sword_img_2,sword2)
    screen.blit(nuke_img,nuke)
    pygame.display.update()
