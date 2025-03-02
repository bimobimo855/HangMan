import pygame,sys
import random

#Colors
Black = (0, 0 ,0)
Purple = (146, 123, 180)
Dark_Purple = (100, 71, 141)
White = (255, 255, 255)

# Initialize Pygame
pygame.init()



# Load word lists once at the start
def load_word_lists():
    easy_words, medium_words, hard_words = [], [], []
    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            if 4 <= len(word) <= 5:
                easy_words.append(word)
            elif 6 <= len(word) <= 7:
                medium_words.append(word)
            elif len(word) >= 8:
                hard_words.append(word)
    return easy_words, medium_words, hard_words

# Word random selection
easy_word_list, medium_word_list, hard_word_list = load_word_lists()

def get_random_word(word_list):
    return random.choice(word_list)


# Start the game


# Sound
    #Effect
    #music

# Fonts

#Main screen 

#Play Button
#Quit Button
#Option Button

# Option Page 
# Volume Settting
   #Music
   #Sounds 
# Font Settting

# Play Screen
# High Score Display
# Diffculty Buttons

# Scoring 
    #Points add until lose then final score (cant change diffculty of run)
# Easy 
    #Start points (50)
    #Correct guess points (+5)
    #Incorect guess points (-5)

# Meduim 
    #Start points (100)
    #Correct guess points (+10)
    #Incorect guess points (-10)

# Hard 
    #Start points (150)
    #Correct guess points (+15)
    #Incorect guess points (-15)

