from os import system
from random import choice
from art import logo, vs
from game_data import data

playing = True
while playing:
    score = 0    
    person1 = choice(data)
    person2 = choice(data)
    winning = True
    while winning:
        system("cls")
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        print(vs)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == "A" and person1['follower_count'] > person2['follower_count']:
            score += 1
            person2 = choice(data)
        elif guess == "B" and person2['follower_count'] > person1['follower_count']:
            score += 1
            person1, person2 = person2, choice(data)
        else:
            winning = False
    system("cls")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    answer = input("Would you like to play again? Enter 'y' or 'n': ")
    if answer == 'n':
        playing = False
