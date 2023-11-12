import sys

import pygame

import settings
import mixins


class Game(mixins.FlaskMixin):

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if self.is_pressed_esc(event):
                    pygame.quit()
                    sys.exit()

            # Накладываем фон
            self.screen.blit(self.landscape, settings.TOP_OF_SCREEN)

            # Отображение счёта
            self.letter_rect = self.letter_surf.get_rect(center=settings.LETTER_POSITION)
            self.screen.blit(self.letter_surf, self.letter_rect)
            self.text_score = self.font.render(
                str(settings.START_SCORE),
                True,
                settings.WHITE_COLOR,
                settings.BLACK_COLOR
            )
            self.text_score.set_colorkey(settings.BLACK_COLOR)
            self.score_rect = self.text_score.get_rect(center=settings.SCORE_POSITION)
            self.screen.blit(self.text_score, self.score_rect)

            # отображение суперсилы
            if settings.ASTERIX_HAS_SUPER_POWER:
                self.super_power_rect = self.super_power_surf.get_rect(
                    center=(
                        self.WIGHT_OF_SCREEN - self.super_power_surf.get_width(),
                        self.HEIGHT_OF_SCREEN - self.super_power_surf.get_height()
                    )
                )
                self.screen.blit(self.super_power_surf, self.super_power_rect)

            # движение Астерикса и Римлян
            self.asterix_go(pressed_buttons=pygame.key.get_pressed())
            self.romans_go()
            self.romans.draw(self.screen)

            # появление волшебной фляжки
            self.flask_go()
            self.flasks.draw(self.screen)

            # отрисовка Астерикса
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

            pygame.display.update()
            self.clock.tick(settings.FTP)


if __name__ == '__main__':
    game = Game()
    game.run_game()
