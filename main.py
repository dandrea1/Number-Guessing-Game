from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100..")

rand_number = randint(1,100)
#testing line
#print(f"Psst... it's {rand_number}")
 
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_of_guesses = 0
game_over = False

if game_difficulty == 'easy':
    print("you chose easy")
    number_of_guesses = 10
elif game_difficulty == 'hard':
    print("you chose hard")
    number_of_guesses = 5

while game_over == False:
    if number_of_guesses == 0:
         print("You've run out of guesses. You lose.")
         game_over = True
    else:   
        print(f"Guess again.\nYou have {number_of_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand_number:
            print(f"You got it! The number was {rand_number}")
            game_over = True
        elif guess > rand_number:
            number_of_guesses -= 1
            print("Too high.")
        else:
            number_of_guesses -= 1
            print("Too low.")

