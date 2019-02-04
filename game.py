import pygame as pg
import sys
from sheep import Sheep
from fence import Fence
pg.init()

window = pg.display.set_mode((800, 400))
border = pg.Rect(0,0,800,300)
pg.display.set_caption("sheep game")
clock = pg.time.Clock()




def game_over(score):

    while True:
        czcionka = pg.font.SysFont("comicsans", 20)
        gameover_text = "Game over your score: " + str(score/4) + "         To play again press p"
        text_render = czcionka.render(gameover_text, 1, (250, 250, 250))

        for event in pg.event.get():
            if pg.key.get_pressed()[pg.K_p]:
                new_game()

            if event.type == pg.QUIT:
                sys.exit(0)
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                sys.exit(0)

        window.fill((0, 0, 200))
        window.blit(text_render, (200, 200))
        pg.display.flip()


def check_fences_distance(fences):
    ok = 1
    for i in range(0,3):
        if (fences[i+1].rect.x-fences[i].rect.x)>20 and (fences[i+1].rect.x-fences[i].rect.x)<80:
            print("not ok")
            ok = -1
    return ok

def harder(score):
    delay = 50
    return int(delay-(score/4)*2)

def new_game():
    score = 0
    delay = 50
    sheep = Sheep()
    fences = []

    for i in range(0, 4):
        fences.append(Fence(i))



    while True:
        pg.time.delay(delay)
        window.fill((0,200,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                sys.exit(0)

        sheep.move(score)

        for fence in fences:
            fence.rect.clamp_ip(border)
            if sheep.rect.colliderect(fence.rect):
                game_over(score)
            if sheep.rect.x >= 760 or sheep.rect.x <= 0:
                if sheep.rect.x >=760:
                    sheep.image = pg.image.load("./res/sheep_left.png")
                else:
                    sheep.image = pg.image.load("./res/sheep_right.png")
                fence.set_fences()
                score += 1
                delay = harder(score)

        ok = check_fences_distance(fences)
        while(ok == -1):
            print("changing fences")
            for fence in fences:
                fence.set_fences()
            ok = check_fences_distance(fences)

        pg.draw.rect(window, (0,0,255), border)
        window.blit(sheep.image, (sheep.rect.x, sheep.rect.y))
        for fence in fences:
            window.blit(fence.image, (fence.rect.x, fence.rect.y))
        pg.display.flip()

new_game()
