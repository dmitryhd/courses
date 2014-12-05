#!/usr/bin/env python3

import random

DEFAULT_FN = 'data/kargerMinCut.txt'
MAX_TRY = 100

def build_graph(datafn):
    gr = {}
    with open(datafn) as dfd:
        for line in dfd.readlines():
            numbers = line.split()
            src = int(numbers[0])
            gr[src] = []
            for dst in numbers[1:]:
                gr[src].append(int(dst))
    return gr

def choose_random_key(gr):
    v1 = random.choice(list(gr.keys()))
    v2 = random.choice(list(gr[v1]))
    return v1, v2


def random_min_cut(graph, seed=None):
    random.seed(seed)
    while len(graph) > 2:
        v_merge, v_del = choose_random_key(graph)
        graph[v_merge].extend(graph[v_del])
        for dst in graph[v_del]:
            graph[dst].remove(v_del)
            graph[dst].append(v_merge)
        while v_merge in graph[v_merge]:
            graph[v_merge].remove(v_merge)
        del graph[v_del]
    length = []
    for vert in graph.keys():
        length.append(len(graph[vert]))
    return length[0]

def main():
    test = [(2, 'data/test02.txt'),
     (2, 'data/test03.txt'),
     (1, 'data/test04.txt'),
     (1, 'data/test05.txt'),
     ]
    for exp_val, fname in test:
        res = 100000
        for num in range(MAX_TRY):
            graph = build_graph(fname)
            val = random_min_cut(graph)
            res = min(res, val)
        assert res == exp_val, '{}, res={}'.format(fname, res)
    res = 100000
    for num in range(100):
        graph = build_graph(DEFAULT_FN)
        res = min(res, random_min_cut(graph))
    print(res)

# ans is 17
if __name__ == '__main__':
    main()
