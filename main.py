"""
  Основной файл, сдесь находится главный класс
  Game, для запуска игры необходимо создать
  экземпляр этого класса и вызвать метод
  run_game().
"""
import sys

import pygame

import settings
import mixins


class Game(mixins.BlitMixin):
    """
    Основной класс Игры.
    """

    def run_game(self):
        """Запуск Игры."""

        while True:
            for event in pygame.event.get():
                if self.is_pressed_esc(event):
                    pygame.quit()
                    sys.exit()

            if self.asterix_is_dead:
                self.game_over_menu(text=settings.LOSE_GAME_TEXT)
            if settings.GAMER_ALREADY_WIN:
                self.game_over_menu(text=settings.WINING_GAME_TEXT)

            self.blit_landscape_to_screen()
            self.blit_lives_number_to_screen()
            self.blit_helmet_to_screen()
            self.blit_super_power_to_screen()
            self.blit_romans_and_cesar_to_screen()
            self.blit_magic_flask_to_screen()
            self.blit_asterix_to_screen()

            pygame.display.update()
            self.clock.tick(settings.FTP)


if __name__ == '__main__':
    game = Game()
    game.run_game()
