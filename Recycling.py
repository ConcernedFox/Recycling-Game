import pgzrun
from random import randint
FONT_Opion = ( 255,255,255 )
WIDTH = 800
HEIGHT = 600
Center_X = WIDTH / 2
Center_Y = HEIGHT / 2
Center = (Center_X,Center_Y)
Final_Level = 6
Start_Speed = 10
ITEMS = ["Sprite_1","Sprite_2","Sprite_3","Sprite_4"]
Game_Over = False
Game_Complete = False
Current_Level = 1
Items = []
ANIMATION = []
def draw():
    global Items, Current_Level, Game_Over, Game_Complete
    Screen.clear()
    Screen.blit("BG_4",(0,0))

    if Game_Over:
        display_message("Game_Over")
    elif Game_Complete:
        display_message("You Win")
    else:
        for item in Items:
            item.draw()
def update():
    global Items
    if len(Items) == 0:
        Items = create_items(Current_Level)