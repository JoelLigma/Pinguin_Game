# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:53:35 2020
@authors: Joel, Hannah, Ben
@artwork: Po Wing Chu
"""
 
# import modules
import pygame, pickle, os, sys, random
import pygame.freetype
from pygame import mixer
folder = 'Images and sounds' 

pygame.init()
mixer.init()

# global variables
WIDTH = 1920 
HEIGHT = 1020
LANE = int(HEIGHT/13)

# set caption for game window
pygame.display.set_caption('Pinguin Game')
# set resolution
screen = pygame.display.set_mode((WIDTH, HEIGHT))
framerate = 48
bg_color = pygame.Color("snow1")
fg_color = pygame.Color("lightskyblue") 

# load menu pictures and music files
background_image = pygame.image.load(os.path.join(folder,"peng_peek.png")).convert_alpha()
background_image = pygame.transform.smoothscale(background_image, (500,500))

background_image2 = pygame.image.load(os.path.join(folder,'peng_scoreboard.png')).convert_alpha()
background_image2 = pygame.transform.smoothscale(background_image2, (600,600))

background_image3 = pygame.image.load(os.path.join(folder,"peng_Q.png")).convert_alpha()
background_image3 = pygame.transform.smoothscale(background_image3, (550,550))

background_image4 = pygame.image.load(os.path.join(folder,"peng_right.png")).convert_alpha()
background_image4 = pygame.transform.smoothscale(background_image4, (400,400))

background_image5 = pygame.image.load(os.path.join(folder,"peng_thankyou.png"))
background_image5 = pygame.transform.smoothscale(background_image5, (225,225))

background_image6 = pygame.image.load(os.path.join(folder,"control.png")).convert_alpha()
background_image6 = pygame.transform.smoothscale(background_image6, (750,750))

background_image8 = pygame.image.load(os.path.join(folder,"tutorial3.png")).convert_alpha()
background_image8 = pygame.transform.scale(background_image8, (540,70))

# https://www.google.com/search?q=red+arrow+png&tbm=isch&ved=2ahUKEwjZ_Oym3sPtAhWK5RoKHW2TAQ8Q2-cCegQIABAA&oq=red+arrow+png&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoFCAAQsQM6CAgAELEDEIMBOgQIABBDOgcIABCxAxBDOgoIABCxAxCDARBDULSPA1jdmgNg05sDaABwAHgAgAFYiAHOBpIBAjEzmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=uT_SX5m8GorLa-2mhng&bih=912&biw=1920&rlz=1C1CHBF_enUS902US902#imgrc=zTJotvu7FQFKPM
background_image9 = pygame.image.load(os.path.join(folder,"r_arrow.png")).convert_alpha()
background_image9 = pygame.transform.scale(background_image9, (100,100))
background_image9 = pygame.transform.rotate(background_image9, 270)

background_image10 = pygame.image.load(os.path.join(folder,'bear.png')).convert_alpha()
background_image10 = pygame.transform.smoothscale(background_image10, (300,300))

background_image11 = pygame.image.load(os.path.join(folder,'floating_ice_1920x1080.png')).convert_alpha()
background_image11 = pygame.transform.smoothscale(background_image11, (400,200))

background_fish = pygame.image.load(os.path.join(folder,'orange_fish.png')).convert_alpha()
background_fish = pygame.transform.smoothscale(background_fish, (80,80))

background_image14 = pygame.image.load(os.path.join(folder,'peng_group1.png')).convert_alpha()
background_image14 = pygame.transform.smoothscale(background_image14, (160,160))

background_image15 = pygame.image.load(os.path.join(folder,'peng_luck.png')).convert_alpha()
background_image15 = pygame.transform.smoothscale(background_image15, (1400,1400))

intro_peng = pygame.image.load(os.path.join(folder,'intro_peng.png')).convert_alpha()
intro_peng = pygame.transform.smoothscale(intro_peng, (300,300))

glacier = pygame.image.load(os.path.join(folder, "glacier.png")).convert_alpha()
glacier = pygame.transform.smoothscale(glacier, (WIDTH, LANE))



# load sound and music
# https://freesound.org/people/complex_waveform/sounds/213148/
click_sound = pygame.mixer.Sound(os.path.join(folder,"click.wav"))

# https://freesound.org/people/joshuaempyre/sounds/251461/
mixer.music.load(os.path.join(folder,"arcade-music.wav"))
mixer.music.set_volume(0.05)

class Menu_button() :

    def __init__(self, text, width, height, bg_color, fg_color, size, y=0,x=0):
        """ 
        Text, size, gf_color and bg_color are the same as in text_surface().
        width = button width 
        height = button height
        y = extra term added to height to make changing button position easier.
        function = button functionality on click
        """
        self.text = text
        # create default and interaction image with helper function
        self.default_image = text_surface(text, size, bg_color, fg_color)
        self.interact_image = text_surface(text, size * 1.2, bg_color, fg_color)
        # add images to list 
        self.images = [self.default_image, self.interact_image]
        self.rects = [self.default_image.get_rect(center=(width/2 + x, height//1.8 + y)),
                      self.interact_image.get_rect(center=(width/2 + x, height//1.8 + y))]
        # mouse over rect True/False
        self.hovered = False

    # class methods
    def draw(self, surface):
        """
        Updates the surface depending on mouse movement.
        """
        if self.hovered:
             surface.blit(self.images[1], self.rects[1])
        else:
            surface.blit(self.images[0], self.rects[0])
     
    def handling_events(self, event):
        """
        Interaction with buttons.
        """
        if event.type == pygame.MOUSEMOTION:
            # detect if mouse over button
            self.hovered = self.rects[1].collidepoint(event.pos)
        # in case button is clicked...
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                # play sound when click registered
                click_sound.play()
                return True
            
def get_colour(x):
    """
    This function returns the color of the font for first, second and third place.
    """
    if x == 0:
        return "yellow1"
    elif x == 1:
        return "white"
    elif x == 2:
        return "lightgoldenrod4"
    else:
        return "darkgray"

def get_pos(x):
    """
    This function returns the text to print for frist, second and third place.
    """
    if x == 0:
        return "1st"
    elif x == 1:
        return "2nd"
    elif x == 2:
        return "3rd"
    else:
        return str(x+1)+"th"    

def rotate_image(surface, angle):
    """
    Source: https://www.youtube.com/watch?v=eGsMMpAglIg
    """
    # -angle for clockwise rotation
    rotated_surface = pygame.transform.rotozoom(surface, -angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(WIDTH//2 , HEIGHT//2))
    
    return rotated_surface, rotated_rect

def main():
    """
    Run this function to start the menu screen.
    """
    # set clock for framerate
    clock = pygame.time.Clock()
    # create menu buttons
    start_button = Menu_button("Start Game", WIDTH, HEIGHT, bg_color, fg_color, 30)
    highscore_button = Menu_button("Highscores", WIDTH, HEIGHT, bg_color, fg_color, 30, 50)
    tutorial_button = Menu_button("Tutorial", WIDTH, HEIGHT, bg_color, fg_color, 30, 100)
    credits_button = Menu_button("Credits", WIDTH, HEIGHT, bg_color, fg_color, 30, 150)
    settings_button = Menu_button("Settings", WIDTH, HEIGHT, bg_color, fg_color, 30, 200)
    quit_button = Menu_button("Quit", WIDTH, HEIGHT, bg_color, fg_color, 30, 250)
    return_button = Menu_button("Return to Main Menu", WIDTH, HEIGHT, bg_color, fg_color, 30,200)
    next_button = Menu_button("Next", WIDTH, HEIGHT, bg_color, fg_color, 30, x=450)
    back_button = Menu_button("Back", WIDTH, HEIGHT, bg_color, fg_color, 30, x=-450, y=-5) 

    # initialize variable window to switch between windows
    music_playing = False
    window = 'intro'    
    active = True
    angle = 0
    already_open = False
    menu_open_time = 0

    # load scoreboard if file exists
    scoreboard = load_highscores()
    # main main_menu loop
    while active:
        for event in pygame.event.get():
            # handling user input
            if event.type == pygame.KEYDOWN:   
                if window == "intro":
                    window = "main_menu" 
                elif event.key == pygame.K_ESCAPE:
                    if window != "main_menu":
                        window = "main_menu"
                    else: 
                        active = False
            # end game by closing the window
            elif event.type == pygame.QUIT:
                    active = False
                                
            # handling events in main menu window
            elif window=="main_menu":
                if not music_playing:
                    mixer.music.play(-1) # infinite loop 
                    music_playing = True
                # handle start game events
                if start_button.handling_events(event):
                    # to stop idle timer while in game
                    already_open = False
                    # start the game
                    active = main_gameplay()
                    # restart the music after returning to the menu
                    if active != False:
                        scoreboard = active
                        active = True
                    music_playing = False
                elif highscore_button.handling_events(event):
                    window = 'highscores'
                    already_open = False
                elif tutorial_button.handling_events(event):
                    window = 'tutorial'
                    already_open = False
                elif credits_button.handling_events(event):
                    window = 'credits'
                    already_open = False
                elif settings_button.handling_events(event):
                    window = 'settings'
                    already_open = False
                else :
                    if quit_button.handling_events(event):
                        active = False
                    
            # handling events in highscores window
            elif window == "highscores":                                        
                if return_button.handling_events(event):
                    window = "main_menu"
                    
            # handling events in tutorial window
            elif window == "tutorial":
                if return_button.handling_events(event):
                    window = "main_menu"
                elif next_button.handling_events(event):
                    window = "tutorial2"
                    
            # handling events in tutorial2 window
            elif window == "tutorial2":
                if back_button.handling_events(event):
                    window = "tutorial"
                elif next_button.handling_events(event):
                    window = "tutorial3"
                    
            # handling events in tutorial3 window
            elif window == "tutorial3":
                if back_button.handling_events(event):
                    window = "tutorial2"
                elif next_button.handling_events(event):
                    window = "tutorial4"
            
            # handling events in tutorial4 window
            elif window == "tutorial4":
                if back_button.handling_events(event):
                    window = "tutorial3"
                          
            # handling events in credits window
            elif window == "credits":
                    if return_button.handling_events(event):
                        window = "main_menu"
            # handling events in settings window
            else:
                if window == "settings":
                    if return_button.handling_events(event):
                        window = "main_menu"
        # draws
        screen.fill(fg_color)
        
        # intro layout
        if window=="intro" :
            pygame.mixer.music.stop()
            # text in SpaceObsessed.ttf source: https://en.m.fontke.com/font/28537714/
            static_text("Press any key to start", 35, WIDTH, HEIGHT, y=250, center=True, screen=screen, font="SpaceObsessed.ttf")                
            # to rotate the image
            angle += 0.5
            peng_rotated, peng_rotated_rect = rotate_image(intro_peng, angle)
            screen.blit(peng_rotated, peng_rotated_rect)

        # main menu layout
        elif window=='main_menu':
            # show image
            screen.blit(background_image15, (920, 0))
            # draw buttons
            start_button.draw(screen)
            highscore_button.draw(screen)
            tutorial_button.draw(screen)
            credits_button.draw(screen)
            settings_button.draw(screen)
            quit_button.draw(screen)
            # text in Snow Blue.ttf source: https://www.1001fonts.com/snow-blue-font.html
            static_text("Pinguin", 120, WIDTH-1250, HEIGHT-750, font="SNOW BLUE.ttf", center=False, screen=screen)

        # highscores layout
        elif window == 'highscores':
            # show image
            screen.blit(background_image2, (WIDTH/1.5, 330))
            screen.blit(background_image4, (200, 480))
            # draw button
            return_button.draw(screen)
            # text
            static_text("Highscores", 80, WIDTH, HEIGHT, y=-350, center=True, font="SNOW BLUE.ttf", screen=screen)
            # show highscores
            try : # check if scoreboard exists and how many entries there are
                if scoreboard:
                    for i in range(len(scoreboard)):
                        static_text(f"{get_pos(i)} {scoreboard[i][0]} {scoreboard[i][1]}pts", 35, WIDTH, HEIGHT-(350-(i*125)), font="SpaceObsessed.ttf", bold=True, color=get_colour(i), center=True, screen=screen)
            except (TypeError, NameError):
                pass # if scoreboard is empty, do nothing
                
        # tutorial layout   
        elif window=='tutorial':
            # show images
            screen.blit(background_image3, (150,200)) # pengiun
            screen.blit(background_image8, (700,400)) # arrow
            screen.blit(background_image9, (1075,335)) # homes - might need change
            # draw button
            return_button.draw(screen)
            next_button.draw(screen)
            # text
            static_text("Destination", 30, WIDTH+620, HEIGHT-340, screen=screen, font="SpaceObsessed.ttf",center=True, color="red1")
            static_text("Reach all 5 destinations to win!", 30, WIDTH, HEIGHT, y=-200, screen=screen, font= "SpaceObsessed.ttf",center=True)
            static_text("Tutorial", 80, WIDTH, HEIGHT, y=-350, font="SNOW BLUE.ttf", center=True, screen=screen)
                
        elif window=='tutorial2':
            # show images
            screen.blit(background_image10, (610, 360)) # polar bear
            screen.blit(background_image11, (950, 450)) # floating ice
            # draw button
            next_button.draw(screen)
            back_button.draw(screen)
            # text
            static_text("Tutorial", 80, WIDTH, HEIGHT, y=-350, center=True, font="SNOW BLUE.ttf", screen=screen)
            static_text("But be careful!", 30, WIDTH, HEIGHT, y=-200, screen=screen, font="SpaceObsessed.ttf",center=True, color='red')
            static_text("Avoid polar bears", 30, WIDTH-460, HEIGHT , y=250, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("Don't fall into the water", 30, WIDTH+400, HEIGHT, y=250, screen=screen, font= "SpaceObsessed.ttf",center=True)
        
        elif window=='tutorial3':
            # show images
            #screen.blit(background_image4, (1500, 500)) # penguin
            screen.blit(background_fish, (880, 460)) # fish
            # draw button
            back_button.draw(screen)
            next_button.draw(screen)
            # text
            static_text("Tutorial", 80, WIDTH, HEIGHT,y=-350, center=True, font="SNOW BLUE.ttf", screen=screen)
            
            static_text("How it works", 30, WIDTH, HEIGHT, y=-200, screen=screen, font="SpaceObsessed.ttf",center=True,color="yellow")
            static_text("There are 3 levels", 25, WIDTH, HEIGHT, y=-150, screen=screen, font= "SpaceObsessed.ttf",center=True)
            static_text("You have 75 seconds for the 1st level", 25, WIDTH, HEIGHT, y=-125, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("And 15 seconds less for each level that follows", 25, WIDTH, HEIGHT, y=-100, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("Each step forward gives you 10 pts", 25, WIDTH, HEIGHT, y=-75, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("Every time you reach a home you earn 100 pts", 25, WIDTH, HEIGHT, y=-50, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("Collect            to gain 25 pts", 25, WIDTH, HEIGHT, y=-25, screen=screen, font="SpaceObsessed.ttf",center=True)

            static_text("Once you complete a level", 30, WIDTH, HEIGHT, y=50, screen=screen, font="SpaceObsessed.ttf",center=True,color="yellow")
            static_text("you receive 1000 pts", 25, WIDTH, HEIGHT, y=100, screen=screen, font="SpaceObsessed.ttf",center=True)
            static_text("plus an extra 5 pts for each second remaining", 25, WIDTH, HEIGHT, y=125, screen=screen, font="SpaceObsessed.ttf",center=True)               
            static_text("and 50 pts per life remaining", 25, WIDTH, HEIGHT, y=150, screen=screen, font="SpaceObsessed.ttf",center=True)

        elif window=='tutorial4':
            # show images
            screen.blit(pygame.transform.rotate(background_image, 90), (WIDTH-500, 225)) # penguin
            screen.blit(background_image6, (580, 200)) # wasd controls
            # draw button
            back_button.draw(screen)
            # text
            static_text("Tutorial", 80, WIDTH, HEIGHT, y=-350, center=True, font="SNOW BLUE.ttf", screen=screen)
            static_text("Use the following keys to move around", 30, WIDTH, HEIGHT, y=-200, screen=screen, font="SpaceObsessed.ttf", center=True)
        
        # credits layout
        elif window=="credits" :
                # show image
                screen.blit(background_image5, (850, 520))
                # draw button
                return_button.draw(screen)
                # text
                static_text("Made by", 30, WIDTH, HEIGHT, y=-225,color='cadetblue1', center=True, screen=screen, font="SpaceObsessed.ttf")
                static_text("Benjamin Pickering", 30, WIDTH, HEIGHT-300, y=0, font="SpaceObsessed.ttf", center=True, screen=screen)
                static_text("Hannah Smith", 30, WIDTH, HEIGHT-200, y=0, font="SpaceObsessed.ttf", center=True, screen=screen)
                static_text("Joel Ligma", 30, WIDTH, HEIGHT-100, y=0, font="SpaceObsessed.ttf", center=True, screen=screen)
                static_text("Po Wing Chu", 30, WIDTH, HEIGHT+0, y=0, font="SpaceObsessed.ttf", center=True, screen=screen)
                static_text("Credits", 80, WIDTH, HEIGHT, y=-350, font="SNOW BLUE.ttf", center=True, screen=screen)
    
        else:
            if window=="settings":
                # show image 

                # draw button
                return_button.draw(screen)
                # text
                static_text("Settings", 80, WIDTH, HEIGHT, y=-350, font="SNOW BLUE.ttf", center=True, screen=screen)


        # handling idle time in main menu to return to intro screen
        if (window=="main_menu") & (not already_open):
            # get current time in miliseconds when window opened
            menu_open_time = pygame.time.get_ticks()
            already_open = True
        # get current time
        current_time = pygame.time.get_ticks()
        # after idle time of 60 seconds return to intro screen
        if already_open & (current_time - menu_open_time >= 60_000):
            already_open = False
            window = "intro"
            music_playing = False
        # update display
        pygame.display.flip()
        # Framerate
        clock.tick(framerate)

# helper functions
def returnSecond(i):
    """
    Helper function to be able to use the second element of each sublist as 
    subject for sorting the scores in descending order in save_highscores fuction.
    """
    return i[1]

# the inspiration for the followng 2 functions came from Thorsten's guess.py file (lecture 21)
def save_highscores(name, score=0) :
    """
    This function saves the top 5 player scores.
    """
    try :
        # try to load the file
        file = open("highscores.sb","rb") # read binary
        scoreboard = pickle.load(file)
        file.close()
        # if it is not there we initialize the scoreboard
    except FileNotFoundError :
        scoreboard = [] 

    if score > 0 :
        # if less than 5 players in scoreboard add player to scoreboard
        if len(scoreboard) < 5 :
            scoreboard += [ [name] + [score] ] 
        # if 5 entries and score > lowest score 
        elif len(scoreboard) == 5 and score > scoreboard[-1][-1] : # debug when it reaches 5 it stops working
        # overwrite lowest score  
            scoreboard[-1] = [name] + [score]   
        else :
            pass # dont add player to scoreboard
    
    else: 
       pass # if score == 0 dont do anything
                
    # finally sort scoreboard in descending order
    scoreboard.sort(key=returnSecond, reverse=True)
    # save the updated scoreboard
    file = open("highscores.sb","wb") # write binary
    pickle.dump(scoreboard,file)
    file.close()    

def load_highscores():  
    """
    This function returns the highscores as a list of lists.
    """
    try :
        # try to load the file and load highscores into variable scoreboard
        file = open("highscores.sb","rb") # read binary
        scoreboard = pickle.load(file)
        file.close()
        return scoreboard
    except FileNotFoundError:
        pass


def static_text(text, size, width, height, x=0, y=0, color=bg_color, font="Courier", bold=True, center=False, screen=screen) :
    """
    This function is used to create static text on the screen.
    """
    # SNOW BLUE.ttf source: https://www.1001fonts.com/snow-blue-font.html
    # SpaceObessed.ttf source: https://en.m.fontke.com/font/28537714/
    if font == "SNOW BLUE.ttf" or font == "SpaceObsessed.ttf" :
        font = pygame.freetype.Font((os.path.join(folder,font)), size)
        if center == True :
            text_surf,_ = font.render(text, color)
            text_rect = text_surf.get_rect(center=(width/2+x, height/2+y))
            screen.blit(text_surf, text_rect)
        else : 
            font.render_to(screen,(width,height), text, color)
    else: 
        font = pygame.freetype.SysFont(font, size, bold=bold)
        if center == True :
            text_surf,_ = font.render(text, color)
            text_rect = text_surf.get_rect(center=(width/2, height/2))
            screen.blit(text_surf, text_rect)
        else : 
            font.render_to(screen,(width,height), text, color)
            
def text_surface(text, size, fg_color, bg_color, font="SpaceObsessed.ttf") :
    """ 
    This function is used as a helper function to create a text surface which 
    will be drawn on the display surface.
    text = Text we want to display
    size = font size
    fg_color = color of the surface
    bg_color = font color
    """
    # using fonts from local device
    font = pygame.freetype.Font(os.path.join(folder,font), size)
    surface, _ = font.render(text = text, fgcolor = fg_color, bgcolor = bg_color)
    return surface


"""
The below code/file contains the code for the core gameplay functionality of our game, and is imported by the main menu file to be integrated with the menu of our game.
"""

"""
Global variable declaration
"""

PLAYING = True
MOVE_DIRECTION = 1
DEAD = False
SKULL_DISPLAY_TIME = 3000
LANE = int(HEIGHT/13)
TOP_BORDER = HEIGHT - (12*LANE)
MOVE_DIS = LANE
SCORE = 0
LIVES = 3
COUNTER = 0 
TIME = 0
LEVEL = 0 
level_parameters = [{'x_bear_inc': 400, 'bear_rows': 4, 'bear_speed': 2, 'x_ice_inc': 240, 'ice_rows': 6, 'ice_speed': 3, 'level_time': 80000},\
                    {'x_bear_inc': 300, 'bear_rows': 5, 'bear_speed': 3, 'x_ice_inc': 300, 'ice_rows': 5, 'ice_speed': 4, 'level_time': 65000},\
                    {'x_bear_inc': 240, 'bear_rows': 6, 'bear_speed': 5, 'x_ice_inc': 400, 'ice_rows': 4, 'ice_speed': 6, 'level_time': 50000}]
name = ""
skull_images = []

# load images, sounds and colours that are used multiple times
#folder = 'Images and sounds' 
#bg_color = pygame.Color("snow1")
#fg_color = pygame.Color("lightskyblue") # cadetblue, lightblue, deepskyblue

# splash sound found as "Splash, Jumping, A.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org”
splash = pygame.mixer.Sound(os.path.join(folder,'Falling into water credit needed.wav'))

# https://freesound.org/people/josepharaoh99/sounds/383240/#
hitwall = pygame.mixer.Sound(os.path.join(folder,'Jumping against wall.wav'))

# landhome sound found as “Power Up, Bright, A.wav" by InspectorJ (www.jshaw.co.uk) of Freesound.org"
landhome = pygame.mixer.Sound(os.path.join(folder,'Home landing.wav'))

# https://freesound.org/people/mitchanary/sounds/505131/
hitbear = pygame.mixer.Sound(os.path.join(folder,'Hitting a polar bear2.wav'))

# https://freesound.org/people/cobratronik/sounds/117136/
wind = pygame.mixer.Sound(os.path.join(folder,'cold_wind.wav'))

# https://freesound.org/people/mallement/sounds/160604/
walk = pygame.mixer.Sound(os.path.join(folder,'walk.wav'))

# https://freesound.org/people/Cabeeno%20Rossley/sounds/126422/
next_level = pygame.mixer.Sound(os.path.join(folder,'next_level3.wav'))

# https://freesound.org/people/Joao_Janz/sounds/482652/
collect = pygame.mixer.Sound(os.path.join(folder,'collect_fish2.wav'))

# https://freesound.org/people/Tuudurt/sounds/258142/
# https://freesound.org/people/elijahdanie/sounds/487436/
game_over = pygame.mixer.Sound(os.path.join(folder,'game_over2.wav'))

# https://freesound.org/people/MattLeschuck/sounds/511484/
success = pygame.mixer.Sound(os.path.join(folder,'success-bell.wav'))

# https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F54%2F87%2F2b%2F54872b269f69e713209795c6c2884ae5.png&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fwijanya6112%2Fpanguin%2F&tbnid=z2NHMp9Z1IbCjM&vet=12ahUKEwjZlq2i2cPtAhUM-BoKHbFnCSAQMyglegUIARCAAg..i&docid=d7ptc2zWDvZ56M&w=259&h=224&itg=1&q=line%20penguin&hl=en&ved=2ahUKEwjZlq2i2cPtAhUM-BoKHbFnCSAQMyglegUIARCAAg
background_image7 = pygame.image.load(os.path.join(folder,"penguin2.png")).convert_alpha() # game over screen

# https://stthomascrookes.org/stc-online-prayer-2/turquoise-square/ turquoise square
background_image13 = pygame.image.load(os.path.join(folder,'penguin_home.png')).convert_alpha()
background_image13 = pygame.transform.smoothscale(background_image13, (int(1.35*LANE), LANE))

snow = pygame.image.load(os.path.join(folder, 'snow.png')).convert_alpha()
snow = pygame.transform.scale(snow, (WIDTH, 4*LANE))

ocean = pygame.image.load(os.path.join(folder, 'ocean.png')).convert_alpha()
ocean = pygame.transform.smoothscale(ocean, (WIDTH, 4*LANE))

# set display caption
#pygame.display.set_caption('Pinguin Game')


"""
Penguin class - class for our main character in the game. Inherits from the pygame sprite class which provides access to functions useful for a sprite. 
There are four images defined, resized and saved in a list which can then be used to draw the penguin as it moves in its 4 possible directions.
A mask of the penguin is created which will be used in collision detections, as otherwise the bounding rectangle of the penguin image is used which obviously 
doesnt take into account an irregular shape so can result in abnormal collisions. 
"""

class Penguin(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image_up = pygame.image.load(os.path.join(folder,'peng_back.png')).convert_alpha()
        self.image_up = pygame.transform.smoothscale(self.image_up, (60, 60))

        self.image_left = pygame.image.load(os.path.join(folder,'peng_right.png')).convert_alpha()
        self.image_left = pygame.transform.smoothscale(self.image_left, (60, 60)) 
        self.image_left = pygame.transform.flip(self.image_left, True, False)

        self.image_right = pygame.image.load(os.path.join(folder,'peng_right.png')).convert_alpha()
        self.image_right = pygame.transform.smoothscale(self.image_right, (60, 60))

        self.image_down = pygame.image.load(os.path.join(folder,'peng_front.png')).convert_alpha()
        self.image_down = pygame.transform.smoothscale(self.image_down, (60, 60))

        self.images = [self.image_up, self.image_left, self.image_right, self.image_down]

        self.image = self.images[0]  # initialise with penguin looking forward
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.spawn_coords()
        
    # update method defines penguin actions in the game including behaviour for collisions with every object      
    def update(self):
        global MOVE_DIRECTION, PLAT_SPEED, SCORE, COUNTER
        # if penguin collides (using masks) with bear they are dead
        if pygame.sprite.spritecollideany(self, bear_group, pygame.sprite.collide_mask):
            hitbear.set_volume(0.05)
            hitbear.play()
            self.dead_behavior()
            
        plat_collisions = pygame.sprite.spritecollide(self, float_group, False, pygame.sprite.collide_mask)
        # checks if penguin is in the water area and not on an ice platform
        if (2*LANE) + TOP_BORDER - 4 < self.rect.bottom <= (6*LANE) + TOP_BORDER and not plat_collisions:
            splash.set_volume(0.05)
            splash.play()
            self.dead_behavior()

        elif plat_collisions:
            for col in plat_collisions:
                # checks that the penguin is far enough on the platform
                if self.rect.left < col.rect.left-22 or self.rect.right > col.rect.right+22:
                    splash.set_volume(0.05)
                    splash.play()
                    self.dead_behavior()
                else:
                    # move the penguin in the same direction and at the same speed as the platform it is on
                    self.rect.left += col.speed*col.direction
        
        fish_col = pygame.sprite.spritecollideany(self, fish_group)
        # check if the penguin has eaten a fish
        if fish_col:
            SCORE += 25
            fish_group.remove(fish_col)
            collect.set_volume(0.5)
            collect.play() 
        
        home_col = pygame.sprite.spritecollideany(self, home_group, pygame.sprite.collide_mask)
        # check if the penguin has reached home
        if home_col:
            # if the home is already occupied, the penguin is dead
            if home_col.occupied:
                hitwall.set_volume(0.05)
                hitwall.play()
                self.dead_behavior()
            else:
                # check that the penguin is fully in the home
                if self.rect.left > home_col.rect.left and self.rect.right < home_col.rect.right:
                    landhome.set_volume(0.1)
                    landhome.play()
                    home_col.draw_success()
                    SCORE += 100
                    COUNTER += 1
                    home_col.occupied = True
                    self.spawn_coords()
                else:
                    hitwall.set_volume(0.05)
                    hitwall.play()
                    self.dead_behavior()
        # checks if penguin is in the top border area in between the homes
        elif self.rect.top < TOP_BORDER+10: 
            hitwall.set_volume(0.1)
            hitwall.play()
            self.dead_behavior()

    # defines what happens when the penguin dies, including removing a life from the player, adding a skull to be drawn where the penguin died and resetting the penguin position
    def dead_behavior(self):
        global DEAD, LIVES, skull_images
        DEAD = True
        LIVES -= 1
        skull_images += [Skull(self.rect.x, self.rect.y)]
        self.spawn_coords()

    # resets the penguin position 
    def spawn_coords(self):
        self.image = self.images[0]
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - LANE + 1

    # function to move the penguin with the keys and change the penguin image based on its direction
    def move_keys(self, e):
        global SCORE
        if e.key == pygame.K_w or e.key == pygame.K_UP:
            self.rect.y -= MOVE_DIS
            self.image = self.images[0]
            walk.play(maxtime=500)
            SCORE += 10
        elif e.key == pygame.K_a or e.key == pygame.K_LEFT:
            self.rect.x -= MOVE_DIS
            self.image = self.images[1]
            walk.play(maxtime=500)

        elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
            self.rect.y += MOVE_DIS
            self.image = self.images[3]
            walk.play(maxtime=500)

        elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
            self.rect.x += MOVE_DIS
            self.image = self.images[2]
            walk.play(maxtime=500)

    # function to ensure the penguin doesnt leave the designated game area
    def check_borders(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > HEIGHT - LANE:
            self.rect.bottom = HEIGHT - LANE + 1

"""
class for the skull objects that are drawn when the penguin dies. Each Skull object will have a spawn time
which is used in the draw_skulls() function to only display the skull for a few seconds
"""
class Skull():
    def __init__(self, x_pos, y_pos):
        self.image = pygame.image.load(os.path.join(folder, 'penguin_skull.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80,80))#(int(0.6*LANE),int(0.6*LANE)))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.spawn_time = TIME

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

"""
Fish class for the fish that spawn on random ice blocks. Inherits from sprite class in order to make use of the spritecollide functions
"""
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(folder, 'orange_fish.png')).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (int(0.7*LANE),int(0.7*LANE)))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        """
        https://stackoverflow.com/questions/51540505/identify-individual-sprite-from-group-in-pygame
        used this to find out how to find a sprite in a group as you can't index sprite groups
        """
        self.ice_block = random.choice(float_group.sprites())
        self.rect.x = self.ice_block.rect.centerx
        self.rect.bottom = self.ice_block.rect.bottom - 10

    # function to move the fish at the same speed and in the same direction as the ice block it sits on
    def update(self):
        self.rect.left += self.ice_block.speed * self.ice_block.direction
        if self.rect.left > WIDTH or self.rect.right < 0:
            fish_group.remove(self)       

"""
SpawnObjects class contains 3 methods that are used for both the Bears and Floating classes spawns and behaviour
"""
class SpawnObjects:
    # method to add objects of the inputted class type to their sprite group
    def move(self,y_start, x_start, x_inc, row_number, group_set, class_type):
        for _ in range(row_number):
            group_set.add(class_type(x_start, y_start))
            x_start += x_inc

    # this method fills the sprite group with the complete initial spawns        
    def initial_spawn(self, y_start, x_start, x_inc, row_number, group_set, class_type):
        y = y_start
        for i in range(4):
            if i%2 == 0:
                self.move(y, x_start, x_inc, row_number, group_set, class_type)
            else:
                 self.move(y, x_start - x_inc, x_inc, row_number, group_set, class_type)
            y += LANE

    # the update methods of the Bears class and Floating class were virtually identical so this method generalises it which can then be inherited by Bears and Floating 
    def update_shared(self, group_set, class_type):
        max_left = 0
        max_right = WIDTH
        
        if self.rect.bottom == HEIGHT - (self.start_row_num*LANE)-1:
            self.speed = level_parameters[LEVEL][self.speed_id] + 3
        if self.rect.bottom == HEIGHT - ((self.start_row_num-2)*LANE)-1:
            self.speed = level_parameters[LEVEL][self.speed_id] + 5
        if self.rect.bottom == HEIGHT - ((self.start_row_num-3)*LANE)-1:
            self.speed = level_parameters[LEVEL][self.speed_id] + 1

        self.rect.left += self.speed*self.direction

        if self.rect.bottom == (HEIGHT - (self.start_row_num*LANE)-1) or self.rect.bottom == (HEIGHT - ((self.start_row_num-2)*LANE)-1):
            if self.direction > 0:
                self.direction *= -1
            if self.rect.right < 0:
                group_set.remove(self)
                for ob in group_set:
                    if ob.rect.bottom == self.rect.bottom:
                        if ob.rect.left > max_left:
                            max_left = ob.rect.left
                if max_left < WIDTH:
                    max_left = WIDTH
                group_set.add(class_type(max_left + random.randint(self.rand_min,self.rand_max), self.rect.bottom))
        else:
            if self.rect.left > WIDTH:
                group_set.remove(self)
                for ob in group_set:
                    if ob.rect.bottom == self.rect.bottom:
                        if ob.rect.left < max_right:
                            max_right = ob.rect.left
                if max_right > 0:
                    max_right = 0
                group_set.add(class_type(max_right - random.randint(self.rand_min,self.rand_max), self.rect.bottom))


class Bears(pygame.sprite.Sprite, SpawnObjects): 
    def __init__(self, x_in, y_in):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(folder,'bear.png'))
        self.image = pygame.transform.smoothscale(self.image, (int(1.3*LANE), LANE-2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = x_in
        self.rect.bottom = y_in
        self.start_row_num = 5
        self.speed_id = 'bear_speed'
        self.rand_min = 80
        self.rand_max = 320
        self.direction = MOVE_DIRECTION
        self.speed = level_parameters[LEVEL]['bear_speed']
        if self.rect.bottom == (HEIGHT - (4*LANE)-1) or self.rect.bottom == (HEIGHT - (2*LANE)-1):
            self.image = pygame.transform.flip(self.image, True, False)

    # uses the inherited method from SpawnObjects
    def update(self):
        self.update_shared(bear_group, Bears)
            
            
class Floating(pygame.sprite.Sprite, SpawnObjects):

    def __init__(self, x_in, y_in):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(folder,'floating_ice_1920x1080.png'))
        self.image = pygame.transform.smoothscale(self.image, (int(2*LANE), LANE-20))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = MOVE_DIRECTION
        self.rect.bottom = y_in
        self.rect.left = x_in
        self.start_row_num = 10
        self.speed_id = 'ice_speed'
        self.rand_min = 150
        self.rand_max = 700 
        
        self.speed = level_parameters[LEVEL]['ice_speed']

    # uses the inherited method from SpawnObjects    
    def update(self):
        self.update_shared(float_group, Floating)

        
class Home(pygame.sprite.Sprite) : 
    
    def __init__(self, x_in, y_in):
        pygame.sprite.Sprite.__init__(self)
        # https://stthomascrookes.org/stc-online-prayer-2/turquoise-square/ turquoise square
        self.image = pygame.image.load(os.path.join(folder,'turquoise-square.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(1.35*LANE), LANE))
        self.rect = self.image.get_rect()
        self.rect.centerx = x_in
        self.rect.bottom = y_in
        self.occupied = False

    # replaces the empty home image with an image of the penguin in its home        
    def draw_success(self):
        self.image = background_image13
        

# initial creation of Home objects
def create_homes():
    x = WIDTH/6
    for _ in range(5):
        home_group.add(Home(x, LANE+TOP_BORDER))
        x += WIDTH/6

# function for drawing skulls
def draw_skulls():
    global skull_images
    for skull in skull_images:
        if TIME > skull.spawn_time + SKULL_DISPLAY_TIME:
            # once the image has been displayed for 3 seconds it is removed from the skull_images list
            skull_images.pop(0)
        else:
            skull.draw()


#screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""
Creating the sprite groups. This is neccessary for all sprites used ot be added to a group, as the base pygame sprite class
only contains limited functionality, while the sprite groups contain more useful functions such as draw() 
"""
fish_group = pygame.sprite.Group()
home_group = pygame.sprite.Group()
float_group = pygame.sprite.Group()
bear_group = pygame.sprite.Group()
penguin_group = pygame.sprite.Group()
penguin = Penguin()
penguin_group.add(penguin)

