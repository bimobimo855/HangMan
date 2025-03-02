import pygame as pg, sys
from button import ButtonIMAGE

Black = (0, 0 ,0)
Purple = (146, 123, 180)
Dark_Purple = (100, 71, 141)
White = (255, 255, 255)
OffWhite = (232, 232, 232)

pg.init()
pg.display.set_caption("Keyboard")
screen = pg.display.set_mode((2080, 673))

Sound1 = pg.mixer.Sound('Assets/Sound/keyboard-spacebar-hit-101812-[AudioTrimmer.com].mp3')
Sound1.set_volume(0.5)

#Key Postion
KeyPostionQ = 0,0
KeyPostionW = 209,0
KeyPostionE = 418,0
KeyPostionR = 627,0
KeyPostionT = 836,0
KeyPostionY = 1045,0
KeyPostionU = 1254,0
KeyPostionI = 1463,0
KeyPostionO = 1672,0
KeyPostionP = 1881,0
KeyPostionA = 99.5, 209
KeyPostionS = 308.5, 209
KeyPostionD = 517.5, 209
KeyPostionF = 726.5, 209
KeyPostionG = 935.5, 209
KeyPostionH = 1144.5, 209
KeyPostionJ = 1353.5, 209
KeyPostionK = 1562.5, 209
KeyPostionL = 1771.5, 209
KeyPostionZ = 308.5, 418
KeyPostionX = 517.5, 418
KeyPostionC = 726.5, 418
KeyPostionV = 935.5, 418
KeyPostionB = 1144.5, 418
KeyPostionN = 1353.5, 418
KeyPostionM = 1562.5, 418




#Key Images
SqareKey = pg.image.load("Assets/Images/KeYSquare.png")
KeyImageQ = [pg.image.load("Assets/KeyBoard/Letters/Base/1.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/1.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/1.png")
             ]
KeyImageW = [pg.image.load("Assets/KeyBoard/Letters/Base/2.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/2.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/2.png")
             ]
KeyImageE = [pg.image.load("Assets/KeyBoard/Letters/Base/3.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/3.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/3.png")
             ]
KeyImageR = [pg.image.load("Assets/KeyBoard/Letters/Base/4.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/4.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/4.png")
             ]
KeyImageT = [pg.image.load("Assets/KeyBoard/Letters/Base/5.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/5.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/5.png")
             ]
KeyImageY = [pg.image.load("Assets/KeyBoard/Letters/Base/6.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/6.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/6.png")
             ]
KeyImageU = [pg.image.load("Assets/KeyBoard/Letters/Base/7.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/7.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/7.png")
             ]
KeyImageI = [pg.image.load("Assets/KeyBoard/Letters/Base/8.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/8.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/8.png")
             ]
KeyImageO = [pg.image.load("Assets/KeyBoard/Letters/Base/9.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/9.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/9.png")
             ]
KeyImageP = [pg.image.load("Assets/KeyBoard/Letters/Base/10.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/10.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/10.png")
             ]
KeyImageA = [pg.image.load("Assets/KeyBoard/Letters/Base/11.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/11.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/11.png")
             ]
KeyImageS = [pg.image.load("Assets/KeyBoard/Letters/Base/12.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/12.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/12.png")
             ]
KeyImageD = [pg.image.load("Assets/KeyBoard/Letters/Base/13.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/13.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/13.png")
             ]
KeyImageF = [pg.image.load("Assets/KeyBoard/Letters/Base/14.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/14.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/14.png")
             ]
KeyImageG = [pg.image.load("Assets/KeyBoard/Letters/Base/15.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/15.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/15.png")
             ]
KeyImageH = [pg.image.load("Assets/KeyBoard/Letters/Base/16.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/16.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/16.png")
             ]
KeyImageJ = [pg.image.load("Assets/KeyBoard/Letters/Base/17.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/17.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/17.png")
             ]
