## Approach to Solve the Problem

### Solution 1:

1. **Loop through the queue from first to last index**:
2. **Check for chaos**: For each person in the queue, check if they are more than two positions ahead of where they should be, print `"Too chaotic"` and stop.
3. **Count the bribes**: For each person, start from the first person till the current person and check how many people with a larger number have gone ahead of them in the queue as they must have bribed the current person.

## Time Complexity:

- **O(n²)**: The algorithm loops through each person and, for each person, checks all the people before them in the queue to count bribes. This results in a nested loop, making the time complexity quadratic.

### Solution 2: (optimal)

1. **Loop through the queue backwards (last to first index)**:
2. **Check for chaos**: For each person in the queue, check if they are more than two positions ahead of where they should be, print `"Too chaotic"` and stop.
3. **Count the bribes**: For each person, determine their expected position, example arr[i] should be at index arr[i]-1 and if it gets bribed, briber will take its position, and briber can still briber 1 more person and goto position arr[i]-2. So from index arr[i]-2 and before index i compare the values to arr[i] and count the bribes.
