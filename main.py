import sys

import pygame

import settings
import mixins


class Game(mixins.RomansMixin):

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if self.is_pressed_esc(event):
                    pygame.quit()
                    sys.exit()

            self.asterix_go(pressed_buttons=pygame.key.get_pressed())
            self.romans_go()

            self.screen.blit(self.landscape, settings.TOP_OF_SCREEN)
            self.romans.draw(self.screen)

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