KeyImageK = [pg.image.load("Assets/KeyBoard/Letters/Base/18.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/18.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/18.png")
             ]
KeyImageL = [pg.image.load("Assets/KeyBoard/Letters/Base/19.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/19.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/19.png")
             ]
KeyImageZ = [pg.image.load("Assets/KeyBoard/Letters/Base/20.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/20.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/20.png")
             ]
KeyImageX = [pg.image.load("Assets/KeyBoard/Letters/Base/21.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/21.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/21.png")
             ]
KeyImageC = [pg.image.load("Assets/KeyBoard/Letters/Base/22.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/22.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/22.png")
             ]
KeyImageV = [pg.image.load("Assets/KeyBoard/Letters/Base/23.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/23.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/23.png")
             ]
KeyImageB = [pg.image.load("Assets/KeyBoard/Letters/Base/24.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/24.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/24.png")
             ]
KeyImageN = [pg.image.load("Assets/KeyBoard/Letters/Base/25.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/25.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/25.png")
             ]
KeyImageM = [pg.image.load("Assets/KeyBoard/Letters/Base/26.png"),
             pg.image.load("Assets/KeyBoard/Letters/No/26.png"),
             pg.image.load("Assets/KeyBoard/Letters/Yes/26.png")
             ]

#KeyIndex
KeyIndexQ = 0
KeyIndexW = 0
KeyIndexE = 0
KeyIndexR = 0
KeyIndexT = 0
KeyIndexY = 0
KeyIndexU = 0
KeyIndexI = 0
KeyIndexO = 0
KeyIndexP = 0
KeyIndexA = 0
KeyIndexS = 0
KeyIndexD = 0
KeyIndexF = 0
KeyIndexG = 0
KeyIndexH = 0
KeyIndexJ = 0
KeyIndexK = 0
KeyIndexL = 0
KeyIndexZ = 0
KeyIndexX = 0
KeyIndexC = 0
KeyIndexV = 0
KeyIndexB = 0
KeyIndexN = 0
KeyIndexM = 0



