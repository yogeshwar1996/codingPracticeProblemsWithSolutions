#!/bin/python3

import math
import os
import random
import re
import sys

def activityNotifications(expenditure, d):

    # Write your code heres
    print(f'd {d}')
    notifications = 0
    for i in range(d, len(expenditure)):
        # Even number of trailing days
        trailing_expenses = expenditure[i-d:i]
        print(f'trailing_expenses: {trailing_expenses}')
        trailing_expenses.sort()
        print(f'trailing_expenses sorrted: {trailing_expenses}')
        if d % 2 == 0:
            median = (trailing_expenses[d// 2] + trailing_expenses[d// 2 - 1]) / 2
        else:
            median = trailing_expenses[d // 2]
        if expenditure[i] >= 2 * median:
            notifications += 1
    return notifications

if __name__ == '__main__':
    d = int(input())

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
