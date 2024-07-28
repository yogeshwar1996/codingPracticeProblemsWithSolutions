### Time Complexity

Let's analyze the time complexity of the function `min_deletions_to_make_anagrams(s1, s2)`.

1. **Counting Frequencies**:
   - `count1 = Counter(s1)` and `count2 = Counter(s2)` both involve iterating over each string once.
   - If the lengths of `s1` and `s2` are \( n \) and \( m \) respectively, counting the frequencies takes \( O(n) \) and \( O(m) \).

2. **Creating the Set of Unique Characters**:
   - `all_chars = set(count1.keys()).union(set(count2.keys()))` involves iterating over the keys of both counters.
   - In the worst case, each counter has all unique characters, so the size of each set is at most the number of distinct characters (let's denote this as \( k \)).
   - Creating the union of these two sets takes \( O(k) \), where \( k \) is at most \( 26 \) (since there are only 26 letters in the English alphabet).

3. **Calculating the Number of Deletions**:
   - `for char in all_chars` iterates over all unique characters.
   - For each character, `deletions += abs(count1[char] - count2[char])` is an \( O(1) \) operation.
   - Since there are at most \( k \) unique characters, this loop takes \( O(k) \) time.

Combining these, the overall time complexity is:
\[ O(n + m + k) \]

Since \( k \) is a constant (at most 26), the time complexity simplifies to:
\[ O(n + m) \]

### Space Complexity

Let's analyze the space complexity of the function.

1. **Space for Counters**:
   - `count1` and `count2` each store frequencies of characters.
   - In the worst case, each counter has entries for all 26 characters.
   - Thus, the space for each counter is \( O(1) \) because the size of the counters is bounded by the number of distinct characters (26).

2. **Space for the Set of Unique Characters**:
   - `all_chars` contains all unique characters from both strings.
   - In the worst case, it has at most 26 elements.
   - Thus, the space for `all_chars` is \( O(1) \).

3. **Auxiliary Space**:
   - The variable `deletions` and loop variables use \( O(1) \) space.

Combining these, the overall space complexity is:
\[ O(1) \]

### Summary

- **Time Complexity**: \( O(n + m) \), where \( n \) and \( m \) are the lengths of the two input strings.
- **Space Complexity**: \( O(1) \), considering the space for counters and the set of unique characters is bounded by a constant (the number of distinct characters in the alphabet).

This solution is efficient in both time and space, making it suitable for the given problem.