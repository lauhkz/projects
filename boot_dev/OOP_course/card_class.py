import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)

    def __eq__(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            if self.suit_index < other.suit_index:
                return True
        if self.rank_index < other.rank_index:
            return True
        return False

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            if self.suit_index > other.suit_index:
                return True
        if self.rank_index > other.rank_index:
            return True
        return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Equal should return False
# Greather Than should return True
# Less than should return False

card1 = Card("Ace", "Hearts")
card2 = Card("Queen", "Hearts")

print(f"{card1.__str__()}, {card2.__str__()}")
print(f"Equal: {card1.__eq__(card2)}")
print(f"Less Than: {card1.__lt__(card2)}")
print(f"Greater Than: {card1.__gt__(card2)}")
