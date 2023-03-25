import collections

# typename - Card
# field_names - rank suit
# klasa obiektów - posiada tylko listę atrybutów, bez żadnych
# własnych metod - coś jak rekordy w bazie danych

Card = collections.namedtuple('Card', ['rank', 'suit'])

# ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# ['2', '3', '4', '5', '6', '7', '8', '9', '10']
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


# suits = 'spades diamonds clubs hearts'.split()
# ['spades', 'diamonds', 'clubs', 'hearts']


# print(suits)
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    #  osługuje [] oraz [::]
    #  iterowanie

#  klas FrenchDeck niejawnie dziedziczy z klasy object, to jej funkcjonalność nie jest dziedziczona,
#  a pochodzi z podległego modelu danych i kompozycji
# dzięki implementacji metod specjalnych __len__ i  __getitem__, klasa FrenchDeck zachowuje się jak
# standardowa sekwencja Pythona, które pozwalają na korzystanie z podstawowych funkcjonalności języka
# np. iteracji i wycinania oraz biblioteki standardowe -> random.choice, sorted, reversed
#
# dzięki kompozycji implementacje metod __len__ i __getitem__ mogą delegować całą pracę do obiektu list -
# o nazwie self._cards


# beer_card = Card('7', 'diamonds')
# Card(rank='7', suit='diamonds')

deck = FrenchDeck()
# zwróć liczbę kart zawartych w taliii
# print(len(deck))
# 52

# odczytaj kartę z talii
#  np. pierwszą i ostatnią
# print(deck[0])
# print(deck[-1])
#  dzięki __getitem__

# Card(rank='2', suit='spades')
# Card(rank='A', suit='hearts')


#  wybór losowej karty
# nie jest konieczne tworzenie nowej metody służącej do
# do wyboru losowej karty
# P. ma taką funkcję która służy do pobierania losowego elementu z sekwencji
# jest nią: random.choice

from random import choice

# print(choice(deck))


# print(deck[:3])
# [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

# przeglądanie talii począwszy od 12 indexu i pomijając 13 kart
# print(deck[12::13])
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# iterowanie

# for card in deck:
#     print(card)

# Card(rank='2', suit='spades')
# Card(rank='3', suit='spades')
# Card(rank='4', suit='spades')

# iterowanie w przeciwną stronę

# for card in reversed(deck):
#     print(card)

# Card(rank='A', suit='hearts')
# Card(rank='K', suit='hearts')
# Card(rank='Q', suit='hearts')

# niejawna iteracja
# gdy kolekcja nie ma metody __contains__ to operator in
# przeprowadza skanowanie sekwencyjne
# in działa z klasą FrenchDeck bo jest ona iterowalna

# print(Card('Q', 'hearts') in deck)
# True

# print(Card('7', 'beasts') in deck)
# False

# sortowanie
#  ranking kart - asy są najwyższe
#  kolor w kolejności od najwyższych do najniższych - spades (piki), hearts (kiery), diamonds (karo),
#  clubs (trefle)
# funkcja która ustawia karty wg zasady, zwracając 0 dla 2 trefl, a 51 dla asa pik:

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

#  dzięki spades_high można wyświetlić talię kart w kolejności rosnącej

for card in sorted(deck, key=spades_high):
    print(card)

# Card(rank='2', suit='spades')
# Card(rank='3', suit='spades')
# Card(rank='4', suit='spades')
# Card(rank='5', suit='spades')

# Card(rank='A', suit='clubs')
# Card(rank='A', suit='diamonds')
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='spades')



# str 8