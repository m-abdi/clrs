from datetime import datetime
from math import ceil, floor
from random import random, randint


def merge(input, first_index, middle_index, last_index):
    nl = middle_index - first_index + 1
    nr = last_index - middle_index
    L = [0 for i in range(nl)]
    R = [0 for i in range(nr)]
    for i in range(0, nl):
        L[i] = input[first_index + i]
    for j in range(0, nr):
        R[j] = input[middle_index + j + 1]

    i = 0
    j = 0
    k = first_index

    while i < nl and j < nr:
        if L[i] < R[j]:
            input[k] = L[i]
            i += 1
        elif R[j] < L[i]:
            input[k] = R[j]
            j += 1
        k += 1

    while i < nl:
        input[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        input[k] = R[j]
        j += 1
        k += 1


def merge_sort(input, first_index, last_index):
    if first_index >= last_index:
        return

    middle_index = floor((first_index + last_index) / 2)

    merge_sort(input, first_index, middle_index)
    merge_sort(input, middle_index+1, last_index)

    merge(input, first_index, middle_index, last_index)


input = [randint(1, 875) for i in range(23)]
start = datetime.now()
merge_sort(input, 0, len(input) - 1)

print(input)
print(datetime.now() - start)
