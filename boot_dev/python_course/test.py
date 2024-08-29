list_of_protagonists = [
    {"Vagabond": "Misashi"},
    {"Berserk": "Guts"},
    {"Way of kings": "Kaladin"},
]

list_of_protagonists2 = [
    {"blue lock": "Misashi"},
    {"jujutsu kaisen": "Guts"},
    {"chainsaw man": "denji"},
]

purchase_orders = [
    {"price": 10.00, "money_available": 125.00},
    {"price": 5.00, "money_available": 2.00},
    {"price": 20.01, "money_available": 5.20},
]

alphabet_list = [
    ("p", 6121),
    ("r", 20818),
    ("o", 25225),
    ("j", 504),
    ("e", 46043),
    ("c", 9243),
    ("t", 30365),
    ("g", 5974),
    ("u", 10407),
    ("n", 24367),
    ("b", 5026),
    ("s", 21155),
    ("f", 8731),
    ("a", 26743),
    ("k", 1755),
    ("i", 24613),
    ("y", 7914),
    ("m", 10604),
    ("w", 7638),
    ("l", 12739),
    ("d", 16863),
    ("h", 19725),
    ("v", 3833),
    ("z", 243),
    ("x", 677),
    ("q", 324),
]


def sort_it(lst):
    return (lst["Hearts"], lst["Diamonds"], lst["Clubs"], lst["Spades"])


def sort_on(lst):
    new_list = sorted(lst, reverse=True, key=lambda char: char[1])
    print(new_list)


cards = [
    ("Ace", "Clubs"),
    ("2", "Clubs"),
    ("3", "Clubs"),
    ("4", "Clubs"),
    ("5", "Clubs"),
    ("6", "Clubs"),
    ("7", "Clubs"),
    ("8", "Clubs"),
    ("9", "Clubs"),
    ("10", "Clubs"),
    ("Jack", "Clubs"),
    ("Queen", "Clubs"),
    ("King", "Clubs"),
    ("Ace", "Diamonds"),
    ("2", "Diamonds"),
    ("3", "Diamonds"),
    ("4", "Diamonds"),
    ("5", "Diamonds"),
    ("6", "Diamonds"),
    ("7", "Diamonds"),
    ("8", "Diamonds"),
    ("9", "Diamonds"),
    ("10", "Diamonds"),
    ("Jack", "Diamonds"),
    ("Queen", "Diamonds"),
    ("King", "Diamonds"),
    ("Ace", "Hearts"),
    ("2", "Hearts"),
    ("3", "Hearts"),
    ("4", "Hearts"),
    ("5", "Hearts"),
    ("6", "Hearts"),
    ("7", "Hearts"),
    ("8", "Hearts"),
    ("9", "Hearts"),
    ("10", "Hearts"),
    ("Jack", "Hearts"),
    ("Queen", "Hearts"),
    ("King", "Hearts"),
    ("Ace", "Spades"),
    ("2", "Spades"),
    ("3", "Spades"),
    ("4", "Spades"),
    ("5", "Spades"),
    ("6", "Spades"),
    ("7", "Spades"),
    ("8", "Spades"),
    ("9", "Spades"),
    ("10", "Spades"),
    ("Jack", "Spades"),
    ("Queen", "Spades"),
    ("King", "Spades"),
]

sort_on(cards)
