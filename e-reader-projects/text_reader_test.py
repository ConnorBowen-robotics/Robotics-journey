import readchar
from readchar import key
import os
import sys 
import pygame
#this is the start of the page
b = 0
new_page = 1000
page_num = 1

#loads and enables sounds in python
pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('page_turn.wav')

with open("odyssey.txt", "r") as file:
    content = file.read()
    max_pages = len(content)
    while(b < max_pages):
        cut_point = content.rfind(" ", b, new_page)
        if cut_point == -1:
            break
        page = content[b:cut_point]
        print(page)
        while True:
            key_press = readchar.readkey()
            if key_press == key.RIGHT:
                sound.play()
                break
            elif key_press == 'q':
                print(f"\n\nThank you for reading! :)")
                print(f"please have a good day!")
                exit()
        b = cut_point + 1
        new_page += 1000
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n--- Page {page_num} ---")
        page_num += 1