import random

import pygame

import settings

romans = pygame.sprite.Group()


class Roman(pygame.sprite.Sprite):
    """Класс Римлянина."""

    def __init__(self):
        self.WIGHT_OF_SCREEN = pygame.display.get_surface().get_width()
        self.HEIGHT_OF_SCREEN = pygame.display.get_surface().get_height()

        self.PLACES_OF_BIRTH = (
            random.randint(settings.ROMANS_INDENT, self.WIGHT_OF_SCREEN),
            random.randint(settings.ROMANS_INDENT, self.HEIGHT_OF_SCREEN)
        )

        pygame.sprite.Sprite.__init__(self)
        img_surf = pygame.image.load(settings.PATH_TO_ROMANS)
        self.image = pygame.transform.scale(
            img_surf,
            settings.get_size_of_character(img_surf, settings.ROMANS_SIZE_DIVIDER)
        ).convert_alpha()
        self.rect = self.image.get_rect(
            center=self.PLACES_OF_BIRTH
        )
        self.vectors = [
            self.go_up,
            self.go_down,
            self.go_right,
            self.go_left,
        ]
        self.go_vectors = []
        self.crush_music_time_out = 0

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

    def update(self, asterix_rect, hit_music, crush_music) -> None:
        self.go()
        if self.rect.colliderect(asterix_rect):
            if settings.ASTERIX_HAS_SUPER_POWER:
                settings.START_SCORE += settings.SCORE_INCREASE
                hit_music.play()
                self.kill()
            else:
                if self.crush_music_time_out <= 0:
                    crush_music.play()
                    self.crush_music_time_out = settings.ROMANS_CRUSH_MUSIC_TIME_OUT
                settings.ASTERIX_LIVES -= settings.ASTERIX_LIVES_ENDS_SPEED
                self.crush_music_time_out -= settings.ROMANS_CRUSH_MUSIC_ENDS_SPEED


class MagicFlask(pygame.sprite.Sprite):
    """Класс фляжки с волшебным напитком."""
    SUPER_POWER_TIME_OUT = settings.ASTERIX_SUPER_POWER_TIME_OUT

    def __init__(self):
        self.WIGHT_OF_SCREEN = pygame.display.get_surface().get_width()
        self.HEIGHT_OF_SCREEN = pygame.display.get_surface().get_height()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(settings.PATH_TO_FLASK)
        self.rect = self.image.get_rect(
            center=(
                random.randint(self.image.get_width(), self.WIGHT_OF_SCREEN - self.image.get_width()),
                random.randint(self.image.get_height(), self.HEIGHT_OF_SCREEN - self.image.get_height())
            )
        )

    def update(self, asterix_rect, flask_music) -> None:
        if self.rect.colliderect(asterix_rect):
            settings.ASTERIX_HAS_SUPER_POWER = True
            settings.ASTERIX_SUPER_POWER_TIME_OUT = self.SUPER_POWER_TIME_OUT
            flask_music.play()
            self.kill()
