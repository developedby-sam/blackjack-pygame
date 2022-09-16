import sys
import pygame
from pygame.locals import *


class App:
    """Create a single-window app with multiple scenes."""
    SCREEN = None
    RUNNING = True
    FPS = 40
    FPS_OFFSET = 0
    CLOCK = pygame.time.Clock()

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        App.SIZE = self.w, self.h = 1024, 576
        pygame.display.set_caption('Blackjack Game')
        App.SCREEN = pygame.display.set_mode(App.SIZE, 0, 32)

    @staticmethod
    def run():
        """Run the main event loop."""
        while App.RUNNING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.RUNNING = False

            App.SCREEN.fill(Color(13, 148, 136))
            pygame.display.update()
            App.CLOCK.tick(App.FPS)
        App.quit()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    App().run()
