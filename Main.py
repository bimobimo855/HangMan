import pygame,sys
import random
from button import Button

#Colors
Black = (0, 0 ,0)
Purple = (146, 123, 180)
Dark_Purple = (100, 71, 141)
White = (255, 255, 255)

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Menu")

def full_screen():
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



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

def get_font(size):  # Returns the font in the desired size
    return pygame.font.Font("UI/Assets/Font/Lugrasimo/Lugrasimo-Regular.ttf", size)

def display_word(word):
    while True:
        SCREEN.fill("white")

        WORD_MOUSE_POS = pygame.mouse.get_pos()

        word_text = get_font(45).render(word, True, "Black")
        word_rect = word_text.get_rect(center=(640, 360))  # Center the text
        SCREEN.blit(word_text, word_rect)

        BACK_BUTTON = Button(image=pygame.image.load("UI/Assets/Play Rect.png"), pos=(640, 550), 
                                text_input="Back", font=get_font(75), base_color="Black", hovering_color="Black")
        
        for button in [BACK_BUTTON]:
                button.changeColor(WORD_MOUSE_POS)
                button.update(SCREEN)

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(WORD_MOUSE_POS):
                        play_menu()

        pygame.display.flip()

def Easy():
    word = get_random_word(easy_word_list)
    display_word(word)

def Medium():
    word = get_random_word(medium_word_list)
    display_word(word)

def Hard():
    word = get_random_word(hard_word_list)
    display_word(word)

def wait_for_exit():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to return to the main menu
                    return

def play_menu():
    while True:
        SCREEN.fill(White)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(image=pygame.image.load("UI/Assets/Play Rect.png"), pos=(640, 250), 
                             text_input="Easy", font=get_font(75), base_color="Black", hovering_color="Black")
        MEDIUM_BUTTON = Button(image=pygame.image.load("UI/Assets/Play Rect.png"), pos=(640, 400), 
                               text_input="Medium", font=get_font(75), base_color="Black", hovering_color="Black")
        HARD_BUTTON = Button(image=pygame.image.load("UI/Assets/Play Rect.png"), pos=(640, 550), 
                             text_input="Hard", font=get_font(75), base_color="Black", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load("UI/Assets/Quit.png"), pos=(800, 550), 
                             text_input="", font=get_font(75), base_color="Black", hovering_color="Black")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        

        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Easy()
                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Medium()
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Hard()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Escape()
                if event.type == pygame.K_UP():
                    full_screen()

        pygame.display.update()

# Start the game
play_menu()

def Escape():
    pygame.quit()
    sys.exit()


# Sound
    #Effect
    #music

# Fonts
def get_font(size):  # Returns the font in the desired size
    return pygame.font.Font("UI/Assets/Font/Lugrasimo/Lugrasimo-Regular.ttf", size)

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

