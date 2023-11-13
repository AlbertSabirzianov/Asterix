"""
Классы миксины для разного функционала
основного класса игры Game.
"""
import pygame

import details
import settings


class InitGame:
    """Класс создания игрового пространства."""

    def __init__(self):
        # запускаем музыкальное сопровождение
        pygame.mixer.init()
        pygame.mixer.music.load(settings.PATH_TO_GAME_MUSIC)
        pygame.mixer.music.play(settings.INFINITY_LOOP)

        self.hit_music = pygame.mixer.Sound(settings.PATH_TO_HIT_MUSIC)
        self.flask_music = pygame.mixer.Sound(settings.PATH_TO_FLASK_MUSIC)

        pygame.init()
        self.clock = pygame.time.Clock()

        # Настраеваем экран
        self.screen = pygame.display.set_mode(
            settings.TOP_OF_SCREEN,
            pygame.FULLSCREEN
        )
        self.landscape = pygame.transform.scale(
            pygame.image.load(settings.PATH_TO_LANDSCAPE),
            self.screen.get_size()
        )

        # размеры экрана
        self.WIGHT_OF_SCREEN = pygame.display.get_surface().get_width()
        self.HEIGHT_OF_SCREEN = pygame.display.get_surface().get_height()

        img_surf = pygame.image.load(settings.PATH_TO_ASTERIX).convert_alpha()

        # Настройки астерикса
        self.asterix_surf = pygame.transform.scale(
            img_surf,
            settings.get_size_of_character(img_surf, settings.ASTERIX_SIZE_DIVIDER)
        )
        self.asterix_rect = self.asterix_surf.get_rect(center=settings.ASTERIX_POSITION)
        self.asterix_is_right = True

        # оторажение суперсилы
        self.super_power_surf = pygame.image.load('images/superpower_new.png')
        self.super_power_rect = self.super_power_surf.get_rect()

        # Отображение жизней Астерикса
        self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)

        # Отображение каски
        casca_img_surf = pygame.image.load('images/casca.png').convert_alpha()
        self.casca_surf = pygame.transform.scale(
            casca_img_surf,
            settings.get_size_of_character(casca_img_surf, settings.CASCCA_DIVIDER)
        )

        # Настройки Римлян
        self.romans = pygame.sprite.Group()
        self.time_out = settings.ROMANS_TIME_OUT

        # Настройки фляжки
        self.flasks = pygame.sprite.Group()


class EventMixin(InitGame):
    """Класс для обработки событий в игре."""

    @staticmethod
    def is_pressed_esc(event) -> bool:
        """Нажата ли кнопка выхода - Esc."""
        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    @property
    def bottom_height(self):
        return self.screen.get_height() - self.asterix_rect.height

    @property
    def right_wight(self):
        return self.screen.get_width() - self.asterix_rect.width

    @property
    def asterix_speed(self):
        """Вычисляет скорость Астерикса в зависимости от суперсилы."""
        speed_data = {
            False: settings.ASTERIX_SPEED,
            True: settings.ASTERIX_MAGIC_SPEED
        }
        return speed_data[settings.ASTERIX_HAS_SUPER_POWER]

    def asterix_go_left(self) -> None:
        """Астерикс движется на лево."""
        self.asterix_is_right = False

        self.asterix_rect.x -= self.asterix_speed
        if self.asterix_rect.x < 0:
            self.asterix_rect.x = 0

    def asterix_go_right(self) -> None:
        """Астерикс движется на право."""
        self.asterix_is_right = True

        self.asterix_rect.x += self.asterix_speed
        if self.asterix_rect.x > self.right_wight:
            self.asterix_rect.x = self.right_wight

    def asterix_go_down(self) -> None:
        """Астерикс движется вниз."""

        self.asterix_rect.y += self.asterix_speed
        if self.asterix_rect.y > self.bottom_height:
            self.asterix_rect.y = self.bottom_height

    def asterix_go_up(self) -> None:
        """Астерикс движется вверх."""

        self.asterix_rect.y -= self.asterix_speed
        if self.asterix_rect.y < 0:
            self.asterix_rect.y = 0

    def asterix_go(self, pressed_buttons) -> None:
        """Движение астерикса."""

        if pressed_buttons[pygame.K_LEFT]:
            self.asterix_go_left()
        if pressed_buttons[pygame.K_RIGHT]:
            self.asterix_go_right()
        if pressed_buttons[pygame.K_DOWN]:
            self.asterix_go_down()
        if pressed_buttons[pygame.K_UP]:
            self.asterix_go_up()


class RomansMixin(EventMixin):
    """Класс для обработки Римлян."""

    def add_roman_to_romans(self):
        """Добавляем Римлянина в игру."""
        roman = details.Roman()
        self.romans.add(roman)

    def romans_go(self):
        self.time_out -= settings.ROMANS_TIME_OUT_ENDS_SPEED
        if self.time_out <= 0 and len(self.romans) < settings.ROMANS_MAX_AMOUNT:
            self.time_out = settings.ROMANS_TIME_OUT
            self.add_roman_to_romans()

        self.romans.update(self.asterix_rect, self.hit_music)


class FlaskMixin(RomansMixin):

    def add_flask_to_flasks(self):
        flask = details.MagicFlask()
        self.flasks.add(flask)

    def flask_go(self):

        if settings.ASTERIX_HAS_SUPER_POWER:
            settings.ASTERIX_SUPER_POWER_TIME_OUT -= settings.ASTERIX_SUPER_POWER_ENDS_SPEED
        if settings.ASTERIX_SUPER_POWER_TIME_OUT <= 0:
            settings.ASTERIX_HAS_SUPER_POWER = False

        if not settings.ASTERIX_HAS_SUPER_POWER and not self.flasks:
            self.add_flask_to_flasks()
        self.flasks.update(self.asterix_rect, self.flask_music)


