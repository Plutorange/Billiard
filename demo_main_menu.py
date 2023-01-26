import sys
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


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
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.exit_)
        self.btn_unlogin.clicked.connect(self.unlogin_)
        self.btn_stats.clicked.connect(self.stats_)
        self.btn_play.clicked.connect(self.play_)


    def play_(self):
        pass

    def stats_(self):
        pass

    def unlogin_(self):
        self.cont = Controller()
        self.cont.show_login_page()
        self.game_menu = Game_Buttons()
        self.game_menu.close()

    def exit_(self):
        self.close()



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
    controller1 = Controller()
    controller1.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
