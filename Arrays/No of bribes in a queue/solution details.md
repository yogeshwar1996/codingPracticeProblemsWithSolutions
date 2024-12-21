## Approach to Solve the Problem

### Solution 1:

1. **Loop through the queue from first to last index**:
2. **Check for chaos**: For each person in the queue, check if they are more than two positions ahead of where they should be, print `"Too chaotic"` and stop.
3. **Count the bribes**: For each person, start from the first person till the current person and check how many people with a larger number have gone ahead of them in the queue as they must have bribed the current person.

### Solution 2: (optimal)

1. **Loop through the queue backwards (last to first index)**:
2. **Check for chaos**: For each person in the queue, check if they are more than two positions ahead of where they should be, print `"Too chaotic"` and stop.
3. **Count the bribes**: For each person, check and compare people two indices before it, if current person has been bribed he can be bribed by at most too people one immediately before him and one 2 steps before him.

## Time Complexity:

- **O(n²)**: The algorithm loops through each person and, for each person, checks all the people before them in the queue to count bribes. This results in a nested loop, making the time complexity quadratic.

### Iterating Backwards vs Iterating Forwards

- **Iterating backwards** simplifies the task of counting bribes because you can only look at a limited number of previous positions (at most 2), and the problem constraints are naturally handled.

- **Iterating forwards** is possible, but it complicates the counting of bribes, as you'd need to compare with people behind you and possibly track more state information.
