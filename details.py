import random
from typing import Any

import pygame

import settings


romans = pygame.sprite.Group()


class Roman(pygame.sprite.Sprite):
    """Класс Римлянина."""

    def __init__(self):
        self.WIGHT_OF_SCREEN = pygame.display.get_surface().get_width()
        self.HEIGHT_OF_SCREEN = pygame.display.get_surface().get_height()

        self.PLACES_OF_BIRTH = [
            (
                settings.ROMAIN_WIGHT_INDENT,
                settings.ROMAIN_HEIGHT_INDENT
            ),
            (
                settings.ROMAIN_WIGHT_INDENT,
                self.HEIGHT_OF_SCREEN - settings.ROMAIN_HEIGHT_INDENT
            ),
            (
                self.HEIGHT_OF_SCREEN - settings.ROMAIN_HEIGHT_INDENT,
                settings.ROMAIN_WIGHT_INDENT
            ),
            (
                self.WIGHT_OF_SCREEN - settings.ROMAIN_HEIGHT_INDENT,
                settings.ROMAIN_WIGHT_INDENT
            )
        ]

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(settings.PATH_TO_ROMANS),
            settings.ROMANS_SIZE
        ).convert_alpha()
        self.image.set_colorkey(settings.BLACK_COLOR)
        self.rect = self.image.get_rect(
            center=random.choice(self.PLACES_OF_BIRTH)
        )
        self.vectors = [
            self.go_up,
            self.go_down,
            self.go_right,
            self.go_left,
        ]
        self.go_vectors = []

    def go_left(self):
        self.rect.x -= settings.ROMANS_SPEED
        if self.rect.x <= 0:
            self.rect.x = 0

    def go_right(self):
        self.rect.x += settings.ROMANS_SPEED
        if self.rect.x >= self.WIGHT_OF_SCREEN - self.rect.width:
            self.rect.x = self.WIGHT_OF_SCREEN - self.rect.width

    def go_up(self):
        self.rect.y -= settings.ROMANS_SPEED
        if self.rect.y <= 0:
            self.rect.y = 0

    def go_down(self):
        self.rect.y += settings.ROMANS_SPEED
        if self.rect.y >= self.HEIGHT_OF_SCREEN - self.rect.height:
            self.rect.y = self.HEIGHT_OF_SCREEN - self.rect.height

    def add_go_vectors(self, vector):
        self.go_vectors = [vector] * settings.ROMANS_SMOOTHNESS

    def go(self):
        if not self.go_vectors:
            vector = random.choice(self.vectors)
            self.add_go_vectors(vector)
        self.go_vectors.pop()()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.go()
        if self.rect.colliderect(args[0]):
            settings.START_SCORE += 1
            self.kill()


class MagicFlask(pygame.sprite.Sprite):
    """Класс фляжки с волшебным напитком."""
    pass