import pygame
from pygame.locals import *


color_1 = (210,0,20)#RGB value of color 1
color_2 = (21,12,211)#RGB value of color 2
color_n = (240,240,240)#RGB value of color n


pygame.init()


w, h = 800,600#Width dimension, #Height dimension
screen = pygame.display.set_mode((w, h))


img = pygame.image.load(r'sprites/bird.png')
img.convert()
img = pygame.transform.rotozoom(img,0,0.1)


rect = img.get_rect()
rect.center = w//2, h//2


running = True
moving = False


while running:
   for event in pygame.event.get():


       if event.type == QUIT:
           running = False


       elif event.type == MOUSEBUTTONDOWN:
          if rect.collidepoint(event.pos):
              moving = True  


       elif event.type == MOUSEBUTTONUP:          
           moving = False


       elif event.type == MOUSEMOTION and moving:
           rect.move_ip(event.rel)  


   screen.fill(color_1)
   screen.blit(img, rect)


   #pygame.draw.rect(screen, color_2, rect, 2)


   pygame.display.update()


pygame.quit()