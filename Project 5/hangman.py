# ****** Project 5 ******

import random
from words import words
import string


def get_valid_word(value):
    word = random.choice(value)  # randomly choose something from list
    while '-' in word or ' ' in word:
        word = random.choice(value)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user have guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nLives:', lives, '| You have used these letters: ',
              ' '.join(used_letters))

        # what current word is(ie W _ R D)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list), '\n')

        # getting user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives > 0:
        print('YAY! You guessed it', word)
    else:
        print('YOU DIED, sorry. The word was', word)


hangman()

# user_input = input('Type something: ')

# print(user_input)
