
# Finding longest common subsequence

LCS (longest common subsequence) between two strings S1 and S2, is determined by iterating over them.
We compare the characters of the two strings, one by one and for this we use a 2D array of size len(S1) + 1 and len(S2) + 1

This represents the strings S1 lets say `axbycz` and S2 `bxyzc` in a tabular form like this


|    | "" | b | x | y | z | c |
| -- | -- | - | - | - | - | - |
| "" | 0  | 0 | 0 | 0 | 0 | 0 |
| a  | 0  | 0 | 0 | 0 | 0 | 0 |
| x  | 0  | 0 | 0 | 0 | 0 | 0 |
| b  | 0  | 0 | 0 | 0 | 0 | 0 |
| y  | 0  | 0 | 0 | 0 | 0 | 0 |
| c  | 0  | 0 | 0 | 0 | 0 | 0 |
| z  | 0  | 0 | 0 | 0 | 0 | 0 |

`Table of size len(S1) + 1, len(S2) + 1`

We added and extra 1 to the array size for rows and columns, for the case where the strings are empty and we initalize the values of lcs for 
them as 0 as there can be nothing common when one string is empty

Since we already marked lcs for the case i=0 or j=0 when we initialized the table, we iterate it from `i=1, j=1` i.e. from `range(1, len(S1)+1)` and `range(1, len(S2)+1)`
As we iterate, we keep evaluating the LCS at each step (i,j), based on whether characters at that step, match or not.

### When characters match

If the characters match it means they contribute to common subsequence at that step, 
and to mark that contribution, we add 1 to the longest common subsequence found so far for characters in the strings before the current step i.e i-1 and j-1.

```python
if self.str1[i-1] == self.str2[j-1]:
    self.lcs_table[i][j] = self.lcs_table[i - 1][j - 1] + 1
```
Note: Since 2D array we are iterating is of length (len(str) + 1, len(str2) + 1) and strings have lengths
len(str1), len(str2) only we need to reduce 1 from both i, j indices to iterate the stings

### When characters do not match

If the characters do not match, then we determine the max of - 
LCS  of String1 till current step with string2( where we exclude its current character that did not match) i.e self.lcs_table[i][j-1], and
LCS  of String2 till current step with string1( where we exclude its current that did not match) i.e self.lcs_table[i-1][j]

```python
if self.str1[i-1] != self.str2[j-1]:
    self.lcs_table[i][j] = max(self.lcs_table[i][j-1],self.lcs_table[i-1][j])
```
Finally when we would have iterated the entire 2d array comparing each character in both the strings. We will get the LCS in the last cell

##### Note
We solve this problem using dynamic programming
Dynamic programming is a method for solving complex problems by
*  breaking them down into simpler subproblems and solving each subproblem only once, storing 
their solutions – usually using a memory-based data structure (like an array or table) – to avoid redundant computations.

We build the 2D array with bottom up approach,where starts solving the problem from the simplest (smallest) subproblems and builds up to the solution of the original, larger problem


## Printing the LCS

An empty list `lcs=""` is initialized to store the characters of the LCS as we backtrack the `lcs_table`
The indices are set to max values i.e the lengths of the strings S1 and S2

Then the `lcs_table` is iterated from the bottom corner such that

### When chars match

If characters at `i, j` i.e `S1[i-1]` and `S2[j-1]` match, we put them in front of the lcs string
and update the indices to move up in our iteration diagonally decrementing i and j by 1

```
lcs = matching_char + lcs
i = i - 1
j = j - 1
```

### When chars match dont match

If characters dont match we move in the direction where lcs value is more i.e. either `i-1` or `j-1`



```python
if (lcs_table[i-1][j] > lcs_table[i][j-1]):
    i = i - 1 
else:
    j = j - 1
```
When we are done iterating `lcs` is our result

**NOTE** With this approach we get only 1 of the longest common subsequences.


## Printing all the LCS(s)
For the strings `axbycz` and `bxyzc` the lcs_table looks like this - 
           
