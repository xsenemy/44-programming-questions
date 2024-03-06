#44 Programming questions Code
#Very easy questions:
#15) Flip two coins, and note whether they land as two heads. two tails, or a head and a tail. Do this a thousand times
# and display the results as three percentages.

import random

flips = 1000
faces = [0, 1]
results = {
    "two heads" : 0,
    "two tails" : 0,
    "one one": 0,
}

for i in range(flips):
    coin1 = random.choice(faces)
    coin2 = random.choice(faces)
    if coin1 == 0 and coin2 == 0:
        results["two heads"] += 1
    elif coin1 == 1 and coin2 == 1:
        results["two tails"] += 1
    else:
        results["one one"] += 1

two_heads = results["two heads"]
two_tails = results["two tails"]
one_one = results["one one"]
print(f"Flips: {flips}\n")
print("Two heads:\t{}\t\t%{:.2f}\nTwo tails:\t{}\t\t%{:.2f}\nOne & one:\t{}\t\t%{:.2f}".format(two_heads, two_heads * 100/flips, two_tails, two_tails * 100/flips, one_one, one_one * 100/flips))
