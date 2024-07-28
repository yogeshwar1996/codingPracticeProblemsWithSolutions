# Longest Common Subsequence (LCS)

## Problem Statement

The **Longest Common Subsequence (LCS)** problem is to find the longest subsequence common to two given sequences. A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

### Input

- Two sequences (strings) `S1` and `S2`.

### Output

- The length of the longest common subsequence of `S1` and `S2`.
- Optionally, the longest common subsequence itself.

### Constraints

- `1 <= len(S1), len(S2) <= 1000`
- The sequences consist of uppercase English letters.

### Example

**Input:**

"ABCBDAB"<br>"BDCAB"


**Output:**

- Length of LCS = 4
- LCS = "BCAB"

