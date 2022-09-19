import sys
import os
import pygame
from pygame.locals import *
from pygame.rect import Rect, RectType
from blackjack_helper import *

def load_image(name, colorkey=None, only_image=False, size=(150, 200)):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image', name)
        raise SystemExit(message)
    # image = image.convert()
    image = pygame.transform.scale(image, size)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    if only_image:
        return image
    else:
        return image, image.get_rect()


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

    def update(self, text):
        self.render(text)
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
    CARDS = []
    CLOCK = pygame.time.Clock()

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        App.SIZE = self.w, self.h = 1820, 720
        pygame.display.set_caption('Blackjack Game')
        App.SCREEN = pygame.display.set_mode(App.SIZE, 0, 32)
        App.t = Text('Blackjack Game', pos=(self.w/ 2, 10))
        # GENERATES THE STARTING HAND FOR BOTH DEALER AND PLAYER
        App.dealing = False
        App.game_up = False
        App.dealer_hand, App.dealer_cards = draw_starting_hand();
        App.player_hand, App.player_cards = draw_starting_hand();
        App.dealer_section = Text(f'Dealer\'s Hand', pos=(self.w / 3, 70))
        App.player_section = Text(f'Your Hand: {App.player_hand}', pos=(self.w / 3 - 20, 370))

    # @staticmethod
    # def draw_card(card, is):


    @staticmethod
    def load_cards():
        for i in range(13):
            card, card_rect = load_image(f'{i + 1}-club.jpg')
            App.CARDS.append([card, card_rect])


    @staticmethod
    def draw_cards(card_number, is_dealer_card=False, n_card_drawn=0):
        card = App.CARDS[card_number -1][0]
        card_rect = App.CARDS[card_number][1]
        if is_dealer_card:
            card_rect.center = (App.SIZE[0] / 3 + (170 * n_card_drawn), 210)
        else:
            card_rect.center = (App.SIZE[0] / 3 + (170 * n_card_drawn), 500)
        App.SCREEN.blit(card, card_rect)


    @staticmethod
    def end_game_screen(game_status):
        terminate = Text(f'{game_status}', (1420, 288), bold=False, size=48)


        new_game = False

        while not new_game:

            for event in pygame.event.get():

                if event.type == QUIT:
                    App().quit()
                if event.type == MOUSEBUTTONDOWN:
                    if btn_replay.get_rect().collidepoint(event.pos[0], event.pos[1]):
                        App().run()

            Text('Final Result', (1420, 188), bold=True, size=70,)
            btn_replay = Button((1340, 350), text='Replay')

            pygame.display.update()
        if new_game:
            App().run()

    @staticmethod
    def deal():
        App.dealing = True
        while App.dealer_hand <= 17:
            card_rank = draw_card()
            App.dealer_hand += card_rank;
            App.dealer_cards.append((card_rank))
        App.dealer_section.update(f'Dealer Hand: {App.dealer_hand}')
        App.game_up = True



    @staticmethod
    def run():
        """Run the main event loop."""

        App.load_cards()

        back_card, back_card_rect = load_image('card-back.jpg')
        back_card_rect.center = (App.SIZE[0] / 3 + 170, 210 )


        print(App.dealer_hand, App.dealer_cards, App.player_hand, App.player_cards)

        while App.RUNNING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.RUNNING = False
                elif event.type == MOUSEBUTTONDOWN:
                    if btn_hit.get_rect().collidepoint(event.pos):
                        if App.player_hand < 21:
                            card_value = draw_card()
                            App.player_hand += card_value
                            if App.player_hand >= 21:
                                App.deal()

                            App.player_cards.append(card_value)
                        else:
                            App.deal()

                    elif btn_deal.get_rect().collidepoint((event.pos)):
                        App.deal()

                    elif btn_stand.get_rect().collidepoint(event.pos):
                        App.deal()



            # Draw on screen
            App.SCREEN.fill(Color(13, 148, 136))
            App.t.draw()
            App.dealer_section.draw()
            App.player_section.draw()
            App.draw_cards(App.dealer_cards[0], is_dealer_card=True)
            for indx, card in enumerate(App.player_cards):
                App.draw_cards(card, n_card_drawn=indx)
            App.SCREEN.blit(back_card, back_card_rect)
            App.player_section.update(f'Your Hand: {App.player_hand}')

            if App.dealing:
                for indx, card in enumerate(App.dealer_cards):
                    App.draw_cards(card, is_dealer_card=True, n_card_drawn=indx)

            btn_deal = Button((50, 150), text='Deal')
            btn_hit = Button((50, 250), text='Hit')
            btn_stand = Button((50, 350), text='Stand')

            if App.game_up:
                game_status = (print_end_game_status(App.player_hand, App.dealer_hand))
                App.end_game_screen(game_status)

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
