# Understanding the array
Note: indices start from 0 and values start from 1
```
arr[0] 1
arr[1] 2
arr[2] 3
```

Similarly value `arr[i]` is at index `arr[i]-1`<br>
```
arr[0] is at index arr[0]-1 ie 1-1 = 0
arr[1] is at index arr[1]-1 ie 2-1 = 1
```

## Solution 1

Algo
* Iterate the array
* if value at index i i.e arr[i] is not i+1 and their difference is greater than 2 its too chaotic
* Then iterate backwards from position i-1 till index 0
  * if value is greater than a[i], count it as a bribe.

  Example
  [1 2 5 3 7 8 6 4]

We start with i=0 till i=7
* i=0, a[0] is 1 which is fine
* i=1 a[1] is 2 which is fine
* i=2 a[2] is 5 , expected was 2+1 ie 3 but 5-3 !> 2 which is fine <br>
  Now we iterate backwards from i-1 to 0 comparing values with a[2]<br>
  But none is bigger than 5
* i=3 a[3] is 3, expected was 3+1 i.e 4 but 3-4 !> 2<br>
  Now we iterate backwards from i-1 to 0 comparing values with a[3]<br>
  * 5 is bigger than 3, bribe+=1 ie 1
  * 2,1 are smaller
 
* i=4 a[4] is 7, expected was 4+1 i.e 5 but 7-5 !>2 which is fine <br>
  Now we iterate backwards from i-1 to 0 comparing values with a[4]<br>
  * 3,5,2,1 all are is smaller than 7 
* i=5 a[5] is 8 expectec was 5+1 i.e 6 but 8-6 !>2 which is fine<br> 
  Now we iterate backwards from i-1 to 0 comparing values with a[5]<br>
  * 7,3,5,2,1 all are smaller than 8
* i=6 a[6] is 6 expectec was 6+1 i.e 7 but 6-7 !>2 which is fine<br> 
  Now we iterate backwards from i-1 to 0 comparing values with a[6]<br>
  * 8,7 are bigger than 6 bribe+=2 ie 3
  * 3,5,2,1 all are smaller than 6
* i=7 a[7] is 4 expectec was 7+1 i.e 8 but 4-7 !>2 which is fine<br> 
  Now we iterate backwards from i-1 to 0 comparing values with a[7]<br>
  * 8,7,6,5 are bigger than 4 bribe+=4 ie 7
  * 3,2,1 all are smaller than 4

  Total bribes are 7


  Since we have an inner loop that iterates all the way backwards from i-1 to 0 to count bribes.<br>
  The time complexity of this algo is O(n^2)

## Solution 2

Algo
* Iterate backwards from index n-1 to 0 
* if current value - expected value ie a[i] - (i+1) > 2 , its too chaotic
* Iterate from max(0, a[i]-2) to i-1 and if any value is bigger than a[i] count it as a bribe

We use `max(0, q[i]-2)` for case if `q[i]-2` is negative we start with index 0 <br>
Now why start from `q[i]-2`, because <br>
We know index of value `arr[i]` is `arr[i]-1`
when it gets bribed the briber comes at index `arr[i]-1`
we know briber can bribe one more time and goto `arr[i]-2`

So thats why we start from index `arr[i]-2`

Time complexity: O(n^2) 

 
