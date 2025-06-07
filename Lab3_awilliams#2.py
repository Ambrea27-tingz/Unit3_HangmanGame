"""Name: Ambrea Williams
   
   Date: 06/07/2025

   Unit 3: Lab 3

   Description: Import the file from project 1, do not copy and paste it.  Append 5 more items to the list.  Print the result.
   """

import random

hangman_stages = ["""  -----
                       |   |
                           |
                           |
                           |
                           |
                   ---------
                   """,
                  """ -----
                      |   |
                      O   |
                          |
                          |
                          |
                  ---------
                  """,
                  """ -----
                      |   |
                      O   |
                      |   |
                          |
                          |
                  --------- 
                  """,
                  """ -----
                      |   |
                      O   |
                     /|   |
                          |
                          |
                  ---------
                  """,
                  """ -----
                      |   |
                      O   |
                     /|\  |
                          |
                          |
                  ---------
                  """,
                  """
                      -----
                      |   |
                      O   |
                     /|\  |
                     /    |
                          |
                  ---------
                  """,
                  """ -----
                      |   |
                      O   |
                     /|\  |
                     / \  |
                          |
                  ---------
                  """
]

number_to_guess = random.randint(1,15) 

max_wrong_guesses = len(hangman_stages)- 1

wrong_guesses = 0

print('Come on and play Guess The Number - Hangman Game!')
print('Guess a number between 1 and 15.')

