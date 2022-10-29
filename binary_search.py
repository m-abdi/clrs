from math import floor


value = "Zahraa"


def binary_search(Array, start, end, value):
    if start == end:
        if Array[start] == value:
            return start
        return False
    elif start > end:
        return False

    midpoint = floor((start + end) / 2)
    if Array[midpoint] == value:
        return midpoint
    if Array[midpoint] > value:
        return binary_search(Array, start, midpoint, value)
    else:
        return binary_search(Array, midpoint + 1, end, value)


Array = ['Asad', "Mahram", "Majid", "Mehdi", "Saeid", "Zahra"]
resp = binary_search(Array, 0, len(Array)-1, value)

print(resp)