def KeyBoard():
    while True:
        MOUSE_POS = pg.mouse.get_pos()
        global KeyIndexQ
        #Images
        screen.blit(KeyImageQ[KeyIndexQ], (0, 0))  
        screen.blit(KeyImageW[KeyIndexW], (209, 0))  
        screen.blit(KeyImageE[KeyIndexE], (418, 0))  
        screen.blit(KeyImageR[KeyIndexR], (627, 0))  
        screen.blit(KeyImageT[KeyIndexT], (836, 0))  
        screen.blit(KeyImageY[KeyIndexY], (1045, 0))  
        screen.blit(KeyImageU[KeyIndexU], (1254, 0))  
        screen.blit(KeyImageI[KeyIndexI], (1463, 0))  
        screen.blit(KeyImageO[KeyIndexO], (1672, 0))  
        screen.blit(KeyImageP[KeyIndexP], (1881, 0))  
        screen.blit(KeyImageA[KeyIndexA], (99.5, 209))  
        screen.blit(KeyImageS[KeyIndexS], (308.5, 209))  
        screen.blit(KeyImageD[KeyIndexD], (517.5, 209))  
        screen.blit(KeyImageF[KeyIndexF], (726.5, 209))  
        screen.blit(KeyImageG[KeyIndexG], (935.5, 209))  
        screen.blit(KeyImageH[KeyIndexH], (1144.5, 209))  
        screen.blit(KeyImageJ[KeyIndexJ], (1353.5, 209))  
        screen.blit(KeyImageK[KeyIndexK], (1562.5, 209))  
        screen.blit(KeyImageL[KeyIndexL], (1771.5, 209))  
        screen.blit(KeyImageZ[KeyIndexZ], (308.5, 418))  
        screen.blit(KeyImageX[KeyIndexX], (517.5, 418))  
        screen.blit(KeyImageC[KeyIndexC], (726.5, 418))  
        screen.blit(KeyImageV[KeyIndexV], (935.5, 418))  
        screen.blit(KeyImageB[KeyIndexB], (1144.5, 418))  
        screen.blit(KeyImageN[KeyIndexN], (1353.5, 418))  
        screen.blit(KeyImageM[KeyIndexM], (1562.5, 418))  
        #Buttons
        QBUTTON = ButtonIMAGE(image=SqareKey, pos=(99.5,99.5))
        WBUTTON = ButtonIMAGE(image=SqareKey, pos=(308.5,99.5))
        EBUTTON = ButtonIMAGE(image=SqareKey, pos=(517.5,99.5))
        RBUTTON = ButtonIMAGE(image=SqareKey, pos=(726.5,99.5))
        TBUTTON = ButtonIMAGE(image=SqareKey, pos=(935.5,99.5))
        YBUTTON = ButtonIMAGE(image=SqareKey, pos=(1144.5,99.5))
        UBUTTON = ButtonIMAGE(image=SqareKey, pos=(1353.5,99.5))
        IBUTTON = ButtonIMAGE(image=SqareKey, pos=(1562.5,99.5))
        OBUTTON = ButtonIMAGE(image=SqareKey, pos=(1771.5,99.5))
        PBUTTON = ButtonIMAGE(image=SqareKey, pos=(1980.5,99.5))
        ABUTTON = ButtonIMAGE(image=SqareKey, pos=(199, 321.5))
        SBUTTON = ButtonIMAGE(image=SqareKey, pos=(408, 321.5))
        DBUTTON = ButtonIMAGE(image=SqareKey, pos=(617, 321.5))
        FBUTTON = ButtonIMAGE(image=SqareKey, pos=(826, 321.5))
        GBUTTON = ButtonIMAGE(image=SqareKey, pos=(1035, 321.5))
        HBUTTON = ButtonIMAGE(image=SqareKey, pos=(1244, 321.5))
        JBUTTON = ButtonIMAGE(image=SqareKey, pos=(1453, 321.5))
        KBUTTON = ButtonIMAGE(image=SqareKey, pos=(1662, 321.5))
        LBUTTON = ButtonIMAGE(image=SqareKey, pos=(1871, 321.5))
        ZBUTTON = ButtonIMAGE(image=SqareKey, pos=(408, 543.5))
        XBUTTON = ButtonIMAGE(image=SqareKey, pos=(617, 543.5))
        CBUTTON = ButtonIMAGE(image=SqareKey, pos=(826, 543.5))
        VBUTTON = ButtonIMAGE(image=SqareKey, pos=(1035, 543.5))
        BBUTTON = ButtonIMAGE(image=SqareKey, pos=(1244, 543.5))
        NBUTTON = ButtonIMAGE(image=SqareKey, pos=(1452.5, 543.5))
        MBUTTON = ButtonIMAGE(image=SqareKey, pos=(1661.5, 543.5))

        for button in [QBUTTON,WBUTTON,EBUTTON,RBUTTON,TBUTTON,YBUTTON,UBUTTON,IBUTTON,OBUTTON,PBUTTON,ABUTTON,SBUTTON,DBUTTON,FBUTTON,GBUTTON,HBUTTON,JBUTTON,KBUTTON,LBUTTON,ZBUTTON,XBUTTON,CBUTTON,VBUTTON,BBUTTON,NBUTTON,MBUTTON]:
                button.update(screen)


        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:
                    if event.type == pg.MOUSEBUTTONDOWN and QBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_q):
                        QIMAGE()
                        Sound1.play()
                    
                    if event.type == pg.MOUSEBUTTONDOWN and WBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_w):
                        WIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and EBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_e):
                        EIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and RBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_r):
                        RIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and TBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_t):
                        TIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and YBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_y):
                        YIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and UBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_u):
                        UIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and IBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_i):
                        IIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and OBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_o):
                        OIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and PBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_p):
                        PIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and ABUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_a):
                        AIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and SBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_s):
                        SIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and DBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_d):
                        DIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and FBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_f):
                        FIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and GBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_g):
                        GIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and HBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_h):
                        HIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and JBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_j):
                        JIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and KBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_k):
                        KIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and LBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_l):
                        LIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and ZBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_z):
                        ZIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and XBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_x):
                        XIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and CBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_c):
                        CIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and VBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_v):
                        VIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and BBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_b):
                        BIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and NBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_n):
                        NIMAGE()
                        Sound1.play()
                        
                    if event.type == pg.MOUSEBUTTONDOWN and MBUTTON.checkForInput(MOUSE_POS) or (event.type == pg.KEYDOWN and event.key == pg.K_m):
                        MIMAGE()
                        Sound1.play()

        pg.display.update()

