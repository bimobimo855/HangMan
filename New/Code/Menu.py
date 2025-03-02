import pygame as pg, sys
from button import Button
from button import ButtonIMAGE
from pygame import mixer

mixer.init()
#music
volume_music = [0,0.1,0.3,0.5]
mixer.music.load('Assets/Sound/City Date-a-bgm-asset-pack/Blithe part B.ogg')
mixer.music.set_volume(volume_music[3])
mixer.music.play(-1)
#sound effect
volume_sound = [0,0.1,0.3,0.5]
Sound1 = pg.mixer.Sound('Assets/Sound/keyboard-spacebar-hit-101812-[AudioTrimmer.com].mp3')
Sound1.set_volume(volume_sound[3])


#Colors
Black = (0, 0 ,0)
Purple = (146, 123, 180)
Dark_Purple = (100, 71, 141)
White = (255, 255, 255)
OffWhite = (232, 232, 232)

#Images
Boarder = pg.image.load("Assets/Images/Border.png")
LolitaBunny = pg.image.load("Assets/Images/Lolita Bunny.png")
VolumeSquare = pg.image.load("Assets/Images/Volume Square.png")
Back = pg.image.load("Assets/Images/Back.png")
PlayButton = pg.image.load("Assets/Images/PlayRect.png")
OptionButton = pg.image.load("Assets/Images/QuitRect.png")
ButtonDiffulcuty = pg.image.load("Assets/Images/Button.png")

VolumeImage = [
    pg.image.load("Assets/Images/Volume(0).png"),
    pg.image.load("Assets/Images/Volume(1).png"),
    pg.image.load("Assets/Images/Volume(2).png"),
    pg.image.load("Assets/Images/Volume(3).png"),
]
VolumeMusicImageIndex = 3
VolumeSoundImageIndex = 3 

VolumeMusicIndex = 3
VolumeSoundIndex = 3


Origanal_screen_size= (1470, 956)
screen = pg.display.set_mode(Origanal_screen_size)


pg.init()
pg.display.set_caption("Hangman")

def GetFontSmall(size):
    return pg.font.Font("Assets/Font/Dangrek/Dangrek-Regular.ttf", size)
def GetFont(size):
    return pg.font.Font("Assets/Font/Modak-Regular.ttf", size)

def CenterText(text_render):
    text_rect = text_render.get_rect()
    text_rect.center = (735, 478)
    return(text_render, text_rect)


def MainMenu():
        while True:
            MOUSE_POS = pg.mouse.get_pos()

            screen.fill(pg.Color(Purple))     
            screen.blit(Boarder, (0,0))
            screen.blit(LolitaBunny, (1124, 84))

            PLAY_BUTTON = Button(image= PlayButton, pos=(735, 460), 
                                text_input="PLAY", font=GetFont(120), base_color=(OffWhite), hovering_color=(White))
            OPTIONS_BUTTON = Button(image= OptionButton, pos=(735, 681), 
                                text_input="OPTIONS", font=GetFont(70), base_color=(OffWhite), hovering_color=(White))

            for button in [PLAY_BUTTON, OPTIONS_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
        
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MOUSE_POS):
                        Sound1.play()
                        PlayScreen()
                    if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                        Sound1.play()
                        OptionsScreen()
            pg.display.update()

def PlayScreen():
    while True:
        Play_MOUSE_POS = pg.mouse.get_pos()

        screen.fill(Purple)
        screen.blit(Boarder, (0,0))
        #High score
        Score = GetFont(120).render("High Score", False, (White))
        screen.blit(Score,(436,100))

        EASY_BUTTON = Button(image= ButtonDiffulcuty, pos=(735, 335), 
                                text_input="Easy", font=GetFont(80), base_color=(OffWhite), hovering_color=(White))
        MEDIUM_BUTTON = Button(image= ButtonDiffulcuty, pos=(735, 475), 
                                text_input="MEDIUM", font=GetFont(60), base_color=(OffWhite), hovering_color=(White))
        HARD_BUTTON = Button(image= ButtonDiffulcuty, pos=(735, 615), 
                                text_input="HARD", font=GetFont(80), base_color=(OffWhite), hovering_color=(White))
        Back_BUTTON = ButtonIMAGE(image=Back, pos=(735, 775))

        for button in [Back_BUTTON]:
            button.update(screen)

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
                button.changeColor(Play_MOUSE_POS)
                button.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if Back_BUTTON.checkForInput(Play_MOUSE_POS):
                    Sound1.play()
                    return
                
                if EASY_BUTTON.checkForInput(Play_MOUSE_POS):
                    Sound1.play()

                if MEDIUM_BUTTON.checkForInput(Play_MOUSE_POS):
                    Sound1.play()

                if HARD_BUTTON.checkForInput(Play_MOUSE_POS):
                    Sound1.play()

                

        pg.display.update()

def OptionsScreen():
    while True:
        OPTION_MOUSE_POS = pg.mouse.get_pos()
        global VolumeMusicImageIndex
        global VolumeSoundImageIndex
        global VolumeMusicIndex 
        global VolumeSoundIndex 


        screen.fill(Purple)
        screen.blit(Boarder, (0,0))
        text_sound = GetFontSmall(120).render("SOUND", True, White)
        screen.blit(text_sound, (370,410))
        text_music = GetFontSmall(120).render("MUSIC", True, White)
        screen.blit(text_music, (370,150))

        screen.blit(VolumeImage[VolumeMusicImageIndex], (867.5, 182.5))
        screen.blit(VolumeImage[VolumeSoundImageIndex], (867.5, 442.5))

        Music_BUTTON = ButtonIMAGE(image=VolumeSquare, pos=(935, 250))
        Sound_BUTTON = ButtonIMAGE(image=VolumeSquare, pos=(935, 510))
        Back_BUTTON = ButtonIMAGE(image=Back, pos=(735, 750))

        for button in [Music_BUTTON, Sound_BUTTON, Back_BUTTON]:
            button.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if Music_BUTTON.checkForInput(OPTION_MOUSE_POS):
                    Sound1.play()
                    MusicImage()
                    

                if Sound_BUTTON.checkForInput(OPTION_MOUSE_POS):
                    Sound1.play()
                    SoundImage()
                
                if Back_BUTTON.checkForInput(OPTION_MOUSE_POS):
                    Sound1.play()
                    return 

        pg.display.update()

def MusicImage():
    global VolumeMusicImageIndex
    global VolumeMusicIndex  
    VolumeMusicIndex = (VolumeMusicIndex + 1)% len(volume_sound)
    VolumeMusicImageIndex = (VolumeMusicImageIndex + 1) % len(VolumeImage) 
    screen.blit(VolumeImage[VolumeMusicImageIndex], (867.5, 182.5))  
    mixer.music.set_volume(volume_music[VolumeMusicIndex])
    pg.display.update((867.5, 182.5,135,135))

def SoundImage(): 
    global VolumeSoundImageIndex  
    global VolumeSoundIndex 
    VolumeSoundIndex = (VolumeSoundIndex + 1) % len(volume_sound)
    VolumeSoundImageIndex = (VolumeSoundImageIndex + 1) % len(VolumeImage) 
    screen.blit(VolumeImage[VolumeSoundImageIndex ], (867.5, 442.5))  
    Sound1.set_volume(volume_sound[VolumeSoundIndex])
    pg.display.update((867.5, 442.5, 135 , 135))

#Keys


MainMenu()