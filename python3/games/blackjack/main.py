import deck
import player
import logging
#import doctest

logging.basicConfig(level=logging.DEBUG)

def dealer():
    cards = deck.Deck()
    if cards.length > 10:
        player1.hand = cards.draw_card


def main():
    player1 = player.Player('bob')
    logging.debug(type(player1))
    player2 = player.Player('kevin')
    logging.debug(type(player2))
    cards = deck.Deck()
    logging.debug(type(cards))


if __name__ == '__main__':
    main()
