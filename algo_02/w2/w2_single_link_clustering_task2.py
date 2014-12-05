#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
# https://class.coursera.org/algo2-003/quiz/feedback?submission_id=35953
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer = 6118

"""
Single link clustering of large (200000) quantity of 01101101(24 bit) numbers.
Metric - huffman distance.
Main idea:
    for every number in input:
        generate all 1 and 2 distance numbers
        look for this numbers in all input, if they exists, then
            place these numbers in graph
    count number of connected components - answer
"""
import sys
sys.path.append('../')

def load_file(filename):
    vertices = []
    with open(filename) as fd:
        fd.readline()
        for line in fd.readlines():
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            vertices.append(int(line,2))
    return [vertices]

def generate_sub(a, max_bit=24):
    vals = [a]
    for i in range(max_bit):
        vals.append(a ^ (1<<i))
    for i in range(max_bit-1):
        tmp = a ^ (1<<i)
        for j in range(i,max_bit):
            vals.append(tmp ^ (1 << j))
    return vals

def dfs(graph, start):
    S = [start]
    while S:
        v = S.pop()
        if graph[v][1] == False:
            graph[v][1] = True
            for w in graph[v][0]:
                S.append(w)

def find_connected_components(graph):
    res = 0
    all_visited = False
    while not all_visited:
        for v in graph.keys():
            if graph[v][1] == False:
                dfs(graph, v)
                res += 1
        all_visited = True
        for v in graph.keys():
            if graph[v][1] == False:
                all_visited = False
    return res

def get_single_link_clustering_max_k(v):
    edges = []
    for i in range(len(v)):
        vals = generate_sub(v[i])
        for val in vals:
            if val in v:
                edges.append([v[i], val])
    graph = {}
    for val in v:
        graph[val] = [[],False]
    for edge in edges:
        graph[edge[0]][0].append(edge[1])

    return find_connected_components(graph)

def main():
    if len(sys.argv) == 1:
        import coursera_test
        cases = [
              ['test_cases/p2_case1.txt', 1],
              ['test_cases/p2_case2.txt', 3],
              ['test_cases/p2_case3.txt', 4],
              ['test_cases/p2_case4.txt', 11],
            ]
        coursera_test.run_tests(cases,
                                get_single_link_clustering_max_k,
                                load_file)
    else:
        res = get_single_link_clustering_max_k(load_file(sys.argv[1]))
        print(res)

if __name__ == '__main__':
    main()

