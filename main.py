import game
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def show_scoreboard():
    global menu
    menu.clear()
    with open('scoreboard.txt', 'r') as file:
        text = file.read()
        menu.add.label(text, max_char=-1, font_size = 20)

def start_the_game():
    myGame = game.game()
    myGame.play()


menu = pygame_menu.Menu('Welcome', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Scoreboard', show_scoreboard)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)