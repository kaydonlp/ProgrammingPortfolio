#KaydonPayne
#October 9th, 2019
#Hangman Game



#The classic game of Hangman.
#The computer picks a random word
#The player tries to uess it
#One letter at a time
#If the player cant guess the word in time,
#The little stick figure gets hung


#imports
import random
import time
#Constants


    #Hangman Art
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

#Initialize Variables

word = random.choice(WORDS) #Word to be guessed
so_far = "-" * len(word)#One dash per letter in word to be guessed
wrong = 0#Number of wrong guesses
used = []     #Letters already guessed

print("Welcome to Hangman,   Good Luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used all the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You have laready guessed the letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "Is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nSorry", guess, "is not in the word.")
        wrong += 1
        
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been Hung!!!")

else:
    print("\nYou guessed it!!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
        
    






































