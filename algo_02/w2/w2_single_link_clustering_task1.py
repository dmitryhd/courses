#!/usr/bin/python
#-*- coding: utf-8 -*-

# For coursera algo course 02.
# https://class.coursera.org/algo2-003/quiz/feedback?submission_id=35953
#
# by Dmitriy Khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer = 6118

import sys
sys.path.append('../')

def load_file(filename):
    edges = []
    clusters = []
    with open(filename) as fd:
        n = int(fd.readline())
        clusters = [[i] for i in range(n)]
        for line in fd.readlines():
            split_line = line.split()
            edges.append((int(split_line[0]) - 1 , int(split_line[1]) - 1, int(split_line[2])))
    return clusters, edges

def single_link_clustering(clusters, edges, k=4):
    edges = sorted(edges, key=lambda edge: edge[2])
    n_clust = len(clusters)
    while n_clust > k:
        spacing = edges[0][2]
        n1 = edges[0][0]
        n2 = edges[0][1]
        i = j = 0
        for x in range(n_clust):
            if n1 in clusters[x]:
                i = x
                continue
            if n2 in clusters[x]:
                j = x
        to_remove = []
        for x in range(len(edges)):
            if edges[x][0] in clusters[i] and edges[x][1] in clusters[j]:
                to_remove.append(x)
            if edges[x][0] in clusters[j] and edges[x][1] in clusters[i]:
                to_remove.append(x)
        new_edges = []
        for ind in range(len(edges)):
          if ind not in to_remove:
            new_edges.append(edges[ind])
        edges = new_edges
        new_clusters = []
        for ind in range(n_clust):
            if ind == i:
                new_clusters.append(clusters[i] + clusters[j])
            elif ind == j:
                continue
            else:
                new_clusters.append(clusters[ind])

        clusters = new_clusters
        n_clust=len(clusters)
    return edges[0][2]

import coursera_test
coursera_test.run_tests([['test_cases/clust10.txt', 134365]],
                        single_link_clustering,
                        load_file)

#clusters, edges = load_file(sys.argv[1])
#spacing = single_link_clustering(clusters, edges)
#print(spacing)
# clust 10 134365 k = 4
# ans is 106