# main function for the game
def main_gameplay():
    # declare global variables that are modified in this function
    global PLAYING, TIME, SCORE, LEVEL, COUNTER
    # create a clock object
    clock = pygame.time.Clock() 
    level_set = False
    pygame.mixer.music.stop()
    fish_time = 0
    wind.set_volume(0.025) # used to be 0.3 but is too loud
    wind.play(-1) # play background sound for atmosphere
    intro = True

    while PLAYING:
        # sets up the level based on the parameters contained in level_parameters
        if not level_set:
            SpawnObjects().initial_spawn((HEIGHT-(5*LANE)-1), 30, level_parameters[LEVEL]['x_bear_inc'], level_parameters[LEVEL]['bear_rows'], bear_group, Bears)
            SpawnObjects().initial_spawn((HEIGHT-(10*LANE)-1), 20, level_parameters[LEVEL]['x_ice_inc'], level_parameters[LEVEL]['ice_rows'], float_group, Floating)
            GAME_TIME = level_parameters[LEVEL]['level_time']
            create_homes()
            level_set = True
            
        # time_delta gets the time since the game started
        time_delta = clock.tick()
        TIME += time_delta 
        fish_time += time_delta
        seconds = (GAME_TIME - TIME) // 1000
        # every 1.5 seconds spawn a new fish
        if fish_time > 1500:
            fish_group.add(Fish())
            fish_time = 0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                # this will return False to the main menu code
                return False                 
            if e.type == pygame.KEYDOWN:
                penguin.move_keys(e)

        penguin.check_borders()
        
       # pygame.draw.rect(screen,pygame.Color("white"), pygame.Rect(0,HEIGHT-LANE,WIDTH,LANE))
        pygame.draw.rect(screen,pygame.Color("turquoise4"), pygame.Rect(0,0,WIDTH,TOP_BORDER))
        pygame.draw.rect(screen,pygame.Color("black"), pygame.Rect(0,TOP_BORDER,WIDTH,LANE))
        
        # safety before river
        pygame.draw.rect(screen, pygame.Color("turquoise"), pygame.Rect(0,HEIGHT-LANE*7,WIDTH,LANE))
        # starting point safety
        pygame.draw.rect(screen, pygame.Color("turquoise"), pygame.Rect(0, HEIGHT - LANE * 2, WIDTH, LANE))
        # bottom border
        pygame.draw.rect(screen, pygame.Color("turquoise4"), pygame.Rect(0, HEIGHT - LANE, WIDTH, LANE))
        # water
        screen.blit(ocean, (0, LANE+TOP_BORDER))
        # snow
        screen.blit(snow, (0, HEIGHT - LANE * 6))
        # text in game SpaceObsessed.ttf source: https://en.m.fontke.com/font/28537714/
        static_text(f"Time: {str(seconds)}", 25, WIDTH - 200, HEIGHT - LANE/1.5,screen=screen, font="SpaceObsessed.ttf")
        static_text(f"Lives: {str(LIVES)}", 25, WIDTH - 200, 10,screen=screen, font="SpaceObsessed.ttf")
        static_text(f"Score: {str(SCORE)}", 25, 60, 10,screen=screen, font="SpaceObsessed.ttf")
        static_text(f"Level {LEVEL+1}", 25, 60, HEIGHT- LANE/1.5,screen=screen, font="SpaceObsessed.ttf")

        # call the update methods and draw to screen for all sprites
        bear_group.update()
        float_group.draw(screen)
        float_group.update()
        bear_group.draw(screen)
        penguin_group.update()  
        fish_group.update()
        home_group.draw(screen)
        fish_group.draw(screen)
        penguin_group.draw(screen)

        draw_skulls()
        
        pygame.display.flip()
        # set the framerate   
        pygame.time.Clock().tick(framerate)

        # add LEVEL 1 text to start of the game
        if intro:
            # top left
            static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=10, y=-10, color="white",screen=screen, font="SpaceObsessed.ttf", center=True)
            # top right
            static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10, y=-10, color="white",screen=screen, font="SpaceObsessed.ttf", center=True)
            # bottom left 
            static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10, y=10, color="white",screen=screen, font="SpaceObsessed.ttf", center=True)
            # bottom right
            static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10 , y=-10, color="white",screen=screen, font="SpaceObsessed.ttf", center=True)
            # actual text
            static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, color="black",screen=screen, font="SpaceObsessed.ttf", center=True)

            next_level.set_volume(0.1)
            next_level.play()
            pygame.display.flip()
            pygame.time.wait(2000)
            intro = False

        if LIVES == 0:
            PLAYING = False
        if COUNTER == 5:
            # add scores for completing level and increment the level
            SCORE += 1000
            SCORE += LIVES*50
            SCORE += seconds*5
            LEVEL += 1
            # display next level screen for 2 seconds
            if LEVEL < 3:
                # top left
                static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=10, y=-10, color="white", screen=screen, font="SpaceObsessed.ttf", center=True)
                # top right
                static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10, y=-10, color="white", screen=screen, font="SpaceObsessed.ttf", center=True)
                # bottom left 
                static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10, y=10, color="white", screen=screen, font="SpaceObsessed.ttf", center=True)
                # bottom right
                static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, x=-10 , y=-10, color="white", screen=screen, font="SpaceObsessed.ttf", center=True)
                # actual text               
                static_text(f"Level {LEVEL+1}", 240, WIDTH, HEIGHT, color="black", screen=screen, font="SpaceObsessed.ttf", center=True)
                next_level.set_volume(0.1)
                next_level.play()
                pygame.display.flip()
                pygame.time.wait(2000)
            # if all levels are complete, exit the playing loop
            if LEVEL == 3: 
                PLAYING = False
            # before the next level starts reset key variables and empty the sprite groups to allow for new initial spawn positions
            COUNTER = 0
            TIME = 0
            float_group.empty()
            bear_group.empty()
            home_group.empty()
            level_set = False 
        if seconds <= 0: 
            PLAYING = False
           
    # game over screen to ask player for their name
    find_input()
    # if score > 0 save score
    if SCORE > 0 :
        save_highscores(name,SCORE)
        
    scoreboard = load_highscores()
    # reset variables for next round
    reset_variables()
    return scoreboard