def QIMAGE():
    global KeyIndexQ 
    KeyIndexQ = (KeyIndexQ + 1) % len(KeyImageQ)
    screen.blit(KeyImageQ[KeyIndexQ], (0, 0)) 
    pg.display.update((0, 0, 199, 244))

def WIMAGE():
    global KeyIndexW 
    KeyIndexW = (KeyIndexW + 1) % len(KeyImageW)
    screen.blit(KeyImageW[KeyIndexW], (209, 0)) 
    pg.display.update((209, 0, 199, 244))

def EIMAGE():
    global KeyIndexE 
    KeyIndexE = (KeyIndexE + 1) % len(KeyImageE)
    screen.blit(KeyImageE[KeyIndexE], (418, 0)) 
    pg.display.update((418, 0, 199, 244))

def RIMAGE():
    global KeyIndexR 
    KeyIndexR = (KeyIndexR + 1) % len(KeyImageR)
    screen.blit(KeyImageR[KeyIndexR], (627, 0)) 
    pg.display.update((627, 0, 199, 244))

def TIMAGE():
    global KeyIndexT 
    KeyIndexT = (KeyIndexT + 1) % len(KeyImageT)
    screen.blit(KeyImageT[KeyIndexT], (836, 0)) 
    pg.display.update((836, 0, 199, 244))

def YIMAGE():
    global KeyIndexY 
    KeyIndexY = (KeyIndexY + 1) % len(KeyImageY)
    screen.blit(KeyImageY[KeyIndexY], (1045, 0)) 
    pg.display.update((1045, 0, 199, 244))

def UIMAGE():
    global KeyIndexU 
    KeyIndexU = (KeyIndexU + 1) % len(KeyImageU)
    screen.blit(KeyImageU[KeyIndexU], (1254, 0)) 
    pg.display.update((1254, 0, 199, 244))

def IIMAGE():
    global KeyIndexI 
    KeyIndexI = (KeyIndexI + 1) % len(KeyImageI)
    screen.blit(KeyImageI[KeyIndexI], (1463, 0)) 
    pg.display.update((1463, 0, 199, 244))

def OIMAGE():
    global KeyIndexO 
    KeyIndexO = (KeyIndexO + 1) % len(KeyImageO)
    screen.blit(KeyImageO[KeyIndexO], (1672, 0)) 
    pg.display.update((1672, 0, 199, 244))

def PIMAGE():
    global KeyIndexP 
    KeyIndexP = (KeyIndexP + 1) % len(KeyImageP)
    screen.blit(KeyImageP[KeyIndexP], (1881, 0)) 
    pg.display.update((1881, 0, 199, 244))

def AIMAGE():
    global KeyIndexA 
    KeyIndexA = (KeyIndexA + 1) % len(KeyImageA)
    screen.blit(KeyImageA[KeyIndexA], (99.5, 209)) 
    pg.display.update((99.5, 209, 199, 244))

def SIMAGE():
    global KeyIndexS 
    KeyIndexS = (KeyIndexS + 1) % len(KeyImageS)
    screen.blit(KeyImageS[KeyIndexS], (308.5, 209)) 
    pg.display.update((308.5, 209, 199, 244))

