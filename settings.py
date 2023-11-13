"""
  Настройки игры "Астерикс против Цезаря"
  переменные помеченные знаком <- меняются во
  время игры и должны быть перезаписаны для новой игры.
"""
from typing import Tuple

FTP = 60

TOP_OF_SCREEN = (0, 0)

# настройки астерикса
ASTERIX_POSITION = (300, 300)
ASTERIX_LIVES = 100 # <-
ASTERIX_LIVES_ENDS_SPEED = 0.2
ASTERIX_SIZE_DIVIDER = 5
ASTERIX_SPEED = 10
ASTERIX_MAGIC_SPEED = 20
ASTERIX_FLIP_X = 1
ASTERIX_FLIP_Y = 0
ASTERIX_HAS_SUPER_POWER = False # <-
ASTERIX_SUPER_POWER_TIME_OUT = 100 # <-
ASTERIX_SUPER_POWER_ENDS_SPEED = 1

# настройки римлян
ROMANS_SPEED = 5
ROMANS_FLY_SPEED = 40
ROMANS_TIME_OUT = 100
ROMANS_TIME_OUT_ENDS_SPEED = 1
ROMANS_MAX_AMOUNT = 5
ROMANS_ARMY_SIZE = 10
ROMANS_SIZE_DIVIDER = 7
ROMANS_SMOOTHNESS = 20
ROMANS_INDENT = 10
ROMANS_CRUSH_MUSIC_TIME_OUT = 10
ROMANS_CRUSH_MUSIC_ENDS_SPEED = 1

# цвета
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

INFINITY_LOOP = -1

WINING_GAME_TEXT = 'YOU_WIN'
LOSE_GAME_TEXT = 'GAME_OVER'

GAMER_ALREADY_WIN = False # <-

# пути до картинок
PATH_TO_LANDSCAPE = 'images/landscape.png'
PATH_TO_ASTERIX = 'images/Asterix_new_3.png'
PATH_TO_ROMANS = 'images/w-romans.png'
PATH_TO_FLASK = 'images/magic-flask.png'
PATH_TO_ASTERIX_AND_IDEA_FIX = 'images/asterix_and_ideafix.png'
PATH_TO_CESAR = 'images/cesar.png'

# пути до музыки
PATH_TO_GAME_MUSIC = 'music/game_music.mp3'
PATH_TO_HIT_MUSIC = 'music/hit.wav'
PATH_TO_FLASK_MUSIC = 'music/flask.wav'
PATH_TO_CRASH_MUSIC = 'music/mech-zvonkiy-yarkiy.wav'
PATH_TO_WINNING_MUSIC = 'music/fanfar.wav'
PATH_TO_ROMANS_FLY_MUSIC = 'music/romans_fly.mp3'

CASCCA_DIVIDER = 15

CESAR_SIZE_DIVIDER = 5

# настройки шрифта
FONT_SIZE = 80
MINI_FONT_SIZE = 40
FONT = 'script'

SCORE_UP_SPEED = 1
START_SCORE = 0 # <-

HELP_TEXT = 'press enter to continue, ' \
            'press esc to exit'


def get_size_of_character(img_srf, divider) -> Tuple[int, int]:
    """Возвращает размер персонажа."""

    rect = img_srf.get_rect()
    width = rect.width // divider
    height = rect.height // divider
    return width, height
