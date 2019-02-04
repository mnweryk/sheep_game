import pygame as pg
import random

class Fence:
    def __init__(self, id):
        self.id = id

        self.x = ((self.id)*150+100)+random.randint(0,150)
        #doesn't matter becaouse of clamp_ip_function
        self.y = 3000

        high = 60+random.randint(0,90)
        self.rect = pg.Rect(self.x, self.y, 10, high)
        self.image = pg.transform.scale(pg.image.load("./res/fence.png"), (10, high))

    def set_fences(self):
        rand_position = random.randint(0, 150)
        self.rect.x = ((self.id) * 150 + 100) + rand_position
        rand_high = 60+random.randint(0,90)
        self.rect = pg.Rect(self.rect.x, self.y, 10, rand_high)
        self.image = pg.transform.scale(pg.image.load("./res/fence.png"), (10, rand_high))

    def set_high(self):
        high = 60+random.randint(0,90)
        return high

    def set_image(self):
        self.image = pg.transform.scale(pg.image.load("./res/fence.png"), (10, self.set_high()))
