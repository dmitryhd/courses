#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
# https://class.coursera.org/algo2-003/quiz/attempt?quiz_id=89
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer = -19

"""
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem.
our task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one.
used bellman ford algo
"""

import sys
sys.path.append('../')
import coursera_test

def load_graph(filename):
    with open(filename) as fd:
        fl = fd.readline()
        vn = int(fl.split()[0])
        en = int(fl.split()[1])
        edges = []
    for line in fd.readlines():
        v1 = int(line.split()[0])
        v2 = int(line.split()[1])
        w = int(line.split()[2])
        edges.append([v1, v2, w])
    return vn, edges

def bellman_ford(vn, edges, src):
    has_negative = False
    d = [float("inf")]*vn
    d[src-1] = 0
    for i in range(vn-1):
        for edge in edges:
            if d[edge[1]-1] > d[edge[0]-1] + edge[2]:
                d[edge[1]-1] = d[edge[0]-1] + edge[2]
    old_d = d[:]
    for edge in edges:
        if d[edge[1]-1] > d[edge[0]-1] + edge[2]:
            d[edge[1]-1] = d[edge[0]-1] + edge[2]
    if d != old_d:
        has_negative = True
        print('has negative cycles!')
    return d, has_negative

def full_bellman_ford(vn, edges, start=1):
    minimum_dist = float('inf')
    for i in range(start, vn + 1):
        d, negative = bellman_ford(vn, edges, i)
        if negative == True:
            return float('inf')
    minimum_dist = min(min(d), minimum_dist)
    sys.stdout.write('\r{}/{}. mindist = {}'.format(i, vn, minimum_dist))
    return minimum_dist


def test():
    vn, edges = load_graph('tests/g4.txt')
    d, negative = bellman_ford(vn, edges, 1)
    assert d == [0, 2, 4, 6, 3]
    assert negative == False

    vn, edges = load_graph('tests/g5.txt')
    d, negative = bellman_ford(vn, edges, 1)
    assert negative == True

# TODO: add test system here
vn, edges = load_graph(sys.argv[1])
#d, negative = bellman_ford(vn, edges, 1)
#print(min(d), negative)
print(full_bellman_ford(vn, edges, int(sys.argv[2])))
# only g3 hasnt nonneg cycle and ans is -19 (335->670 vert)
