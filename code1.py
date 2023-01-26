import pygame
import random
import math

pygame.init()
resolution = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
FPS = 120


class Blow_up():
    def __init__(self, x, y):
        self.color = [(218, 165, 32), (255, 36, 0), (255, 116, 23), (255, 191, 0), (255, 0, 0), (255, 219, 139),
                      (205, 164, 52)]
        self.x = x
        self.y = y
        self.angle = random.uniform(-60, 360)
        self.value = random.uniform(.3, 4)
        self.speed_x = self.value * math.cos(math.radians(self.angle))
        self.speed_y = -1 * self.value * math.sin(math.radians(self.angle))
        self.timing = 0
        self.end_firework = False

    def get_angle(self):
        return math.atan2(-self.speed_y, self.speed_x)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.timing += 1
        if self.timing >= 100:
            self.end_firework = True

    def drawing(self):
        angle = self.get_angle()
        length = 1
        delta_x = length * math.cos(angle)
        delta_y = length * math.sin(angle)
        pos_1 = [int(self.x + delta_y), int(self.y - delta_x)]
        pos_2 = [int(self.x - delta_y), int(self.y + delta_x)]
        pygame.draw.line(resolution, self.color[random.randint(0, 6)], pos_1, pos_2, 1)


class Firework():
    def __init__(self):
        self.x = random.randint(100, 900)
        self.y = random.randint(100, 700)
        self.speed = random.uniform(3.5, 7)
        self.coord = random.uniform(10, 300)
        self.end_firework = False

    def text_draw(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Победа \n за \n nickname", True, (100, 255, 100))
        text_x = 1000 // 2 - text.get_width() // 2
        text_y = 800 // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        resolution.blit(text, (text_x, text_y))
        pygame.draw.rect(resolution, (0, 255, 0), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)

    def move(self):
        self.y -= self.speed
        if self.y <= self.coord:
            self.end_firework = True

    def drawing(self):
        pos_1 = [self.x, int(self.y + 15)]
        pos_2 = [self.x, int(self.y - 15)]
        pygame.draw.line(resolution, (0, 0, 0), pos_1, pos_2, 4)


def game():
    fireworks = [Firework()]
    blow_ups = []
    text = Firework()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        text.text_draw()
        if random.uniform(0, 1) <= 1 / 60:
            fireworks.append(Firework())
        resolution.fill((0, 0, 0))
        for firework in fireworks:
            firework.move()
            firework.drawing()
            if firework.end_firework:
                blow_ups += [Blow_up(firework.x, firework.y) for i in range(800)]
                fireworks.remove(firework)
        for blow_up in blow_ups:
            blow_up.move()
            blow_up.drawing()
            if blow_up.end_firework:
                blow_ups.remove(blow_up)
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()
