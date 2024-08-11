import math
import os
import random
import re
import sys


def countSwaps(a):
    swapCount = 0
    n = len(a)

    # in bubble sort for n values we make n - 1 comparisons 
    # resulting in at least 1 value being sorted to its correct position
    # and we repeat this n times to sort the entire array
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                swapCount+=1
                c = a[j]
                a[j] =  a[j+1]
                a[j+1] = c
    
    print(f'Array is sorted in {swapCount} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    # Example
    # 4
    # 10 5 7 4
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
