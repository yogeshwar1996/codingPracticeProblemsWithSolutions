# Solution 1

- Iterate over all indices
- In each iteraton, check if element at current index is at its expected position.
- Since we have are given list of unordered consecutive integers. Value at any index in when sorted should be index + 1.
- If element is not at its expected position, swap with element at its expected position, and increment the swap counter.
- Keep doing this till the element at current index is at its expected position
- Iterate to next index

# Solution 2

When un-ordered list of integers is given of len n. Where value are not consecutive. A more generic solution that is applicable is as follows -

- Create a list of (value, index) tuples from the given unordered array.
- Sort the list by value in the tuple
- Initialize a list to track visited values [False] \* n
- Iterate over the list of tuples, in each iteration
  - determine cycle size
  - determin swap count, as swap count = cycle size - 1
- return swap count
