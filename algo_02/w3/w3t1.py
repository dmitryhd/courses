#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014
# answer = 6118

def knapsack(filename):
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
  n = len(vs)
  #print(vs)
  #print(ws)

  A = []
  for i in range(2):
      A.append([0]*wr)
  cr = 1
  pr = 0
  for i in range(1,n):
    cr, pr = pr, cr
    print("i=",i)
    for x in range(0, wr):
      if x >= ws[i]:
        A[cr][x] = max(A[pr][x], A[pr][x - ws[i]] + vs[i])
      else:
        A[cr][x] = A[pr][x]
      #print('A[{}][{}]={}'.format(i, x, A[i][x]))

  #for line in A:
  #  print(line)
  return A[cr][wr-1]

assert knapsack('w3/knapsack_test_01.txt') == 60
assert knapsack('w3/knapsack_test_02.txt') == 60
assert knapsack('w3/knapsack_test_03.txt') == 60
assert knapsack('w3/knapsack_test_04.txt') == 27000
assert knapsack('w3/knapsack_test_05.txt') == 27000
assert knapsack('w3/knapsack_test_06.txt') == 27000
assert knapsack('w3/knapsack_test_07.txt') == 13
filename = 'knapsack1.txt'
print(knapsack(filename))
filename = 'knapsack_big.txt'
print(knapsack(filename))
