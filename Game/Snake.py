"""Softdes SP2015 Project4, game design: snake"""
"""Author: Hieu Nguyen and Ziyi Lan(Jason)"""

import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
green=(170,249,186)

clock=pygame.time.Clock()
FPS=20

class Snakehead():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 10
        self.vel_y = 0

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y


class Display():
    def __init__(self,xspan,yspan,caption):
        self.xspan=xspan
        self.yspan=yspan
        self.caption=caption

    def display_text(self,msg,color):
        self.font=pygame.font.Sysfont(None,25)
        self.text=font.render(msg,True,color)
        background.

snakehead=Snakehead(400,300)
gamedefalt=Display(800,600,"Sneaky Snake")

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

    if snakehead.pos_x<=20 or snakehead.pos_x>=770 or snakehead.pos_y<=20 or snakehead.pos_y>=570:
        gameexit= True  

    background.fill(green) #Background color of the game.
    '''Drawing the border of the ground where the snake will be moving'''
    background.fill(black,rect=[0,10,800,10])
    background.fill(black,rect=[0,580,800,10])
    background.fill(black,rect=[10,0,10,600])
    background.fill(black,rect=[780,0,10,600])

    pygame.draw.rect(background,black,[snakehead.pos_x,snakehead.pos_y,10,10])
    snakehead.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()