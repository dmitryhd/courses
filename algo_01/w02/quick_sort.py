#!/usr/bin/env python3 

""" Quick sort implementation. """

import unittest
import sys

sys.setrecursionlimit(100000)

cmpr = 0

def choose_pivot(arr, i, k):
    return i

def choose_pivot_first(arr, i, k):
    return i

def choose_pivot_last(arr, i, k):
    return k

def choose_pivot_mid(arr, i, k):
    mid = int((k - i)/2) + i
    if (arr[i] <= arr[mid] <= arr[k]):
        return mid
    if (arr[i] <= arr[k] <= arr[mid]):
        return k
    if (arr[mid] <= arr[k] <= arr[i]):
        return k
    if (arr[mid] <= arr[i] <= arr[k]):
        return i
    if (arr[k] <= arr[i] <= arr[mid]):
        return i
    if (arr[k] <= arr[mid] <= arr[i]):
        return mid

def quicksort(arr, l, r):
    if l >= r:
        return
    global cmpr
    #print('quicksort {}, {}: was {}'.format(l, r, arr[l:r+1]))
    cmpr += r - l
    q = partition(arr, l, r)
    #print('quicksort: after part in {} was {}'.format(q, arr))
    quicksort(arr, l, q-1)
    quicksort(arr, q+1, r)


def partition(arr, l, r):
    pivot_index = choose_pivot(arr, l, r)
    arr[pivot_index], arr[l] = arr[l], arr[pivot_index]
    #pivot_index = l
    p = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < p:
            #print('swap {} {}'.format(arr[i], arr[j]))
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i - 1


class TestQuickSort(unittest.TestCase):
    def test_chose_pivot(self):
        assert True

    def test_partition(self):
        arr = [3, 8, 2, 5, 1, 4, 7, 6]
        exp = [2, 1, 3, 5, 8, 4, 7, 6]
        partition(arr, 0, len(arr) - 1)
        assert arr == exp, 'got {}'.format(arr)

    def test_quicksort(self):
        test_cases = [#([3, 8, 2, 5, 1, 4, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8]),
                      #([3, 2, 1], [1, 2, 3]),
                      ([5, 4, 2, 3, 1], [1, 2, 3, 4, 5])
                     ]
        for arr, exp in test_cases:
            quicksort(arr, 0, len(arr) - 1)
            assert arr == exp, 'got {}'.format(arr)

def get_comparisons(fname, function):
    global cmpr
    global choose_pivot
    choose_pivot = function
    cmpr = 0
    with open(fname) as fd:
        arr = []
        for line in fd.readlines():
            arr.append(int(line))
        quicksort(arr, 0, len(arr) - 1)
        #print(arr)
    return cmpr


def main():
    import sys
    for test_fn in ['data/10.txt', 'data/100.txt', 'data/1000.txt']:
        x1 = get_comparisons(test_fn, choose_pivot_first)
        x2 = get_comparisons(test_fn, choose_pivot_last)
        x3 = get_comparisons(test_fn, choose_pivot_mid)
        print(x1, x2, x3)
    fn = 'data/QuickSort.txt'
    x1 = get_comparisons(fn, choose_pivot_first)
    x2 = get_comparisons(fn, choose_pivot_last)
    x3 = get_comparisons(fn, choose_pivot_mid)
    print(x1, x2, x3)

    #unittest.main()
    # 10     25        29        21
    # 100   615      587      518
    #1000 10297 10184  8921
    # anwwers: 162085 164123 138382
if __name__ == '__main__':
    main()
