import copy
import os

import pygame


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


class GameInfo:
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 1000, 800
    board_width, board_height = 900, 480
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    out_sprites = pygame.sprite.Group()
    corners = pygame.sprite.Group()
    corner_image = load_image('corner.png', -1)
    corner_image = pygame.transform.scale(corner_image, (45, 45))
    username = ''
    username2 = ''
    winner = ''

    @staticmethod
    def getfirst(name):
        GameInfo.username = name

    @staticmethod
    def getsecond(name):
        GameInfo.username2 = name


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, num, sprlist):
        super().__init__(sprlist)
        GameInfo.all_sprites.add(self)
        width, height = GameInfo.width, GameInfo.height
        ball_image = load_image(f'ball{num + 1}.png', -1)
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
        for i in GameInfo.all_sprites:
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
        for i in GameInfo.all_sprites:
            if pygame.sprite.collide_mask(self, i) and self != i:
                self.dist_x -= self.speed_x
                self.dist_y -= self.speed_y
                self.rect = self.rect.move(self.dist_x - self.rect.x, self.dist_y - self.rect.y)
        self.speed_x /= 1.005
        self.speed_y /= 1.005
        for i in GameInfo.corners:
            if pygame.sprite.collide_mask(self, i):
                GameInfo.all_sprites.remove(self)
                if self != Game.sp_ball:
                    GameInfo.out_sprites.add(self)
                break


class Corner(pygame.sprite.Sprite):
    def __init__(self, sprlist):
        super().__init__(sprlist)
        GameInfo.corners.add(self)
        self.image = GameInfo.corner_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        if len(GameInfo.corners) == 1:
            self.rect.x = 55
            self.rect.y = 165
        elif len(GameInfo.corners) == 2:
            self.rect.x = 55
            self.rect.y = 590
        elif len(GameInfo.corners) == 3:
            self.rect.x = 900
            self.rect.y = 165
        elif len(GameInfo.corners) == 4:
            self.rect.x = 900
            self.rect.y = 590
        elif len(GameInfo.corners) == 5:
            self.rect.x = 485
            self.rect.y = 160
        elif len(GameInfo.corners) == 6:
            self.rect.x = 485
            self.rect.y = 595


class Game:
    sp_ball = Ball((500, 400), 15, GameInfo.all_sprites)

    @staticmethod
    def pygame_start():
        for i in range(6):
            Corner(GameInfo.corners)
        for i in range(15):
            Ball((500, 400), i, GameInfo.all_sprites)
        scream_image = pygame.transform.scale(load_image('scream.jpeg'), (1000, 800))
        bait_image = pygame.transform.scale(load_image('butto.jpeg'), (25, 25))
        turn = 0
        text1 = pygame.font.Font(None, 40).render(GameInfo.username, True, (36, 9, 53))
        text2 = pygame.font.Font(None, 40).render(GameInfo.username2, True, (36, 9, 53))
        p1_balls = [None, []]
        p2_balls = [None, []]
        clock = pygame.time.Clock()
        scr = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= event.pos[0] < 950 and 160 <= event.pos[1] < 640:
                        if Game.sp_ball not in GameInfo.all_sprites:
                            Game.sp_ball = Ball(event.pos, 15, GameInfo.all_sprites)
                        else:
                            if Game.sp_ball.speed_x == 0 == Game.sp_ball.speed_y:
                                Game.sp_ball.speed_x = (Game.sp_ball.rect.x + 15 - event.pos[0]) / 50
                                Game.sp_ball.speed_y = (Game.sp_ball.rect.y + 15 - event.pos[1]) / 50
                    elif 975 <= event.pos[0] and event.pos[1] <= 25:
                        scr = True
            if len(GameInfo.out_sprites) == 1:
                a = [i for i in GameInfo.out_sprites][0]
                if a.num < 7:
                    if turn == 0:
                        p1_balls = ['solid', [a.num]]
                        p2_balls[0] = 'stripe'
                    else:
                        p2_balls = ['solid', [a.num]]
                        p1_balls[0] = 'stripe'
                elif a.num > 8:
                    if turn == 0:
                        p1_balls = ['stripe', [a.num]]
                        p2_balls[0] = 'solid'
                    else:
                        p2_balls = ['stripe', [a.num]]
                        p1_balls[0] = 'solid'
            elif len(GameInfo.out_sprites) > 1:
                a = [i for i in GameInfo.out_sprites][-1]
                if (p1_balls[0] == 'solid' and a.num < 7) or (p1_balls[0] == 'stripe' and a.num > 8):
                    p1_balls[1].append(a.num)
                else:
                    p2_balls[1].append(a.num)
            if Game.sp_ball.speed_x == 0 or 0 == Game.sp_ball.speed_y:
                turn = (turn + 1) % 2
            GameInfo.screen.fill((40, 120, 80))
            pygame.draw.rect(GameInfo.screen, (50, 200, 50), (80, 190, 840, 420))
            pygame.draw.rect(GameInfo.screen, (150, 75, 0), (50, 160, 900, 30))
            pygame.draw.rect(GameInfo.screen, (150, 75, 0), (50, 160, 30, 480))
            pygame.draw.rect(GameInfo.screen, (150, 75, 0), (50, 610, 900, 30))
            pygame.draw.rect(GameInfo.screen, (150, 75, 0), (920, 160, 30, 480))
            pygame.draw.circle(GameInfo.screen, (0, 0, 0), (500, 400), 10)
            pygame.draw.rect(GameInfo.screen, (220, 220, 220), (30, 30, 300, 100), border_radius=100)
            pygame.draw.rect(GameInfo.screen, (0, 0, 0), (30, 30, 300, 100), 5, border_radius=100)
            pygame.draw.rect(GameInfo.screen, (220, 220, 220), (670, 30, 300, 100),
                             border_radius=100)
            pygame.draw.rect(GameInfo.screen, (0, 0, 0), (670, 30, 300, 100), 5, border_radius=100)
            GameInfo.screen.blit(text1, (70, 40))
            GameInfo.screen.blit(text2, (710, 40))
            GameInfo.screen.blit(bait_image, (975, 0))
            if scr:
                GameInfo.screen.blit(scream_image, (0, 0))
                pygame.display.flip()
                pygame.time.delay(5000)
                scr = False
            else:
                GameInfo.corners.draw(GameInfo.screen)
                GameInfo.all_sprites.draw(GameInfo.screen)
                GameInfo.all_sprites.update()
                pygame.display.flip()
                clock.tick(150)
            if len(p1_balls[1]) == 8 or len(p2_balls[1]) == 8:
                GameInfo.screen.fill((0, 0, 0))
                pygame.display.flip()
                pygame.time.delay(1000)
                if len(p1_balls[1]) == 8:
                    Game.winner = GameInfo.username
                else:
                    Game.winner = GameInfo.username2
                pygame.quit()
                return
