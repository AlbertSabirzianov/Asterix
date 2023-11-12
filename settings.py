from typing import Tuple

FTP = 60

TOP_OF_SCREEN = (0, 0)

ASTERIX_POSITION = (300, 300)
ASTERIX_SIZE_DIVIDER = 5
ASTERIX_SPEED = 10
ASTERIX_FLIP_X = 1
ASTERIX_FLIP_Y = 0
ASTERIX_HAS_SUPER_POWER = False # меняется во время инры
ASTERIX_SUPER_POWER_TIME_OUT = 100 # меняется во время игры
ASTERIX_SUPER_POWER_ENDS_SPEED = 1

FLASK_POSITION = (500, 500)

ROMANS_SPEED = 5
ROMANS_TIME_OUT = 100
ROMANS_TIME_OUT_ENDS_SPEED = 1
ROMANS_MAX_AMOUNT = 5
ROMANS_SIZE_DIVIDER = 7
ROMANS_SMOOTHNESS = 20
ROMANS_INDENT = 10 # отступ от края вместе появления римлянина

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

INFINITY_LOOP = -1

PATH_TO_LANDSCAPE = 'images/landscape.png'
PATH_TO_ASTERIX = 'images/Asterix_new_3.png'
PATH_TO_GAME_MUSIC = 'music/game_music.mp3'
PATH_TO_ROMANS = 'images/w-romans.png'
PATH_TO_LETTER = 'images/letter.jpg'
PATH_TO_FLASK = 'images/magic-flask.png'

LETTER_POSITION = (50, 50)
LETTER_SIZE = (80, 80)

SCORE_POSITION = (50, 55)
SCORE_FONT_SIZE = 80
SCORE_INCREASE = 1
START_SCORE = 0 # меняется во время игры


def get_size_of_character(img_srf, divider) -> Tuple[int, int]:
    """Возвращает размер персонажа."""

    rect = img_srf.get_rect()
    width = rect.width // divider
    height = rect.height // divider
    return width, height
