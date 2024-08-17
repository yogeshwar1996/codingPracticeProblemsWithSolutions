Since the array size is fixed i.e 6 x 6
We know the 

first hour glass with all elements is possible for index 1,1 
where from where all the other elements are accessible 
and last such hourglass will be for index 4,4
```
  0 1 2 3 4 5 
0 x x x
1   x
2 x x x
3       x x x
4         x
5       x x x

```

Sum of hour glass wih central point i,j from where we start iterating,

will be 

```
arr[i-1][j-1]  + arr[i-1][j]  + arr[i-1][j+1]
                    arr[i][j] + 
 arr[i+1][j-1] + arr[i+1][j]  + arr[i+1][j+1]
```

Then we just push all the sums in arr and find the max