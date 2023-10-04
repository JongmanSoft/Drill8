import random

from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(1,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self, a):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint (1,10)
        if (a == 0):
            self.h = 20
            self.image = load_image('ball21x21.png')
        else :
            self.h = 40
            self.image = load_image('ball41x41.png')
    def update(self):
        if (self.y -(self.h/2) >50): self.y -= int(self.speed) *2
        else: self.y = 50 +(self.h/2)
    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world
    global balls
    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    world += team
    balls = [Ball(random.randint(0,1))for i in range(20)]
    print (len(balls))
    world += balls


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
running = True
reset_world()

# game main loop code

while(running):
    handle_events()
    update_world() #게임로직
    render_world() #드로우 게임월드
    delay(0.05)

# finalization code

close_canvas()
