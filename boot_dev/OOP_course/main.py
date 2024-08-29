import random


def sort_it(lst):
    return (
        lst[1].index("Hearts"),
        lst[1].index("Diamonds"),
        lst[1].index("Clubs"),
        lst[1].index("Spades"),
    )


def sort_on(lst):
    new_list = sorted(lst, reverse=True, key=sort_it)
    print(new_list)


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for rank in DeckOfCards.RANKS:
            for suit in DeckOfCards.SUITS:
                self.__cards.append((rank, suit))

        self.__cards.sort(key=lambda x: DeckOfCards.SUITS.index(x[1]))

        print(self.__cards)
        # print(DeckOfCards.SUITS.index("Diamonds"))


deck = DeckOfCards()

print(deck)
