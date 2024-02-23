#44 Programming questions Code
#Ultra easy questions:
#5) Let the user input their [name]. and check if it is "Jack". If it is "Jack", print out "Hi Jack!". Otherwise, print out "Hello. [name]".

name = input("Type your name: ").capitalize()
if name == "Jack":
    print("Hi Jack!")
else:
    print(f"Hello {name}")