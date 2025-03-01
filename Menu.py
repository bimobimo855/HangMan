import pygame as pg

#Colors
Black = (0, 0 ,0)
Purple = (146, 123, 180)
Dark_Purple = (100, 71, 141)
White = (255, 255, 255)

Origanal_screen_size= (1470, 956)

def GetFont(size):
    return pg.font.Font("Assets/Font/Lugrasimo-Regular.ttf", size)

def main():
    pg.init()
    pg.display.set_caption("Hangman")
    screen = pg.display.set_mode(Origanal_screen_size, pg.RESIZABLE)
    screen_rect = screen.get_rect()

    is_fullscreen = False
    
    canvas = pg.Surface(Origanal_screen_size).convert()
    canvas_rect = canvas.get_rect()
    Center = (735, 478)
    Boarder = pg.image.load("Assets/Border.png")

    exit = False

    while not exit:
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                exit = True
                break

            if event.type == pg.KEYDOWN and event.key == pg.K_F11:
                is_fullscreen = not is_fullscreen
                screen = pg.display.set_mode(Origanal_screen_size)
                screen_rect = screen.get_rect()
                pg.display.toggle_fullscreen()
                break

            if event.type == pg.VIDEORESIZE and not is_fullscreen:
                screen = pg.display.set_mode(event.size, pg.RESIZABLE)
                screen_rect = screen.get_rect()

    #Main menu with out function
        canvas.fill(pg.Color(Purple))
        text_surface = font=GetFont(30).render("Hangman", False, (White))
        canvas.blit(text_surface, (1000, 100))
        canvas.blit(Boarder, (0,0))

        if screen_rect.size != Origanal_screen_size:
            canvas_rect = canvas_rect.fit(screen_rect)
            canvas_rect.center = screen_rect.center
            CanvaScaled = pg.transform.smoothscale(canvas, canvas_rect.size)
            screen.blit(CanvaScaled, canvas_rect)
        else:
            screen.blit(canvas, (0, 0))

        pg.display.update()

main()