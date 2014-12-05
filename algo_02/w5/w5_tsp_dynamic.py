#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
# 
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer is 26442

import sys
import itertools
from math import sqrt

def load_graph(filename):
    with open(filename) as fd:
        fl = fd.readline()
        n = int(fl.split()[0])
        vertices = []
    for line in fd.readlines():
        x = float(line.split()[0])
        y = float(line.split()[1])
        vertices.append([x, y])
    return vertices

def length(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def solve_tsp_dynamic(points):
    all_distances = [[length(x,y) for y in points] for x in points]
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    l = 0
    for i in range(1,len(res[1])):
        x = res[1][i]
        y = res[1][i-1]
        l += length(points[x], points[y])

    l += length(points[res[1][len(res[1])-1]], points[res[1][0]])
    return l

# TODO: add to testing framework
def test():
    ans = {4: 'tsp2.txt',
            10.4721: 'tsp3.txt',
            6.17986: 'tsp4.txt',
            6.26967: 'tsp5.txt',
            124.966: 'tsp6.txt',
            16898.1: 'tsp8.txt',
            }
    for an, fn in ans.items():
        l = solve_tsp_dynamic(load_graph(fn))
        assert abs(an - l) <= 0.1, 'get ans {} for fn={}'.format(l, fn)

test()
l = solve_tsp_dynamic(load_graph(sys.argv[1]))
print(l)