def DIMAGE():
    global KeyIndexD 
    KeyIndexD = (KeyIndexD + 1) % len(KeyImageD)
    screen.blit(KeyImageD[KeyIndexD], (517.5, 209)) 
    pg.display.update((517.5, 209, 199, 244))

def FIMAGE():
    global KeyIndexF 
    KeyIndexF = (KeyIndexF + 1) % len(KeyImageF)
    screen.blit(KeyImageF[KeyIndexF], (726.5, 209)) 
    pg.display.update((726.5, 209, 199, 244))

def GIMAGE():
    global KeyIndexG 
    KeyIndexG = (KeyIndexG + 1) % len(KeyImageG)
    screen.blit(KeyImageG[KeyIndexG], (935.5, 209)) 
    pg.display.update((935.5, 209, 199, 244))

def HIMAGE():
    global KeyIndexH 
    KeyIndexH = (KeyIndexH + 1) % len(KeyImageH)
    screen.blit(KeyImageH[KeyIndexH], (1144.5, 209)) 
    pg.display.update((1144.5, 209, 199, 244))

def JIMAGE():
    global KeyIndexJ 
    KeyIndexJ = (KeyIndexJ + 1) % len(KeyImageJ)
    screen.blit(KeyImageJ[KeyIndexJ], (1353.5, 209)) 
    pg.display.update((1353.5, 209, 199, 244))

def KIMAGE():
    global KeyIndexK 
    KeyIndexK = (KeyIndexK + 1) % len(KeyImageK)
    screen.blit(KeyImageK[KeyIndexK], (1562.5, 209)) 
    pg.display.update((1562.5, 209, 199, 244))

def LIMAGE():
    global KeyIndexL 
    KeyIndexL = (KeyIndexL + 1) % len(KeyImageL)
    screen.blit(KeyImageL[KeyIndexL], (1771.5, 209)) 
    pg.display.update((1771.5, 209, 199, 244))

def ZIMAGE():
    global KeyIndexZ 
    KeyIndexZ = (KeyIndexZ + 1) % len(KeyImageZ)
    screen.blit(KeyImageZ[KeyIndexZ], (308.5, 418)) 
    pg.display.update((308.5, 418, 199, 244))

def XIMAGE():
    global KeyIndexX 
    KeyIndexX = (KeyIndexX + 1) % len(KeyImageX)
    screen.blit(KeyImageX[KeyIndexX], (517.5, 418)) 
    pg.display.update((517.5, 418, 199, 244))

def CIMAGE():
    global KeyIndexC 
    KeyIndexC = (KeyIndexC + 1) % len(KeyImageC)
    screen.blit(KeyImageC[KeyIndexC], (726.5, 418)) 
    pg.display.update((726.5, 418, 199, 244))

def VIMAGE():
    global KeyIndexV 
    KeyIndexV = (KeyIndexV + 1) % len(KeyImageV)
    screen.blit(KeyImageV[KeyIndexV], (935.5, 418)) 
    pg.display.update((935.5, 418, 199, 244))

def BIMAGE():
    global KeyIndexB 
    KeyIndexB = (KeyIndexB + 1) % len(KeyImageB)
    screen.blit(KeyImageB[KeyIndexB], (1144.5, 418)) 
    pg.display.update((1144.5, 418, 199, 244))

def NIMAGE():
    global KeyIndexN 
    KeyIndexN = (KeyIndexN + 1) % len(KeyImageN)
    screen.blit(KeyImageN[KeyIndexN], (1353.5, 418)) 
    pg.display.update((1353.5, 418, 199, 244))

def MIMAGE():
    global KeyIndexM 
    KeyIndexM = (KeyIndexM + 1) % len(KeyImageM)
    screen.blit(KeyImageM[KeyIndexM], (1562.5, 418)) 
    pg.display.update((1562.5, 418, 199, 244))




KeyBoard()
 



    

