import sys

import pygame

import settings


class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(settings.FTP)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
