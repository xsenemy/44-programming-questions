#44 Programming questions Code
#Ultra easy questions:
#12) Write a program that lets you play "Higher/Lower" vs a computer. Take turns to see who chooses, and who guesses.

import random


def question_choose():
    n = 0
    for i in db:
        print(f"{n + 1} - {db[n]['question']}")
        n += 1
    question = int(input("Insert the question number:")) - 1
    return question

def next_question():
    print("Choose the question to compare with:")
    return question_choose()


def quiz_the_computer(question1, score):
    computer_guessings = ["y", "n"]
    question2 = next_question()
    while question2 == question1:
        question2 = next_question()
    print(f'\n{db[question1]["question"]}')
    print(f"Is higher than {db[question2]['question']}? Y or N")
    computer_guess = computer_guessings[random.randint(0, 1)]
    print(f"Computer guess: {computer_guess}")
    if computer_guess == "y" and db[question1]['answer'] > db[question2]['answer'] or computer_guess == "n" and db[question1]['answer'] < db[question2]['answer']:
        score += 1
        print(f"score: {score}")
        print("good, next question\n")
        question1 = question2
        quiz_the_computer(question1, score)
    else:
        print("Wrong answer, game over")
        print(f"score: {score}")
        score = 0
        print("\nUSER TURN")
        question1 = random.randint(0, len(db)-1)
        quiz_the_user(question1, score)

def next_question_user():
    return random.randint(0, len(db) - 1)

def quiz_the_user(question1, score):
    question2 = next_question_user()
    while question2 == question1:
        question2 = next_question_user()
    print(db[question1]["question"])
    user_guess = input(f"Is higher than {db[question2]['question']}? Y or N\n")
    if user_guess == "y" and db[question1]['answer'] > db[question2]['answer'] or user_guess == "n" and db[question1]['answer'] < db[question2]['answer']:
        score += 1
        print(f"score: {score}")
        print("good, next question")
        question1 = question2
        quiz_the_user(question1, score)
    else:
        print("Wrong answer, game over")
        print(f"score: {score}")
        score = 0
        print("\nCOMPUTER TURN")
        print("\nChoose a question the computer have to guess:")
        question1 = question_choose()
        quiz_the_computer(question1, score)


db = [
    {"question" : "1000",
     "answer" : 1000},
    {"question" : "2000",
     "answer" : 2000},
    {"question" : "3000",
     "answer" : 3000},
    {"question" : "4000",
     "answer" : 4000},
]
score = 0
is_running = True
while is_running:
    user = input("choose, guess or quit? ")
    if user == "quit":
        is_running = False
    elif user == "choose":
        print("\nChoose a question the computer have to guess:")
        question1 = question_choose()
        quiz_the_computer(question1, score)
    elif user == "guess":
        question1 = random.randint(0, len(db)-1)
        quiz_the_user(question1, score)
