#!/usr/bin/env python2

import unittest

from ps3_hangman import *

class TestHangman(unittest.TestCase):
    def test_word_guess(self):
        secretWord = 'apple' 
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(isWordGuessed(secretWord, lettersGuessed), False)
        secretWord = 'durian'
        lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
        self.assertEqual(isWordGuessed(secretWord, lettersGuessed), True)

    def test_get_word(self):
        secretWord = 'apple'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(getGuessedWord(secretWord, lettersGuessed),
                         '_ p p _ e ')

    def test_get_available_letters(self):
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(getAvailableLetters(lettersGuessed),
                         'abcdfghjlmnoqtuvwxyz')


if __name__ == '__main__':
    unittest.main()
