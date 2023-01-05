import copy
import os

import pygame

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
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 275
        self.rect.y = 135
        self.speed_x = (width // 2 - pos[0]) / 50
        self.speed_y = (height // 2 - pos[1]) / 50
        self.dist_x = copy.deepcopy(self.rect.x)
        self.dist_y = copy.deepcopy(self.rect.y)

    def change_route(self, other):
        if self.speed_x != 0 and self.speed_y != 0:
            other.speed_x = abs(self.rect.x - other.rect.x) * (
                    self.speed_x // abs(self.speed_x)) / 10
            other.speed_y = abs(self.rect.y - other.rect.y) * (
                    self.speed_y // abs(self.speed_y)) / 10
            self.rect = self.rect.move(-(self.dist_x + self.speed_x - self.rect.x),
                                       -(self.dist_y + self.speed_y - self.rect.y))
            self.speed_x = 0
            self.speed_y = 0

    def update(self):
        if self.rect.x + self.speed_x + 20 > width:
            self.speed_x *= -1
        if self.rect.y + self.speed_y + 20 > height:
            self.speed_y *= -1
        if self.rect.x + self.speed_x < 0:
            self.speed_x *= -1
        if self.rect.y + self.speed_y < 0:
            self.speed_y *= -1
        for i in all_sprites:
            self.rect = self.rect.move(self.dist_x + self.speed_x - self.rect.x,
                                       self.dist_y + self.speed_y - self.rect.y)
            if self != i and pygame.sprite.collide_mask(self, i):
                self.change_route(i)
            else:
                self.rect = self.rect.move(-(self.dist_x + self.speed_x - self.rect.x),
                                           -(self.dist_y + self.speed_y - self.rect.y))
        self.dist_x += self.speed_x
        self.dist_y += self.speed_y
        self.rect = self.rect.move(self.dist_x - self.rect.x, self.dist_y - self.rect.y)
        if abs(self.speed_x) < 0.01 and abs(self.speed_y) < 0.01:
            self.speed_x = 0
            self.speed_y = 0
        self.speed_x /= 1.005
        self.speed_y /= 1.005
        for i in corners:
            if pygame.sprite.collide_mask(self, i):
                all_sprites.remove(self)
                i.score += 1
                break


class Corner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(corners)
        self.image = corner_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        if len(corners) == 0:
            self.rect.x = 0
            self.rect.y = 0
        elif len(corners) == 1:
            self.rect.x = 0
            self.rect.y = 290
        elif len(corners) == 2:
            self.rect.x = 570
            self.rect.y = 0
        elif len(corners) == 3:
            self.rect.x = 570
            self.rect.y = 290
        elif len(corners) == 4:
            self.rect.x = 285
            self.rect.y = 0
        elif len(corners) == 5:
            self.rect.x = 285
            self.rect.y = 290


pygame.display.set_caption('Шарики')
size = width, height = 600, 320
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
corners = pygame.sprite.Group()
ball_image = load_image('8.png')
ball_image = pygame.transform.scale(ball_image, (20, 20))
corner_image = load_image('corner.png')
corner_image = pygame.transform.scale(corner_image, (30, 30))
Corner()
Corner()
Corner()
Corner()
Corner()
Corner()

running = True
screen.fill((50, 200, 50))
pygame.draw.rect(screen, (200, 0, 0), (0, 0, 30, 30))
drawing = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Ball(event.pos)
    screen.fill((50, 200, 50))
    corners.draw(screen)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(150)
    if sum(map(lambda x: x.score, corners)) >= 16:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)
        break
pygame.quit()
