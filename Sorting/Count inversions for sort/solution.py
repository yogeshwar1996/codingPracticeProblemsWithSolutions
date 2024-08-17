#!/bin/python3

import math
import os
import random
import re
import sys

inversions = 0


def merge(left_half, right_half):
    """
    To modify a global variable inside a function, you need to use the global keyword.
    Without it, Python treats the variable as a local variable,
    leading to errors like "local variable referenced before assignment.
    """
    global inversions
    
    left_index = 0
    right_index = 0
    sorted_arr = []
    while left_index < len(left_half) and right_index < len(right_half):
        value_in_left = left_half[left_index]
        value_in_right = right_half[right_index]

        if value_in_left <= value_in_right:
            sorted_arr.append(value_in_left)
            left_index += 1
        else:
            sorted_arr.append(value_in_right)
            right_index += 1
            # since right one comes before the remaining left ones that many inversions are counted
            inversions += len(left_half) - left_index

    sorted_arr += left_half[left_index:]
    sorted_arr += right_half[right_index:]
    return sorted_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        sorted_left_half = merge_sort(left_half)
        sorted_right_half = merge_sort(right_half)
        return merge(sorted_left_half, sorted_right_half)


def countInversions(arr):
    merge_sort(arr)


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        inversions = 0  
        countInversions(arr)
        print(f'inversions are  {inversions}')


