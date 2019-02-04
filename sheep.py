import pygame as pg

class Sheep:
    def __init__(self):
        self.jumpCount = 10
        self.isJumping = 0
        self.x = 20
        self.y = 300-40
        self.image = pg.image.load("./res/sheep_right.png")
        self.rect = pg.Rect(self.x, self.y, 40 , 30)
        self.x_direction = 1

    def move(self, score):
        self.rect.move_ip(5*self.x_direction,0)
        #print(self.rect.x)
        if self.rect.x >= 760:
            self.x_direction = -1
        if self.rect.x <= 0:
            self.x_direction = 1


        if (pg.key.get_pressed()[pg.K_SPACE]):
            self.isJumping = 1

        if self.isJumping == 1:
            image = self.image
            if (score / 4) % 2 == 0:
                self.image = pg.image.load("./res/sheep_jump.png")
            else:
                self.image = pg.image.load("./res/sheep_jump_left.png")

            if self.jumpCount >= -10:
                sign = 1
                if self.jumpCount < 0:
                    sign = -1
                self.rect.y -= pow(self.jumpCount, 2)*0.5*sign
                self.jumpCount -= 1

            else:
                #bug fixing
                self.rect.y = 300-40

                if (score/4)%2 == 0:
                    self.image = pg.image.load("./res/sheep_right.png")
                else:
                    self.image = pg.image.load("./res/sheep_left.png")

                self.isJumping = 0
                self.jumpCount = 10


