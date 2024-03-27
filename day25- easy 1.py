#44 Programming questions Code
#Easy questions:
#1) Ignoring white-space, check if two strings are anagrams.

print("44 Programming questions Code - Easy 1\nhttps://github.com/xsenemy/44-programming-questions\n")

def anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    for i in string1:
        if i not in string2:
            return False
        else:
            return anagram(string1.replace(i, ""), string2.replace(i, ""))
    return True


string1 = "c iao c".replace(" ", "").lower()
string2 = "oiaCc".replace(" ", "").lower()

if anagram(string1, string2) and anagram(string2, string1):
    print("Anagram.")
else:
    print("Not an anagram.")
