




































# import keyboard
# import pygame
# from pygame import mixer
# import sys
# import time


# #for my own level of satisfaction i am chaning this: letter key sound is being replaced by delete,backspace, etc.
# # I won't be chaning the variable names tho. 


# mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
# pygame.init()
# print(pygame.mixer.get_init())

# last_key_time = {}
# delayed_sounds = {}

# def play_sound(key):

#     global last_key_time, delayed_sounds
#     current_time = time.time()
#     if key.name == 'esc':
#         pygame.quit()
#         sys.exit()
#     elif key.name == 'backspace' or key.name == 'delete' or  key.name == 'tab' or key.name =='shift' or  key.name == 'enter' or key.name == 'comma' or key.name == 'period' or key.name == 'tab':
#         s = pygame.mixer.Sound('delete_enter_comma_options.ogg')
#     elif key.name == 'space':
#         s = pygame.mixer.Sound('space.ogg')
#     else:
#         s = pygame.mixer.Sound('standard-final.ogg')

#     s.set_volume(2)
#     # Check if enough time has elapsed since the last key press
#     if key.name not in last_key_time or current_time - last_key_time[key.name] >= 0.05:
#         ch = s.play()
#         delayed_sounds[key.name] = ch
#         last_key_time[key.name] = current_time

# def stop_sound(key):
#     global delayed_sounds
#     key_name = key.name
#     if key_name in delayed_sounds:
#         delayed_sounds[key_name].stop()

# keyboard.on_press(play_sound)
# keyboard.on_release(stop_sound)
# keyboard.wait('esc')  # Wait for 'esc' key press to exit



























# import keyboard
# import pygame
# from pygame import mixer
# import sys
# import time

# mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
# pygame.init()
# print(pygame.mixer.get_init())

# while True:
#     try:
#         event = keyboard.read_event(suppress=True)
#         if event.event_type == keyboard.KEY_DOWN:
#             if event.name == 'esc':
#                 pygame.quit()
#                 sys.exit()
#             elif event.name == 'backspace' or event.name == 'delete' or event.name == 'enter' or event.name == 'comma' or event.name == 'period' or event.name == 'tab':
#                 s = pygame.mixer.Sound('delete_enter_comma_options.ogg')
#                 ch = s.play()
#                 while pygame.mixer.get_busy():
#                     pygame.time.delay(0)
#                 time.sleep(0.05)  # Introduce a small delay
#             elif event.name == 'space':
#                 s = pygame.mixer.Sound('space.ogg')
#                 ch = s.play()
#                 while pygame.mixer.get_busy():
#                     pygame.time.delay(0)
#                 time.sleep(0.05)  # Introduce a small delay
#             else:
#                 s = pygame.mixer.Sound('standard-final.ogg')
#                 ch = s.play()
#                 while pygame.mixer.get_busy():
#                     pygame.time.delay(0)
#                 time.sleep(0.05)  # Introduce a small delay
#     except KeyboardInterrupt:
#         pygame.quit()
#         sys.exit()
#             