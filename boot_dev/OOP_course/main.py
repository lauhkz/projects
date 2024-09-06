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


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(
            # top left corner
            (self.pos_x - (self.width / 2)),
            (self.pos_y + (self.height / 2)),
            # bottom side
            (self.pos_x + (self.width / 2)),
            (self.pos_y - (self.height / 2)),
        )

    def in_area(self, x1, y1, x2, y2):
        new_rec = Rectangle(x1, y1, x2, y2)
        return new_rec.overlaps(self.__hit_box)


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
