#!/usr/bin/python
#-*- coding: utf-8 -*-

# For coursera algo course 02.
#
# by Dmitriy Khodakov (dmitryhd@gmail.com) - 08.08.2014

def run_tests(cases, solve_function, load_function):
    # format: file_with case, answer
    for case in cases:
        res = solve_function(*load_function(case[0]))
        assert res == case[1], 'test case {} gone wrong, get {}'.format(case[0], cc)
    print('\n---------------\nall %i tests passed.' % len(cases))
