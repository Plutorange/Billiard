import copy
import math
import os
import random
import sys
import sqlite3

import pygame
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


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


class Blow_up():
    def __init__(self, x, y):
        self.resolution = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.FPS = 120
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
        pygame.draw.line(self.resolution, self.color[random.randint(0, 6)], pos_1, pos_2, 1)


class Firework():
    def __init__(self):
        self.resolution = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.x = random.randint(100, 900)
        self.y = random.randint(100, 700)
        self.speed = random.uniform(3.5, 7)
        self.coord = random.uniform(10, 300)
        self.end_firework = False

    def move(self):
        self.y -= self.speed
        if self.y <= self.coord:
            self.end_firework = True

    def drawing(self):
        pos_1 = [self.x, int(self.y + 15)]
        pos_2 = [self.x, int(self.y - 15)]
        pygame.draw.line(self.resolution, (0, 0, 0), pos_1, pos_2, 4)


def game_start(winner):
    resolution = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    FPS = 120
    fireworks = [Firework()]
    blow_ups = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        f1 = pygame.font.Font(None, 80)
        text1 = f1.render('Победа за {}!'.format(winner.upper()), True,
                              (250, 255, 255))
        resolution.blit(text1, (200, 350))
        pygame.display.update()
        clock.tick(FPS)



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
            if len(p1_balls[1]) == 1 or len(p2_balls[1]) == 1:
                GameInfo.screen.fill((0, 0, 0))
                pygame.display.flip()
                pygame.time.delay(1000)
                if len(p1_balls[1]) == 1:
                    Game.winner = GameInfo.username
                else:
                    Game.winner = GameInfo.username2
                game_start(Game.winner)
                pygame.quit()
                return


