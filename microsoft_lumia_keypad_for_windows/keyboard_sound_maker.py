standard = 'keypress_wp7_standard.ogg'
delete = 'keypress_wp7_delete.ogg'
space='keypress_wp7_spacebar.ogg'
enter='keypress_wp7_return.ogg'
import pygame
from pygame import *
import sys

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
print (pygame.mixer.get_init()) 
screen=pygame.display.set_mode((400,400),0,32) 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key!=K_BACKSPACE:
                s = pygame.mixer.Sound(standard)
                ch = s.play()
                while ch.get_busy():
                    pygame.time.delay(10)
            elif event.key==K_BACKSPACE or evet.key==K_DELETE:
                s = pygame.mixer.Sound(delete)
                ch = s.play()
                while ch.get_busy():
                    pygame.time.delay(10)
            elif event.key==K_SPACE:
                print("worked")
                s = pygame.mixer.Sound(space)
                ch = s.play()
                while ch.get_busy():
                    pygame.time.delay(10)
            elif event.key==K_RETURN:
                s = pygame.mixer.Sound(space)
                ch = s.play()
                while ch.get_busy():
                    pygame.time.delay(10)
    pygame.display.update()