#!/bin/python3

import math
import os
import random
import re
import sys


def maximumToys(prices, budget):
    maxToys = 0
    prices.sort()
    for price in prices:
        if price <= budget:
            budget -= price
            maxToys += 1
        else:
            break

    return maxToys

if __name__ == '__main__':
    

    budget = int(input())

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, budget)

    print(f'Maximum toys that can be bought: {result}')