class Game_Menu(object):
    def setupUi(self, game_menu):
        game_menu.setObjectName("Game_Menu")
        game_menu.resize(800, 600)
        game_menu.setMouseTracking(True)
        game_menu.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.line = QtWidgets.QFrame(game_menu)
        self.line.setGeometry(QtCore.QRect(10, 80, 780, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ball_image = QLabel(game_menu)
        self.pixmap = QPixmap('ball.png')
        self.ball_image.move(400, 175)
        self.ball_image.setPixmap(self.pixmap)
        self.l_title = QtWidgets.QLabel(game_menu)
        self.l_title.setGeometry(QtCore.QRect(233, 20, 250, 60))
        self.l_title.setStyleSheet("color: rgb(240, 240, 240);\n"
                                   "font: 40pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_play = QtWidgets.QPushButton(game_menu)
        self.btn_play.setGeometry(QtCore.QRect(230, 140, 300, 60))
        self.btn_play.setStyleSheet("color: rgb(240, 240, 240);\n"
                                    "background-color: rgb(40, 140, 90);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_play.setObjectName("btn_play")
        self.btn_stats = QtWidgets.QPushButton(game_menu)
        self.btn_stats.setGeometry(QtCore.QRect(230, 220, 300, 60))
        self.btn_stats.setStyleSheet("color: rgb(240, 240, 240);\n"
                                     "background-color: rgb(40, 140, 90);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.btn_stats.setObjectName("btn_stats")
        self.btn_unlogin = QtWidgets.QPushButton(game_menu)
        self.btn_unlogin.setGeometry(QtCore.QRect(230, 300, 300, 60))
        self.btn_unlogin.setStyleSheet("color: rgb(240, 240, 240);\n"
                                       "background-color: rgb(40, 140, 90);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "font: 14pt \"Arial\";")
        self.btn_unlogin.setObjectName("btn_login_back")
        self.btn_exit = QtWidgets.QPushButton(game_menu)
        self.btn_exit.setGeometry(QtCore.QRect(230, 380, 300, 60))
        self.btn_exit.setStyleSheet("color: rgb(240, 240, 240);\n"
                                    "background-color: rgb(40, 140, 90);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_exit.setObjectName("btn_exit")

        self.retranslateUi(game_menu)
        QtCore.QMetaObject.connectSlotsByName(game_menu)

    def retranslateUi(self, game_menu):
        _translate = QtCore.QCoreApplication.translate
        game_menu.setWindowTitle(_translate("game_menu", "Шарики"))
        self.l_title.setText(_translate("game_menu", "   Шарики"))
        self.btn_play.setText(_translate("game_menu", "Играть"))
        self.btn_stats.setText(_translate("game_menu", "Статистика"))
        self.btn_unlogin.setText(_translate("game_menu", "Выйти из аккаунтов"))
        self.btn_exit.setText(_translate("game_menu", "Закрыть"))


class Game_Buttons(QtWidgets.QWidget, Game_Menu):
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.exit_)
        self.btn_unlogin.clicked.connect(self.unlogin_)
        self.btn_stats.clicked.connect(self.stats_)
        self.btn_play.clicked.connect(self.play_)
        self.stats = Statistics()

    def play_(self):
        GameInfo.getfirst('Игрок1')
        GameInfo.getsecond('Игрок2')
        Game.pygame_start()

    def stats_(self):
        self.switch_window2.emit()
        self.stats.show_()

    def unlogin_(self):
        self.cont = Controller()
        self.cont.show_login_page()
        self.game_menu = Game_Buttons()
        self.game_menu.close()

    def exit_(self):
        self.close()


class Statistics_Ui(object):

    def setupUi(self, stats_table):
        stats_table.setObjectName("stats_table")
        stats_table.resize(800, 600)
        stats_table.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.tableWidget = QtWidgets.QTableWidget(stats_table)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 217, 200))
        self.tableWidget.setStyleSheet("background-color: rgb(189, 193, 193);\n"
                                       "color: rgb(27, 28, 28);")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.ball_image = QLabel(stats_table)
        self.pixmap = QPixmap('ball.png')
        self.ball_image.move(400, 175)
        self.ball_image.setPixmap(self.pixmap)
        self.l_title = QtWidgets.QLabel(stats_table)
        self.l_title.setGeometry(QtCore.QRect(280, 10, 250, 50))
        self.l_title.setStyleSheet("\n"
                                   "color: White;\n"
                                   "font: 26pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.l_title_1 = QtWidgets.QLabel(stats_table)
        self.l_title_1.setGeometry(QtCore.QRect(80, 50, 200, 30))
        self.l_title_1.setStyleSheet("\n"
                                     "color: White;\n"
                                     "font: 14pt \".SF NS Text\";")
        self.l_title_1.setObjectName("l_title_1")
        self.l_title_2 = QtWidgets.QLabel(stats_table)
        self.l_title_2.setGeometry(QtCore.QRect(520, 50, 200, 30))
        self.l_title_2.setStyleSheet("\n"
                                     "color: White;\n"
                                     "font: 14pt \".SF NS Text\";")
        self.l_title_2.setObjectName("l_title_2")
        self.btn_back = QtWidgets.QPushButton(stats_table)
        self.btn_back.setGeometry(QtCore.QRect(270, 360, 200, 45))
        self.btn_back.setStyleSheet("color: rgb(240, 240, 240);\n"
                                    "background-color: rgb(40, 140, 90);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(stats_table)
        QtCore.QMetaObject.connectSlotsByName(stats_table)

    def retranslateUi(self, stats_table):
        _translate = QtCore.QCoreApplication.translate
        stats_table.setWindowTitle(_translate("stats_table", "Статистика"))
        self.l_title.setText(_translate("stats_table", "Статистика"))
        self.btn_back.setText(_translate("stats_table", "Назад"))
        self.l_title_1.setText(_translate("stats_table", "Таблица лидеров"))
        self.l_title_2.setText(_translate("stats_table", "Личных побед - "))


class Statistics(QtWidgets.QWidget, Statistics_Ui):
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_back.clicked.connect(self.btn_back_handler)
        self.cont = Controller_2()

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def load_data(self):
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Имя")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str("Победы")))

    def btn_back_handler(self):
        self.cont.next_step()

    def show_(self):
        self.stats = Statistics()
        self.stats.show()


class Main_Menu(object):

    def setupUi(self, main_menu):
        main_menu.setObjectName("MainMenu")
        main_menu.resize(500, 325)
        main_menu.setMouseTracking(True)
        main_menu.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.line = QtWidgets.QFrame(main_menu)
        self.line.setGeometry(QtCore.QRect(10, 80, 590, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.l_title = QtWidgets.QLabel(main_menu)
        self.l_title.setGeometry(QtCore.QRect(170, 20, 230, 40))
        self.l_title.setStyleSheet("color: rgb(240, 240, 240);\n"
                                   "font: 25pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_ok = QtWidgets.QPushButton(main_menu)
        self.btn_ok.setGeometry(QtCore.QRect(180, 200, 160, 30))
        self.btn_ok.setStyleSheet("color: rgb(240, 240, 240);\n"
                                  "background-color: rgb(40, 140, 90);\n"
                                  "border-style:outset;\n"
                                  "border-radius:10px;\n"
                                  "font: 14pt \"Arial\";")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_newuser = QtWidgets.QPushButton(main_menu)
        self.btn_newuser.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.btn_newuser.setStyleSheet("color: rgb(240, 240, 240);\n"
                                       "background-color: rgb(40, 140, 90);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "font: 14pt \"Arial\";")
        self.btn_newuser.setObjectName("btn_newuser")
        self.txt_username = QtWidgets.QLineEdit(main_menu)
        self.txt_username.setGeometry(QtCore.QRect(130, 100, 270, 30))
        self.txt_username.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(main_menu)
        self.txt_password.setGeometry(QtCore.QRect(130, 150, 270, 30))
        self.txt_password.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_password.setObjectName("txt_password")

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Шарики"))
        self.l_title.setText(_translate("main_menu", "   Шарики"))
        self.btn_ok.setText(_translate("main_menu", "Далее"))
        self.btn_newuser.setText(_translate("main_menu", "Регистрация"))
        self.txt_username.setPlaceholderText(_translate("main_menu", "Введите имя игрока 1"))
        self.txt_password.setPlaceholderText(_translate("main_menu", "Введите пароль"))


class Ui_NewUser(object):

    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(500, 325)
        NewUser.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.l_newuser = QtWidgets.QLabel(NewUser)
        self.l_newuser.setGeometry(QtCore.QRect(150, 5, 180, 45))
        self.l_newuser.setStyleSheet("font: 23pt \".SF NS Text\";\n"
                                     "color: rgb(230, 240, 240);\n"
                                     "")
        self.l_newuser.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")
        self.line = QtWidgets.QFrame(NewUser)
        self.line.setGeometry(QtCore.QRect(10, 50, 590, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_firstname = QtWidgets.QLineEdit(NewUser)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QtCore.QRect(30, 80, 200, 35))
        self.txt_firstname.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "font: 10pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")
        self.txt_lastname = QtWidgets.QLineEdit(NewUser)
        self.txt_lastname.setGeometry(QtCore.QRect(260, 80, 200, 35))
        self.txt_lastname.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 10pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")
        self.txt_username = QtWidgets.QLineEdit(NewUser)
        self.txt_username.setGeometry(QtCore.QRect(30, 135, 200, 35))
        self.txt_username.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 10pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(260, 135, 200, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 10pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_ok = QtWidgets.QPushButton(NewUser)
        self.btn_ok.setGeometry(QtCore.QRect(180, 210, 130, 30))
        self.btn_ok.setStyleSheet("color: rgb(250, 255, 255);\n"
                                  "background-color: rgb(40, 140, 90);\n"
                                  "border-style:outset;\n"
                                  "border-radius:10px;\n"
                                  "font: 14pt \"Arial\";")
        self.btn_ok.setObjectName("btn_ok")
        self.Back = QtWidgets.QPushButton(NewUser)
        self.Back.setGeometry(QtCore.QRect(180, 255, 130, 30))
        self.Back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                "background-color: rgb(40, 140, 90);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "font: 14pt \"Arial\";")
        self.Back.setObjectName("Back")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewPlayer", "НовыйИгрок1"))
        self.l_newuser.setText(_translate("NewPlayer", "  Шарики"))
        self.txt_firstname.setPlaceholderText(_translate("NewPlayer", "Введите свое имя"))
        self.txt_lastname.setPlaceholderText(_translate("NewPlayer", "Введите свою фамилию"))
        self.txt_username.setPlaceholderText(_translate("NewPlayer", "Введите имя игрока"))
        self.lineEdit.setPlaceholderText(_translate("NewPlayer", "Введите пароль"))
        self.btn_ok.setText(_translate("NewPlayer", "Далее"))
        self.Back.setText(_translate("NewPlayer", "Назад"))


class Login(QtWidgets.QWidget, Main_Menu):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.next_step_ = Controller()
        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_ok.clicked.connect(self.btn_ok_handler)

    def get_nickname(self):
        return self.txt_username.text()

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Введите корректные логин и пароль!')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="Таких пользователей не существует!")
                return False

    def btn_ok_handler(self):
        val = self.bool_check_username()

        if (val):
            self.pop_message(text="Вы успешно авторизовались!")
            self.next_step_.next_step()

        else:
            self.pop_message("Некорректные логин и пароль!")

    def btn_newuser_handler(self):
        self.switch_window.emit()

    def check_login(self, txt_username_2):
        if txt_username_2 == self.txt_username.text():
            self.pop_message("Этот пользователь уже авторизован!")
            return False
        return True


class Newuser(QtWidgets.QWidget, Ui_NewUser):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Back.clicked.connect(self.back_handler)
        self.btn_ok.clicked.connect(self.btn_ok_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def btn_ok_handler(self):
        self.create_db_newuser()

    def back_handler(self):
        self.switch_window.emit()

    def create_db_newuser(self):
        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_username_v = self.txt_username.text()
        txt_password_v = self.lineEdit.text()
        txt_wins_v = '0'

        if (len(txt_firstname_v) <= 1
                and len(txt_lastname_v) <= 1 and
                len(txt_username_v) <= 1 and
                len(txt_password_v) <= 1):
            self.pop_message(text="Заполните все поля!")

        else:

            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    fname TEXT, 
                    lname TEXT, 
                    username TEXT, 
                    password TEXT)""")

            cursor.execute(""" INSERT INTO credentials 
                    (fname,
                    lname,
                    username, 
                    password)

                VALUES 
                (?,?,?,?)
                """, (txt_firstname_v, txt_lastname_v, txt_username_v, txt_password_v))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message(text="Вы были успешно зарегистрированы!")


class Main_Menu_2(object):

    def setupUi(self, main_menu_2):
        main_menu_2.setObjectName("MainMenu")
        main_menu_2.resize(500, 325)
        main_menu_2.setMouseTracking(True)
        main_menu_2.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.line = QtWidgets.QFrame(main_menu_2)
        self.line.setGeometry(QtCore.QRect(10, 80, 590, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.l_title = QtWidgets.QLabel(main_menu_2)
        self.l_title.setGeometry(QtCore.QRect(170, 20, 230, 40))
        self.l_title.setStyleSheet("color: rgb(240, 240, 240);\n"
                                   "font: 25pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_ok = QtWidgets.QPushButton(main_menu_2)
        self.btn_ok.setGeometry(QtCore.QRect(180, 200, 160, 30))
        self.btn_ok.setStyleSheet("color: rgb(240, 240, 240);\n"
                                  "background-color: rgb(40, 140, 90);\n"
                                  "border-style:outset;\n"
                                  "border-radius:10px;\n"
                                  "font: 14pt \"Arial\";")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_newuser = QtWidgets.QPushButton(main_menu_2)
        self.btn_newuser.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.btn_newuser.setStyleSheet("color: rgb(240, 240, 240);\n"
                                       "background-color: rgb(40, 140, 90);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "font: 14pt \"Arial\";")
        self.btn_newuser.setObjectName("btn_newuser")
        self.txt_username = QtWidgets.QLineEdit(main_menu_2)
        self.txt_username.setGeometry(QtCore.QRect(130, 100, 270, 30))
        self.txt_username.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(main_menu_2)
        self.txt_password.setGeometry(QtCore.QRect(130, 150, 270, 30))
        self.txt_password.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_password.setObjectName("txt_password")

        self.retranslateUi_2(main_menu_2)
        QtCore.QMetaObject.connectSlotsByName(main_menu_2)

    def retranslateUi_2(self, main_menu_2):
        _translate = QtCore.QCoreApplication.translate
        main_menu_2.setWindowTitle(_translate("main_menu_2", "Шарики"))
        self.l_title.setText(_translate("main_menu_2", "   Шарики"))
        self.btn_ok.setText(_translate("main_menu_2", "Далее"))
        self.btn_newuser.setText(_translate("main_menu_2", "Регистрация"))
        self.txt_username.setPlaceholderText(_translate("main_menu_2", "Введите имя игрока 2"))
        self.txt_password.setPlaceholderText(_translate("main_menu_2", "Введите пароль"))


class Ui_NewUser_2(object):

    def setupUi(self, NewUser_2):
        NewUser_2.setObjectName("NewUser")
        NewUser_2.resize(500, 325)
        NewUser_2.setStyleSheet("background-color: rgb(50, 200, 50);")
        self.l_newuser = QtWidgets.QLabel(NewUser_2)
        self.l_newuser.setGeometry(QtCore.QRect(150, 5, 180, 45))
        self.l_newuser.setStyleSheet("font: 23pt \".SF NS Text\";\n"
                                     "color: rgb(230, 240, 240);\n"
                                     "")
        self.l_newuser.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")
        self.line = QtWidgets.QFrame(NewUser_2)
        self.line.setGeometry(QtCore.QRect(10, 50, 590, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_firstname = QtWidgets.QLineEdit(NewUser_2)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QtCore.QRect(30, 80, 200, 35))
        self.txt_firstname.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "font: 10pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")
        self.txt_lastname = QtWidgets.QLineEdit(NewUser_2)
        self.txt_lastname.setGeometry(QtCore.QRect(260, 80, 200, 35))
        self.txt_lastname.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 10pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")
        self.txt_username = QtWidgets.QLineEdit(NewUser_2)
        self.txt_username.setGeometry(QtCore.QRect(30, 135, 200, 35))
        self.txt_username.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 10pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.lineEdit = QtWidgets.QLineEdit(NewUser_2)
        self.lineEdit.setGeometry(QtCore.QRect(260, 135, 200, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 10pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_ok = QtWidgets.QPushButton(NewUser_2)
        self.btn_ok.setGeometry(QtCore.QRect(180, 210, 130, 30))
        self.btn_ok.setStyleSheet("color: rgb(250, 255, 255);\n"
                                  "background-color: rgb(40, 140, 90);\n"
                                  "border-style:outset;\n"
                                  "border-radius:10px;\n"
                                  "font: 14pt \"Arial\";")
        self.btn_ok.setObjectName("btn_ok")
        self.Back = QtWidgets.QPushButton(NewUser_2)
        self.Back.setGeometry(QtCore.QRect(180, 255, 130, 30))
        self.Back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                "background-color: rgb(40, 140, 90);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "font: 14pt \"Arial\";")
        self.Back.setObjectName("Back")

        self.retranslateUi(NewUser_2)
        QtCore.QMetaObject.connectSlotsByName(NewUser_2)

    def retranslateUi(self, NewUser_2):
        _translate = QtCore.QCoreApplication.translate
        NewUser_2.setWindowTitle(_translate("NewPlayer2", "НовыйИгрок2"))
        self.l_newuser.setText(_translate("NewPlayer2", "  Шарики"))
        self.txt_firstname.setPlaceholderText(_translate("NewPlayer2", "Введите свое имя"))
        self.txt_lastname.setPlaceholderText(_translate("NewPlayer2", "Введите свою фамилию"))
        self.txt_username.setPlaceholderText(_translate("NewPlayer2", "Введите имя игрока"))
        self.lineEdit.setPlaceholderText(_translate("NewPlayer2", "Введите пароль"))
        self.btn_ok.setText(_translate("NewPlayer2", "Далее"))
        self.Back.setText(_translate("NewPlayer2", "Назад"))


class Login_2(QtWidgets.QWidget, Main_Menu_2):
    switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.next_step_ = Controller_2()
        self.login = Login()
        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_ok.clicked.connect(self.btn_ok_handler)

    def get_nickname(self):
        return self.txt_username.text()

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Введите корректные логин и пароль!')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="Таких пользователей не существует!")
                return False

    def btn_ok_handler(self):
        val = self.bool_check_username()

        if (val) and self.login.check_login(self.txt_username.text()):
            self.pop_message(text="Вы успешно авторизовались!")
            self.next_step_.next_step()

        else:
            self.pop_message("Некорректные логин и пароль!")

    def btn_newuser_handler(self):
        self.switch_window1.emit()


class Newuser_2(QtWidgets.QWidget, Ui_NewUser_2):
    switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Back.clicked.connect(self.back_handler)
        self.btn_ok.clicked.connect(self.btn_ok_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def btn_ok_handler(self):
        self.create_db_newuser()

    def back_handler(self):
        self.switch_window1.emit()

    def create_db_newuser(self):

        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_username_v = self.txt_username.text()
        txt_password_v = self.lineEdit.text()

        if (len(txt_firstname_v) <= 1
                and len(txt_lastname_v) <= 1 and
                len(txt_username_v) <= 1 and
                len(txt_password_v) <= 1):
            self.pop_message(text="Заполните все поля!")

        else:

            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    fname TEXT, 
                    lname TEXT, 
                    username TEXT, 
                    password TEXT)""")

            cursor.execute(""" INSERT INTO credentials 
                    (fname,
                    lname,
                    username, 
                    password)

                VALUES 
                (?,?,?,?)
                """, (txt_firstname_v, txt_lastname_v, txt_username_v, txt_password_v))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message(text="Вы были успешно зарегистрированы!")


class Controller:

    def __init__(self):
        pass

    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_newuser_page)
        self.login.show()

    def show_newuser_page(self):
        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()

    def next_step(self):
        self.login_2 = Controller_2()
        self.login_2.show_login_page()


class Controller_2:

    def __init__(self):
        pass

    def show_login_page(self):
        self.login = Login_2()
        self.login.switch_window1.connect(self.show_newuser_page)
        self.login.show()

    def show_newuser_page(self):
        self.newuser = Newuser_2()
        self.newuser.switch_window1.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()

    def next_step(self):
        self.game_buttons = Game_Buttons()
        self.game_buttons.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
