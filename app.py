import sys
import pygame
from pygame.locals import *
from pygame.rect import Rect, RectType


class Text(object):

    def __init__(self, text='Pygame', pos=(0, 0), bold=False, size=36):
        self.fontname = None
        self.pos = pos
        self.font = pygame.font.Font(self.fontname, size)
        self.font.set_bold(bold)
        self.color = Color('black')

        self.render(text)
        self.draw()

    def render(self, txt):
        self.img = self.font.render(txt, True, self.color)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos

    def draw(self):
        App.SCREEN.blit(self.img, self.rect)


class Button(object):
    """This is displays all the buttons in this game"""

    def __init__(self, pos, text='pygame'):
        """Initialises the button object"""
        self.text = text
        self.pos = pos
        self.color = (22, 78, 99)
        self.hover_color = (8, 145, 178)
        self.rect = pygame.Rect(pos, (150, 50))
        self.draw()
        self.check_hover()

    def draw(self):
        pygame.draw.rect(App.SCREEN, self.color, self.rect)
        pygame.draw.rect(App.SCREEN, (22, 78, 99), self.rect, 2)
        Text(self.text, (self.rect.centerx, self.rect.centery))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            pygame.draw.rect(App.SCREEN, self.hover_color, self.rect)
            pygame.draw.rect(App.SCREEN, (15, 118, 110), self.rect, 2)
            Text(self.text, (self.rect.centerx, self.rect.centery))

    def get_rect(self):
        return self.rect


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
        App.SIZE = self.w, self.h = 1024, 720
        pygame.display.set_caption('Blackjack Game')
        App.SCREEN = pygame.display.set_mode(App.SIZE, 0, 32)
        App.t = Text('Blackjack Game', pos=(self.w/ 2, 10))
        App.dealer_section = Text('Dealer\'s Hand', pos=(self.w / 3, 70))
        App.player_section = Text('Your Hand', pos=(self.w / 3 - 20, 370))


    @staticmethod
    def run():
        """Run the main event loop."""
        while App.RUNNING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.RUNNING = False

            # Draw on screen
            App.SCREEN.fill(Color(13, 148, 136))
            App.t.draw()
            App.dealer_section.draw()
            App.player_section.draw()

            Button((50, 150), text='Deal')
            Button((50, 250), text='Hit')
            Button((50, 350), text='Stand')

            # Update screen
            pygame.display.update()
            App.CLOCK.tick(App.FPS)
        App.quit()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    App().run()
