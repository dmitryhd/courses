#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
# https://class.coursera.org/algo2-003/quiz/attempt?quiz_id=85
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer01 = 2493893, answer02 = 4243395

"""
Knapsack problem solved by dinamic programming.
"""

import sys
sys.path.append('../')
import coursera_test

def load_file(filename):
    vs = [0]
    ws = [0]
    with open(filename) as fd:
        st = fd.readline()
        wr = int(st.split()[0]) + 1
        for st in fd.readlines():
            ssplit = st.split()
            v = int(ssplit[0])
            w = int(ssplit[1])
            vs.append(v)
            ws.append(w)
    return wr, vs, ws

def solve_knapsack(wr, vs, ws):
    # wr - knapsack capacity
    # vs - values of items
    # ws - weights of items
    n = len(vs)

    A = []
    for i in range(2):
        A.append([0]*wr)
    cr = 1
    pr = 0
    for i in range(1,n):
        cr, pr = pr, cr
        for x in range(0, wr):
            if x >= ws[i]:
                A[cr][x] = max(A[pr][x], A[pr][x - ws[i]] + vs[i])
            else:
                A[cr][x] = A[pr][x]
    return A[cr][wr-1]

def main():
    if len(sys.argv) == 1:
        cases = [
              ['test_cases/knapsack_test_01.txt', 60],
              ['test_cases/knapsack_test_02.txt', 60],
              ['test_cases/knapsack_test_03.txt', 60],
              ['test_cases/knapsack_test_04.txt', 27000],
              ['test_cases/knapsack_test_05.txt', 27000],
              ['test_cases/knapsack_test_06.txt', 27000],
              ['test_cases/knapsack_test_07.txt', 13],
            ]
        coursera_test.run_tests(cases,
                                solve_knapsack,
                                load_file)
    else:
        res = solve_knapsack(*load_file(sys.argv[1]))
        print(res)

if __name__ == '__main__':
    main()
