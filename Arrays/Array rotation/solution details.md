# Solution

For arrays we can get use this syntax `arr[:d]` to get elements from starting to d-1 index

and we can use `arr[d:]` to get elements starting from d till end

For out solution we just need to move the elements starting and ahead of d forward by doing
```
arr[d:] + arr[:d]
```