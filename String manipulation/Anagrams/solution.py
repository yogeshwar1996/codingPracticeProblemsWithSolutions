#!/bin/python3

from collections import Counter


def makeAnagram(a, b):
    frequency_a = Counter(a)
    frequency_b = Counter(b)

    all_chars = set(frequency_a.keys()).union(set(frequency_b.keys()))
    deletions = 0
    for char in all_chars:
        deletions += abs(frequency_a[char] - frequency_b[char])

    return deletions

if __name__ == "__main__":

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(f"Result {res}")
