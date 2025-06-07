"""Name: Ambrea Williams
   
   Date: 06/07/2025

   Unit 3: Lab 3

   Description: Guess The Number / Hangman Game. A program that asks the player to guess a random number between 1 and 15. 
   If the guess is incorrect, the next body part is added to the hangman.  
   """

import random

"""The general seven stages of the hangman game."""
hangman_stages = [r"""  -----
                       |   |
                           |
                           |
                           |
                           |
                   ---------
                   """,
                  r""" -----
                      |   |
                      O   |
                          |
                          |
                          |
                  ---------
                  """,
                  r""" -----
                      |   |
                      O   |
                      |   |
                          |
                          |
                  --------- 
                  """,
                  r""" -----
                      |   |
                      O   |
                     /|   |
                          |
                          |
                  ---------
                  """,
                  r""" -----
                      |   |
                      O   |
                     /|\  |
                          |
                          |
                  ---------
                  """,
                  r"""
                      -----
                      |   |
                      O   |
                     /|\  |
                     /    |
                          |
                  ---------
                  """,
                  r""" -----
                      |   |
                      O   |
                     /|\  |
                     / \  |
                          |
                  ---------
                  """
]

"""asks the player to guess a random number between 1 and 15"""
number_to_guess = random.randint(1,15) 

"""len(hangman_stages) calculates the total # of stages in the hangman stages list"""
max_wrong_guesses = len(hangman_stages)- 1

wrong_guesses = 0

print('Come on and play Guess The Number - Hangman Game!')
print('Guess a number between 1 and 15.')

"""the loop statement (while) keeps the code going as long as the condition remains true"""
while wrong_guesses < max_wrong_guesses:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 15.")
        continue
    
    if guess == number_to_guess:
        print(f"Congratulations! You've guessed the number {number_to_guess}. You win!")
        break
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} guesses left.")
        print(hangman_stages[wrong_guesses])


if wrong_guesses == max_wrong_guesses:
    print("Game over! You've been hanged.")
    print(f"The correct number was {number_to_guess}.")
