import sys

import pygame

import settings
import mixins


class Game(mixins.EventMixin):

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if self.is_pressed_esc(event):
                    pygame.quit()
                    sys.exit()
            pressed_buttons = pygame.key.get_pressed()
            self.asterix_go(pressed_buttons=pressed_buttons)

            self.screen.blit(self.landscape, settings.TOP_OF_SCREEN)
            self.screen.blit(self.asterix_surf, self.asterix_rect)

            pygame.display.update()
            self.clock.tick(settings.FTP)


if __name__ == '__main__':
    game = Game()
    game.run_game()
