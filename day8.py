# 44 Programming questions Code
# Ultra easy questions:
#8) Assume that the user will enter a moderately long (10+ words) sentence as input. Split this sentence into words,
# then display it as one word per line.

sentence = "sit amet luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor purus non enim praesent"
list = sentence.split(" ")
for i in list:
    print(i)