|    | "" | b | x | y | z | c |
| -- | -- | - | - | - | - | - |
| "" | 0  | 0 | 0 | 0 | 0 | 0 |
| a  | 0  | 0 | 0 | 0 | 0 | 0 |
| x  | 0  | 0 | 1 | 1 | 1 | 1 |
| b  | 0  | 1 | 1 | 1 | 1 | 1 |
| y  | 0  | 1 | 1 | 2 | 2 | 2 |
| c  | 0  | 1 | 1 | 2 | 2 | 3 |
| z  | 0  | 1 | 1 | 2 | 3 | 3 |


Start from the bottom-right cell of the LCS table and trace back to the top-left cell. Such that -
```
If the characters match, they are part of the LCS and appended to subsequences found moving diagonally upwards
If they don't match,
    Follow the path with the larger value (either left or up) to find all possible LCS paths.
    If the values on both paths are same then follow both
```
**Step1**
The characters corsp to 6,5 in S1,S2 are z,c which dont match<br>
No we look for the combinations 5,5(leftwards) and 6,4(upwards)<br>
Value at leftwards and upwards is 3 so we follow both the paths and try to find the chars for lcs

**Step1.1**<br>
For (5,5) corsp chars in S1,S2 are c, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally 
**Append c to result of (4,4)**

For(4,4) corsp chars in S1,S2 are y,z which don't match so we check the values leftwards and upwards its 2, 1 respectively so we move leftwards to (4,3)

For (4,3) corsp chars in S1,S2 are y, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (3,2)
**Append y to result of (3,2)**

For (3,2) corsp chars in S1,S2 are b,x, which don't match so we check the values leftwards and upwards its 1, 1 respectively, which is same, so we move in both directions (3,1) and (2,2)

**Step1.1.1**<br>
For (3,1) corsp chars in S1,S2 are b, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (2,0)
**Append b to result of (2,0)**

For (2,0) since j==0 we will return empty string

**Step1.1.2**<br>
For (2,2) corsp chars in S1,S2 are x, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (1,1)
**Append x to result of (1,1)**

For(1,1) corsp chars in S1,S2 are a, b which don't match so we check the values leftwards and upwards its 0, 0 respectively, which is same, so we move in both directions (0,1) and (1,0)

Both (0,1) and (1,0) will return empty string

**Step1.2**<br>
For (6,4) corsp chars in S1,S2 are z. so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (5,3)
**Append z to result of (5,3)**


For(5,3) corsp chars in S1,S2 are c,y  which don't match so we check the values leftwards and upwards. its 1, 2 respectively, So we move upwards to (4,3)

For (4,3) corsp chars in S1,S2 are y, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (3,2)
**Append y to result of (3,2)**

For (3,2) corsp chars in S1,S2 are b,x which don't match so we check the values leftwards and upwards. its 1, 1 respectively,so we move in both directions
(3,1) and (2,2)

**Step1.2.1**<br>
For(3,1) corsp chars in S1,S2 are b. so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (2,0)
**Append b to result of (2,0)**

For 2,0 will return empty string.

**Step1.2.2**<br>
For (2,2) corsp chars in S1,S2 are x, so we find matching char which we will add in the end of the lcs strings we find by backtracking diagonally backwards to (1,1)
**Append x to result of (1,1)**

For(1,1) corsp chars in S1,S2 are a, b which don't match so we check the values leftwards and upwards its 0, 0 respectively, which is same, so we move in both directions (0,1) and (1,0)

Both (0,1) and (1,0) will return empty string
    

Now we have finished iteration and the situation is like this

Step1.1.1 -> b 
<br>Step1.1.2 -> x
<br>Step1.1 -> byc, xyc

<br>Step1.2.1 -> b
<br>Step1.2.2 -> x
<br>Step1.2 -> byz, xyz


Step1 -> byc, xyc, byz, xyz

**Result**
The lcs for `axbycz` and `bxyzc` are `byc, xyc, byz, xyz`

## Time Complexity

The time complexity for filling the lcs table is O(m x n), where m is the length of S1 and n is the ength of S2. This is because we iterate through each cell of the table once.

After filling the LCS table, backtracking to print one LCS takes O(m + n), as in the worst case, we might traverse from the bottom-right to the top-left of the table, moving diagonally, up, or left.

Printing all LCSs is more complex. In the worst case, the number of LCSs can be exponential. Specifically, if there are multiple optimal subproblems that can be solved in different ways, we may need to explore all combinations. Thus, the time complexity can be O(2**min(m,n)) in the worst case.