"""
Классы миксины для разного функционала
основного класса игры Game.
"""
import pygame
import settings


class InitGame:
    """Класс создания игрового пространства."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            settings.TOP_OF_SCREEN,
            pygame.FULLSCREEN
        )
        self.landscape = pygame.transform.scale(
            pygame.image.load(settings.PATH_TO_LANDSCAPE),
            self.screen.get_size()
        )
        self.screen.blit(self.landscape, settings.TOP_OF_SCREEN)

        img_surf = pygame.image.load(settings.PATH_TO_ASTERIX).convert()
        img_surf.set_colorkey(settings.WHITE_COLOR)

        self.asterix_surf = pygame.transform.scale(
            img_surf,
            settings.ASTERIX_SIZE
        )
        self.asterix_rect = self.asterix_surf.get_rect(center=settings.ASTERIX_POSITION)
        self.screen.blit(self.asterix_surf, self.asterix_rect)


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

    def asterix_go_left(self) -> None:
        """Астерикс движется на лево."""

        self.asterix_rect.x -= settings.ASTERIX_SPEED
        if self.asterix_rect.x < 0:
            self.asterix_rect.x = 0

    def asterix_go_right(self) -> None:
        """Астерикс движется на право."""

        self.asterix_rect.x += settings.ASTERIX_SPEED
        if self.asterix_rect.x > self.right_wight:
            self.asterix_rect.x = self.right_wight

    def asterix_go_down(self) -> None:
        """Астерикс движется вниз."""

        self.asterix_rect.y += settings.ASTERIX_SPEED
        if self.asterix_rect.y > self.bottom_height:
            self.asterix_rect.y = self.bottom_height

    def asterix_go_up(self) -> None:
        """Астерикс движется вверх."""

        self.asterix_rect.y -= settings.ASTERIX_SPEED
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
