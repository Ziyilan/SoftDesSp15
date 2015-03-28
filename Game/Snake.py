"""Softdes SP2015 Project4, game design: snake"""
"""Author: Hieu Nguyen and Ziyi Lan(Jason)"""

import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
green=(170,249,186)
red=(255,0,0)
font=pygame.font.SysFont(None, 60)

clock=pygame.time.Clock()
FPS=20

class Snakehead():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 0

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y


class Display():
    def __init__(self,xspan,yspan,caption):
        self.xspan=xspan
        self.yspan=yspan
        self.caption=caption

class Apple():
    def __init__(self,xspan,yspan):
        self.x=round(random.randrange(0,xspan-10)/10.0)*10
        self.y=round(random.randrange(0,yspan-10)/10.0)*10

def display_text(msg,color):
    text=font.render(msg,True,color)
    return background.blit(text,[300,200])

snakehead=Snakehead(400,300)
gamedefalt=Display(800,600,"Sneaky Snake")
apple=Apple(780,580)

background= pygame.display.set_mode((gamedefalt.xspan,gamedefalt.yspan))
pygame.display.set_caption(gamedefalt.caption)



gameexit= False
while not gameexit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameexit= True 

        if pygame.key.get_focused():
            if pygame.key.get_pressed()[pygame.K_a]:
                snakehead.vel_x=-10
                snakehead.vel_y=0
                snakehead.update()

            elif pygame.key.get_pressed()[pygame.K_d]:
                snakehead.vel_x=10
                snakehead.vel_y=0
                snakehead.update()

            elif pygame.key.get_pressed()[pygame.K_w]:
                snakehead.vel_x=0
                snakehead.vel_y=-10
                snakehead.update()

            elif pygame.key.get_pressed()[pygame.K_s]:
                snakehead.vel_x=0
                snakehead.vel_y=10
                snakehead.update()

    if snakehead.x<=20 or snakehead.x>=770 or snakehead.y<=20 or snakehead.y>=570:
        gameexit= True  

    background.fill(green) #Background color of the game.
    '''Drawing the border of the ground where the snake will be moving'''
    background.fill(black,rect=[0,10,800,10])
    background.fill(black,rect=[0,580,800,10])
    background.fill(black,rect=[10,0,10,600])
    background.fill(black,rect=[780,0,10,600])

    pygame.draw.rect(background,red,[apple.x,apple.y,10,10])
    pygame.draw.rect(background,black,[snakehead.x,snakehead.y,10,10])
    snakehead.update()
    pygame.display.update()
    clock.tick(FPS)

    if snakehead.x==apple.x and snakehead.y==apple.y:
        apple.x=round(random.randrange(20,680-10)/10.0)*10
        apple.y=round(random.randrange(20,480-10)/10.0)*10

display_text("GAME OVER",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()