def find_input():
    """
    This function acts as Game Over screen and asks the player for their name.
    The name variable will then be used in save_highscores() for saving the 
    player's name and score.
    """
    global name, screen
    # stop all sounds
    pygame.mixer.stop()
    # play game over sound
    game_over.set_volume(0.3)
    game_over.play()
    enter_pressed = False
    while not enter_pressed:
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                enter_pressed = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    enter_pressed = True   # confirm name
                    success.set_volume(0.5)
                    success.play()
                elif e.key == pygame.K_BACKSPACE:
                    if (len(name) > 0):
                        name = name[:-1] # to remove letters
            if e.type == pygame.TEXTINPUT and len(name) < 30: # set character limit
                name += e.text # add letters 
       
        screen.fill(pygame.Color(fg_color))
        static_text("Game Over", 120, WIDTH, HEIGHT, y=-200,screen=screen, font="SpaceObsessed.ttf", center=True)
        static_text(f"You scored {SCORE} points!", 30, WIDTH, HEIGHT,y=-50 ,screen=screen, font="SpaceObsessed.ttf",center=True)
        static_text("Please enter your name to save your score!",20, WIDTH,HEIGHT,screen=screen,font="SpaceObsessed.ttf",center=True)
        static_text("Name: ",20,WIDTH, HEIGHT, x=-50, y=50,screen=screen,font="SpaceObsessed.ttf",center=True) 
        static_text(f"{name}",20, WIDTH/2-15, HEIGHT/2+43, screen=screen, font="SpaceObsessed.ttf", color='yellow', center=False)        
        background7_rec = background_image7.get_rect()
        background7_rec.center = (WIDTH), (HEIGHT+200)
        screen.blit(background_image7, background7_rec)
        
        pygame.display.flip()
        
    return name
                
def reset_variables():
    global TIME, SCORE, LIVES, PLAYING, DEAD, COUNTER, skull_images, name, LEVEL
    LEVEL = 0 
    TIME = 0
    SCORE = 0
    COUNTER = 0
    LIVES = 3
    PLAYING = True
    DEAD = False
    bear_group.empty()
    float_group.empty()
    home_group.empty()
    skull_images = []
    name = ""
    

# ---------------------------------------------------------------------------#
# run game
main()
mixer.quit()  
pygame.display.quit()
pygame.quit()  
sys.exit()