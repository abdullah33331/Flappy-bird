import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700,800))
pygame.display.set_caption('Fail')

font = pygame.font.SysFont(None,105)

def write(text,font,text_col,x,y):
    texty = font.render(text,True,text_col)
    screen.blit(texty,(x,y))

run = True
while run:
    screen.fill((255,0,255))
    write("FAILED",font,(255,255,0),180,320)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.flip()        

pygame.quit()
sys.exit()            