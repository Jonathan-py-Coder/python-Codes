import pgzrun

WIDTH=1170
HIGHT=800
CENTER_X=WIDTH // 2
CENTER_Y=HIGHT // 2
CENTER=(CENTER_X, CENTER_Y)

FINAL_LEVEL=6
START_SPEED=10
ITEMS=["paper_bag", "plastic_bottle", "battery", "chips", "plastic_bag"]

game_over=False
game_complete=False
current_level=1
items=[]
animations=[]


def draw():
    global items,current_level,game_complete,game_over
    screen.clear()
    screen.blit("bg_recycle",(0,0))
    if game_over:
        display_message("GAME_OVER","Try again")
    elif game_complete:
        display_message("You won...","Well done")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == "0"
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animation_items(new_items)
    return new_items

def get_option_to_crate(number_of_extra_items):
    items_to_crate=["paperbags"]
    for i in range(0, number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_crate.append(random_option)
    return items_to_crate
