"""
  Классы миксины для разного функционала
  основного класса игры Game.
"""
import sys

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

        # загружаем игровую музыку
        self.hit_music = pygame.mixer.Sound(settings.PATH_TO_HIT_MUSIC)
        self.flask_music = pygame.mixer.Sound(settings.PATH_TO_FLASK_MUSIC)
        self.crash_music = pygame.mixer.Sound(settings.PATH_TO_CRASH_MUSIC)
        self.win_music = pygame.mixer.Sound(settings.PATH_TO_WINNING_MUSIC)
        self.romans_fly_music = pygame.mixer.Sound(
            settings.PATH_TO_ROMANS_FLY_MUSIC
        )

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
            settings.get_size_of_character(
                img_surf,
                settings.ASTERIX_SIZE_DIVIDER
            )
        )
        self.asterix_rect = self.asterix_surf.get_rect(
            center=settings.ASTERIX_POSITION
        )
        self.asterix_is_right = True

        # оторажение суперсилы
        self.super_power_surf = pygame.image.load(
            settings.PATH_TO_SUPER_POWER
        )
        self.super_power_rect = self.super_power_surf.get_rect()

        # Отображение жизней Астерикса
        self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)
        self.mini_font = pygame.font.SysFont(
            settings.FONT,
            settings.MINI_FONT_SIZE
        )

        # Отображение каски
        helmet_img_surf = pygame.image.load(
            settings.PATH_TO_HELMET
        ).convert_alpha()
        self.helmet_surf = pygame.transform.scale(
            helmet_img_surf,
            settings.get_size_of_character(
                helmet_img_surf,
                settings.HELMET_DIVIDER
            )
        )

        # Настройки Римлян
        self.romans = pygame.sprite.Group()
        self.time_out = settings.ROMANS_TIME_OUT

        # настройки цезаря
        self.cesar = pygame.sprite.Group()

        # Настройки фляжки
        self.flasks = pygame.sprite.Group()


class EventMixin(InitGame):
    """Класс для обработки событий в игре."""

    @staticmethod
    def is_pressed_esc(event) -> bool:
        """Нажата ли кнопка выхода - Esc."""

        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    @staticmethod
    def is_pressed_enter(event) -> bool:
        """Нажата ли кнопка продолжения игры - Enter."""

        return event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN

    @property
    def bottom_border(self):
        """Нижняя граница."""

        return self.screen.get_height() - self.asterix_rect.height

    @property
    def right_border(self):
        """Правая граница."""

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
        if self.asterix_rect.x > self.right_border:
            self.asterix_rect.x = self.right_border

    def asterix_go_down(self) -> None:
        """Астерикс движется вниз."""

        self.asterix_rect.y += self.asterix_speed
        if self.asterix_rect.y > self.bottom_border:
            self.asterix_rect.y = self.bottom_border

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
        """Движение Римлянина."""

        self.time_out -= settings.ROMANS_TIME_OUT_ENDS_SPEED
        if settings.START_SCORE < settings.ROMANS_ARMY_SIZE:
            if self.time_out <= 0 and \
                    len(self.romans) < settings.ROMANS_MAX_AMOUNT:
                self.time_out = settings.ROMANS_TIME_OUT
                self.add_roman_to_romans()

        self.romans.update(
            self.asterix_rect,
            self.hit_music,
            self.crash_music,
            self.romans_fly_music
        )


class FlaskMixin(RomansMixin):
    """Класс обработки волшебного напитка."""

    def add_flask_to_flasks(self):
        """Добавляем волшебный напиток в игру."""

        flask = details.MagicFlask()
        self.flasks.add(flask)

    def flask_go(self):
        """Появление волшебного напитка."""

        if settings.ASTERIX_HAS_SUPER_POWER:
            settings.ASTERIX_SUPER_POWER_TIME_OUT -= \
                settings.ASTERIX_SUPER_POWER_ENDS_SPEED
        if settings.ASTERIX_SUPER_POWER_TIME_OUT <= 0:
            settings.ASTERIX_HAS_SUPER_POWER = False

        if not settings.ASTERIX_HAS_SUPER_POWER and not self.flasks:
            self.add_flask_to_flasks()
        self.flasks.update(self.asterix_rect, self.flask_music)


