# Solution

If we have to do 'n' no of rotations. It means first 'n' elements will go in the last

If n elements are `arr[:n]`. This gives elements from index 0 to n-1
The elements from index n and onwards can be fetched using `arr[n:]`

To get the result we need to do put first n elements in the last as follows

```
arr[n:] + arr[:n]
```
