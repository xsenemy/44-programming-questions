#44 Programming questions Code
#Very easy questions:
#1) Make a standard deck of cards. Shuffle the deck. and draw two cards at random. Display the two cards.

import random


values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
seeds = ["\u2660", "\u2661", "\u2663", "\u2662"]
deck = []
deck_shuffled = []

print('Deck:')
for i in seeds:
    new_list = []
    for j in values:
        new_list.append(str(j) + i)
    deck.append(new_list)

for i in range(len(deck)):
    print(*deck[i], sep="\t")

print('Deck Shuffled')
char = []
for i in range(4):
    for j in range(len(deck[i])):
        char.append(deck[i][j])
random.shuffle(char)

n=0
for i in range(4):
    new_list = []
    for j in range(len(deck[i])):
        new_list.append(char[n])
        n += 1
    deck_shuffled.append(new_list)

for i in range(len(deck_shuffled)):
    print(*deck_shuffled[i], sep="\t")

card1 = random.choice(char)
card2 = random.choice(char)
while card2 == card1:
    card2 = random.choice(char)
print(f"\nCards: \t{card1}\t{card2}")
