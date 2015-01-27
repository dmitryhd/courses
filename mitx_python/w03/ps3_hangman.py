#!/usr/bin/env python2
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res = ''
    for letter in secretWord:
        if not letter in lettersGuessed:
            res += '_ '
        else:
            res += letter + ' '
    return res

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph = string.ascii_lowercase
    res = ''
    for letter_index in range(len(alph)):
        if not alph[letter_index] in lettersGuessed:
            res += alph[letter_index]
    return res

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    mistakesMade = 0
    def guess():
        print("-------------")
        print("You have {} guesses left.".format(8 - mistakesMade))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))
        letter = raw_input('Please guess a letter:')
        letter = letter.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            return 2
        if letter in secretWord:
            lettersGuessed.append(letter)
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            return 0
        else:
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            lettersGuessed.append(letter)
            return 1

    while True:
        res = guess()
        if res == 1: # omg
            mistakesMade += 1
            if mistakesMade == 8:
                print('-----------')
            	print('Sorry, you ran out of guesses. The word was else.')
                return
        if res == 0 and isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            return
            


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'aabc'
hangman(secretWord)
