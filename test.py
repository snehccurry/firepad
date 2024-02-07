import keyboard
import pygame
from pygame import mixer
import sys
import time






#mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=4096)
pygame.init()
print(pygame.mixer.get_init())



sleeping=False

delete_enter_comma_options = pygame.mixer.Sound('delete_enter_comma_options.ogg')
space = pygame.mixer.Sound('space.ogg')
standard = pygame.mixer.Sound('standard-final1.ogg')

delete_enter_comma_options.set_volume(1)
space.set_volume(1)
standard.set_volume(1)
#for my own level of satisfaction i am chaning this: letter key sound is being replaced by delete,backspace, etc.
# I won't be chaning the variable names tho. 

def sleep_now():
    global sleeping
    if(sleeping==True):
        sleeping=False
    else:
        sleeping=True

keyboard.add_hotkey('ctrl + shift + k', sleep_now)

def play_sound(key):
    global sleeping
    if(sleeping==False):
        if key.name == 'ctrl+shif+q':
            print("going bye,")
            pygame.quit()
            sys.exit()
        elif key.name == 'backspace' or key.name=='esc' or key.name=='windows' or key.name=='alt' or key.name == 'delete' or  key.name == 'tab' or key.name =='shift' or  key.name == 'return' or key.name == 'comma' or key.name == 'period' or key.name == 'tab' or key.name== 'up' or key.name=='down' or key.name=='right' or key.name=='left':
            delete_enter_comma_options.play()

        elif key.name == 'space':
            space.play()
        else:
            standard.play()
    else:
        pass




keyboard.on_press(play_sound)
#keyboard.on_release()
keyboard.wait('ctrl+shift+q')  # Wait for 'esc' key press to exit

















