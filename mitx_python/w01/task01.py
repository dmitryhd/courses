#!/usr/bin/env python2

import unittest

def count_vowels(text):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for char in text:
        if char in VOWELS:
            cnt += 1
    return cnt


def count_bob(text):
    # print "Number of times bob occurs is: {}".format(count_bob(s))
    cnt = 0
    for text_pos in range(len(text) - 2):
        if text[text_pos:text_pos+3] == 'bob':
            cnt += 1
    return cnt


def get_longest_alph(text):
    # print "Longest substring in alphabetical order is:", get_longest_alph(s)
    longest = ''
    cur_alph = ''
    cur_pos = 0
    while cur_pos < len(text):
        cur_alph += text[cur_pos]
        if cur_pos == len(text) - 1 or ord(text[cur_pos]) > ord(text[cur_pos + 1]):
            if len(longest) < len(cur_alph):
                longest = cur_alph
            cur_alph = ''
        cur_pos += 1
    return longest


class TestWordCounters(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(count_vowels('azcbobobegghakl'), 5)
        self.assertEqual(count_vowels('azcbobobegghakliu'), 7)

    def test_bob(self):
        self.assertEqual(count_bob('--bob---bob'), 2)
        self.assertEqual(count_bob('azcbobobegghakl'), 2)
        self.assertEqual(count_bob('bob'), 1)

    def test_alphabetical(self):
        self.assertEqual(get_longest_alph('abcd'), 'abcd')
        self.assertEqual(get_longest_alph('azcbobobegghakl'), 'beggh')
        self.assertEqual(get_longest_alph('abcbcd'), 'abc')
        self.assertEqual(get_longest_alph('sewswkjvzpobywpyzbetsx'), 'jvz')


if __name__ == '__main__':
    unittest.main()
