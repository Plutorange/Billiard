import copy
import os

import pygame
from demo_main_menu import main

pygame.init()


def load_image(name, color_key=None):
    fullname = os.path.join('bil', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, num):
        super().__init__(all_sprites)
        ball_image = load_image(f'ball{num + 1}.png')
        ball_image = pygame.transform.scale(ball_image, (30, 30))
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.num = num
        if num == 0:
            self.rect.x = 175
            self.rect.y = 325
        elif num == 1:
            self.rect.x = 175
            self.rect.y = 355
        elif num == 2:
            self.rect.x = 175
            self.rect.y = 385
        elif num == 3:
            self.rect.x = 175
            self.rect.y = 415
        elif num == 4:
            self.rect.x = 175
            self.rect.y = 445
        elif num == 5:
            self.rect.x = 205
            self.rect.y = 340
        elif num == 6:
            self.rect.x = 205
            self.rect.y = 370
        elif num == 7:
            self.rect.x = 205
            self.rect.y = 400
        elif num == 8:
            self.rect.x = 205
            self.rect.y = 430
        elif num == 9:
            self.rect.x = 235
            self.rect.y = 355
        elif num == 10:
            self.rect.x = 235
            self.rect.y = 385
        elif num == 11:
            self.rect.x = 235
            self.rect.y = 415
        elif num == 12:
            self.rect.x = 265
            self.rect.y = 370
        elif num == 13:
            self.rect.x = 265
            self.rect.y = 400
        elif num == 14:
            self.rect.x = 295
            self.rect.y = 385
        else:
            self.rect.x = 485
            self.rect.y = 385

        self.speed_x = (width // 2 - pos[0]) / 50
        self.speed_y = (height // 2 - pos[1]) / 50
        self.dist_x = copy.deepcopy(self.rect.x)
        self.dist_y = copy.deepcopy(self.rect.y)

    def change_route(self, other):
        if self.speed_x != 0 and self.speed_y != 0:
            other.speed_x += abs(self.rect.x - other.rect.x) * (
                    self.speed_x // abs(self.speed_x)) / 10
            other.speed_y += abs(self.rect.y - other.rect.y) * (
                    self.speed_y // abs(self.speed_y)) / 10
            d1 = (self.speed_x ** 2 + self.speed_y ** 2) ** 0.5
            d2 = (other.speed_x ** 2 + other.speed_y ** 2) ** 0.5
            if d2 != 0:
                dif = d1 / d2
                other.speed_x = other.speed_x * dif / 2
                other.speed_y = other.speed_y * dif / 2
            self.rect = self.rect.move((self.dist_x - self.speed_x - self.rect.x),
                                       (self.dist_y - self.speed_y - self.rect.y))
            if self.speed_y > 0:
                if self.speed_x > other.speed_x:
                    self.speed_x = -other.speed_y
                    self.speed_y = other.speed_x
                elif other.speed_x == 0:
                    self.speed_y = -other.speed_y
                    self.speed_x = other.speed_x
                else:
                    self.speed_x = other.speed_y
                    self.speed_y = -other.speed_x
            elif self.speed_y < 0:
                if self.speed_x < other.speed_x:
                    self.speed_x = -other.speed_y
                    self.speed_y = other.speed_x
                elif other.speed_x == 0:
                    self.speed_y = -other.speed_y
                    self.speed_x = other.speed_x
                else:
                    self.speed_x = other.speed_y
                    self.speed_y = -other.speed_x
            else:
                self.speed_y = other.speed_y
                self.speed_x = -other.speed_x
        self.dist_x += self.speed_x
        self.dist_y += self.speed_y

    def update(self):
        if self.dist_x + self.speed_x + 60 > 950:
            self.speed_x *= -1
        if self.dist_y + self.speed_y + 60 > 640:
            self.speed_y *= -1
        if self.rect.x + self.speed_x - 30 < 50:
            self.speed_x *= -1
        if self.rect.y + self.speed_y - 30 < 160:
            self.speed_y *= -1
        for i in all_sprites:
            self.rect = self.rect.move(self.dist_x + self.speed_x - self.rect.x,
                                       self.dist_y + self.speed_y - self.rect.y)
            if self != i and pygame.sprite.collide_mask(self, i):
                self.change_route(i)
            else:
                self.rect = self.rect.move((self.dist_x - self.speed_x - self.rect.x),
                                           (self.dist_y - self.speed_y - self.rect.y))
        self.dist_x += self.speed_x
        self.dist_y += self.speed_y
        self.rect = self.rect.move(self.dist_x - self.rect.x, self.dist_y - self.rect.y)
        if abs(self.speed_x) < 0.01 and abs(self.speed_y) < 0.01:
            self.speed_x = 0
            self.speed_y = 0
        # for i in all_sprites:
        #     if pygame.sprite.collide_mask(self, i) and self != i:
        #         self.dist_x -= self.speed_x
        #         self.dist_y -= self.speed_y
        #         self.rect = self.rect.move(self.dist_x - self.rect.x, self.dist_y - self.rect.y)
        self.speed_x /= 1.005
        self.speed_y /= 1.005
        for i in corners:
            if pygame.sprite.collide_mask(self, i):
                all_sprites.remove(self)
                if self != sp_ball:
                    out_sprites.add(self)
                i.score += 1
                break


class Corner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(corners)
        self.image = corner_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        if len(corners) == 1:
            self.rect.x = 50
            self.rect.y = 160
        elif len(corners) == 2:
            self.rect.x = 50
            self.rect.y = 595
        elif len(corners) == 3:
            self.rect.x = 905
            self.rect.y = 160
        elif len(corners) == 4:
            self.rect.x = 905
            self.rect.y = 595
        elif len(corners) == 5:
            self.rect.x = 485
            self.rect.y = 160
        elif len(corners) == 6:
            self.rect.x = 485
            self.rect.y = 595


pygame.display.set_caption('Шарики')
size = width, height = 1000, 800
board_width, board_height = 900, 480
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
out_sprites = pygame.sprite.Group()
corners = pygame.sprite.Group()
corner_image = load_image('corner.png')
corner_image = pygame.transform.scale(corner_image, (45, 45))
for i in range(6):
    Corner()
for i in range(15):
    Ball((500, 400), i)
sp_ball = Ball((500, 400), 15)
f1 = pygame.font.Font(None, 40)
text1 = f1.render('Игрок 1', True,
                  (36, 9, 53))
text2 = f1.render('Игрок 2', True,
                  (36, 9, 53))
p1_balls = [None, []]
p2_balls = [None, []]
turn = 0
running = True
screen.fill((40, 120, 80))
drawing = False
clock = pygame.time.Clock()


def game():
    global sp_ball
    global turn
    global p1_balls
    global p2_balls
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] < 950 and 160 <= event.pos[1] < 640:
                    if sp_ball not in all_sprites:
                        sp_ball = Ball(event.pos, 15)
                    else:
                        if sp_ball.speed_x == 0 == sp_ball.speed_y:
                            sp_ball.speed_x = (sp_ball.rect.x + 15 - event.pos[0]) / 50
                            sp_ball.speed_y = (sp_ball.rect.y + 15 - event.pos[1]) / 50
        if len(out_sprites) == 1:
            a = [i for i in out_sprites][0]
            if a.num < 7:
                if turn == 0:
                    p1_balls = ['solid', [a.num]]
                else:
                    p2_balls = ['solid', [a.num]]
            elif a.num > 8:
                if turn == 0:
                    p1_balls = ['stripe', [a.num]]
                else:
                    p2_balls = ['stripe', [a.num]]
        elif len(out_sprites) > 1:
            a = [i for i in out_sprites][-1]
            if p1_balls[0] == 'solid' and a.num < 7:
                p1_balls[1].append(a.num)
            else:
                p2_balls[1].append(a.num)
        if sp_ball.speed_x == 0 == sp_ball.speed_y:
            turn = (turn + 1) % 2
        screen.fill((40, 120, 80))
        pygame.draw.rect(screen, (50, 200, 50), (80, 190, 840, 420))
        pygame.draw.rect(screen, (150, 75, 0), (50, 160, 900, 30))
        pygame.draw.rect(screen, (150, 75, 0), (50, 160, 30, 480))
        pygame.draw.rect(screen, (150, 75, 0), (50, 610, 900, 30))
        pygame.draw.rect(screen, (150, 75, 0), (920, 160, 30, 480))
        pygame.draw.circle(screen, (0, 0, 0), (500, 400), 10)
        pygame.draw.rect(screen, (220, 220, 220), (30, 30, 300, 100), border_radius=100)
        pygame.draw.rect(screen, (0, 0, 0), (30, 30, 300, 100), 5, border_radius=100)
        pygame.draw.rect(screen, (220, 220, 220), (670, 30, 300, 100), border_radius=100)
        pygame.draw.rect(screen, (0, 0, 0), (670, 30, 300, 100), 5, border_radius=100)
        screen.blit(text1, (70, 40))
        screen.blit(text2, (710, 40))
        corners.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(150)
        if sum(map(lambda x: x.score, corners)) == 16:
            screen.fill((0, 0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)
            break

    pygame.quit()


game()