class GameOverMenuMixin(FlaskMixin):
    """
    Класс с меню "Конец Игры".
    """

    # Сохраняем изменяемые переменные, чтобы перезапустить игру
    ASTERIX_LIVES = settings.ASTERIX_LIVES
    ASTERIX_HAS_SUPER_POWER = settings.ASTERIX_HAS_SUPER_POWER
    ASTERIX_SUPER_POWER_TIME_OUT = settings.ASTERIX_SUPER_POWER_TIME_OUT
    START_SCORE = settings.START_SCORE

    def game_reset(self):
        """Возвращает настройки игры к первоначальным."""

        settings.ASTERIX_LIVES = self.ASTERIX_LIVES
        settings.ASTERIX_HAS_SUPER_POWER = self.ASTERIX_HAS_SUPER_POWER
        settings.ASTERIX_SUPER_POWER_TIME_OUT = \
            self.ASTERIX_SUPER_POWER_TIME_OUT
        settings.START_SCORE = self.START_SCORE
        settings.GAMER_ALREADY_WIN = False

        for roman in self.romans:
            roman.kill()

    def prepare_asterix_with_idea_fix(self):
        """
        Готовим картинку Астерикса с пёсиком Идеафиксом
        для заставки меню.
        """

        self.asterix_and_idea_fix_surf = pygame.image.load(
            settings.PATH_TO_ASTERIX_AND_IDEA_FIX
        ).convert_alpha()
        asterix_center = self.asterix_and_idea_fix_surf.get_height() // 2
        self.asterix_and_idea_fix_rect = \
            self.asterix_and_idea_fix_surf.get_rect(
                center=(
                    self.asterix_and_idea_fix_surf.get_width() // 2,
                    self.HEIGHT_OF_SCREEN - asterix_center
                )
            )

    def prepare_game_over_text(self, text):
        """Готовим текст результата игры."""

        self.game_over_text = self.font.render(
            text,
            True,
            settings.WHITE_COLOR,
            None
        )
        self.game_over_rect = self.game_over_text.get_rect(
            center=(
                self.WIGHT_OF_SCREEN // 2,
                self.HEIGHT_OF_SCREEN // 2,
            )
        )

    def prepare_help_text(self):
        """Готовим вспомагательный текст для меню."""

        self.help_text = self.mini_font.render(
            settings.HELP_TEXT,
            True,
            settings.WHITE_COLOR,
            None
        )
        self.help_text_rect = self.help_text.get_rect(
            center=(
                self.WIGHT_OF_SCREEN // 2,
                self.help_text.get_height() // 2
            )
        )

    def game_over_menu(self, text):
        """Меню конца игры."""

        in_menu = True

        self.prepare_asterix_with_idea_fix()
        self.prepare_game_over_text(text)
        self.prepare_help_text()

        if text == settings.WINING_GAME_TEXT:
            self.win_music.play()

        while in_menu:
            for event in pygame.event.get():
                if self.is_pressed_esc(event):
                    pygame.quit()
                    sys.exit()
                if self.is_pressed_enter(event):
                    self.game_reset()
                    in_menu = False

            # закрашиваем экран
            self.screen.fill(settings.BLACK_COLOR)

            # обавляем Астерикса и диафикса на экран
            self.screen.blit(
                self.asterix_and_idea_fix_surf,
                self.asterix_and_idea_fix_rect
            )

            # отображаем результат игры
            self.screen.blit(self.game_over_text, self.game_over_rect)

            # отображаем вспомагательный текст
            self.screen.blit(self.help_text, self.help_text_rect)

            pygame.display.update()
            self.clock.tick(settings.FTP)


class CesarMixin(GameOverMenuMixin):
    """Класс действий Цезаря."""

    @property
    def gamer_win_romans(self) -> bool:
        """Победил ли игрок всех римлян."""
        return settings.START_SCORE >= settings.ROMANS_ARMY_SIZE

    @property
    def asterix_is_dead(self) -> bool:
        """Умер ли астерикс."""
        return settings.ASTERIX_LIVES <= 0

    def cesar_go(self):
        """Движение Цезаря."""

        if self.gamer_win_romans and not self.cesar:
            self.cesar.add(details.Cesar())
        self.cesar.update(self.asterix_rect)


class BlitMixin(CesarMixin):
    """
    Класс отображения на экране предметов и героев.
    """

    def blit_landscape_to_screen(self):
        """Рисуем игровой фон."""

        self.screen.blit(self.landscape, settings.TOP_OF_SCREEN)

    def blit_helmet_to_screen(self):
        """Рисуем шлем на экран."""

        center_of_helmet = self.helmet_surf.get_width() // 2
        self.helmet_rect = self.helmet_surf.get_rect(
            center=(
                self.lives_surf.get_width() + center_of_helmet,
                self.helmet_surf.get_height() // 2
            )
        )
        self.screen.blit(self.helmet_surf, self.helmet_rect)

    def blit_lives_number_to_screen(self):
        """Рисуем колличество жизней на экран."""

        self.lives_surf = self.font.render(
            str(int(settings.ASTERIX_LIVES)),
            True,
            settings.WHITE_COLOR,
            None
        )
        self.lives_rect = self.lives_surf.get_rect(
            center=(
                self.lives_surf.get_width() // 2,
                self.lives_surf.get_height() // 2
            )
        )
        self.screen.blit(self.lives_surf, self.lives_rect)

    def blit_super_power_to_screen(self):
        """Рисуем значёк суперсилы на экран."""

        if settings.ASTERIX_HAS_SUPER_POWER:
            self.super_power_rect = self.super_power_surf.get_rect(
                center=(
                    self.WIGHT_OF_SCREEN - self.super_power_surf.get_width(),
                    self.HEIGHT_OF_SCREEN - self.super_power_surf.get_height()
                )
            )
            self.screen.blit(self.super_power_surf, self.super_power_rect)

    def blit_romans_and_cesar_to_screen(self):
        """Рисуем Римлян и Цезаря на экран."""

        self.romans_go()
        self.romans.draw(self.screen)
        self.cesar_go()
        self.cesar.draw(self.screen)

    def blit_magic_flask_to_screen(self):
        """Рисуем волшебный напиток на экран."""

        self.flask_go()
        self.flasks.draw(self.screen)

    def blit_asterix_to_screen(self):
        """Рисуем Астерикса на экран."""

        self.asterix_go(pressed_buttons=pygame.key.get_pressed())
        if self.asterix_is_right:
            self.screen.blit(self.asterix_surf, self.asterix_rect)
        else:
            self.screen.blit(
                pygame.transform.flip(
                    self.asterix_surf,
                    settings.ASTERIX_FLIP_X,
                    settings.ASTERIX_FLIP_Y
                ),
                self.asterix_rect
            )
