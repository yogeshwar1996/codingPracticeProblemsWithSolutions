# Space and Time Complexity Analysis

## Time Complexity:

### Worst-Case Time Complexity: 
The time complexity of this Bubble Sort implementation is O(n^2).

The outer loop runs n times.

The inner loop also runs n-1 times for each iteration of the outer loop.

Thus, the total number of comparisons (and potential swaps) is n * (n-1) which simplifies to O(n^2).

### Best-Case Time Complexity: 
O(n^2).

Even if the array is already sorted, this implementation still goes through all n * (n-1) comparisons since it doesn't have an early exit mechanism.

## Space Complexity:
The space complexity of this implementation is O(1).
No extra space is used apart from a few variables (swapCount, n, i, j, c).

The sorting is done in-place, meaning the input array a is modified directly without requiring additional memory proportional to the size of the array.

Summary
Time Complexity: O(n^2)
Space Complexity: O(1)
