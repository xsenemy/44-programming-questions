#44 Programming questions Code
#Very easy questions:
#13) Make a standard deck of cards. Shuffle the deck. and draw two cards at random. Display the two cards.

import random

values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
seeds = ["♣", "♦", "♥", "♠"]
deck = []
for i in seeds:
    new_list = []
    for j in values:
        new_list.append(str(j) + i)
    deck.append(new_list)

print('Deck:')
for i in range(len(deck)):
    print(*deck[i])
random.shuffle(deck)
print('Shuffled Deck:')
for i in range(len(deck)):
    print(*deck[i])
seed = random.randint(0, 3)
card1 = random.choice(deck[seed])
card2 = random.choice(deck[seed])
while card2 == card1:
    card2 = random.choice(deck[seed])
print(f"\nCards: \t{card1}\t{card2}")
