# Solved using merge sort

We chose to solve this using merge sort as it divides the array of values to the level where we are get single values and then we compare them and merge them to sort which is just like the inversion operation


When we merge the values we compare if the value in the right array is less then the left array it means we are doing an inversion operation

Now the number of inversions here is equal to the number of elements in the left array before which the right element is getting merged

i.e the len of left array  - current index of left array


In merge sort
The splitting process takes 
`O(logn)` time, as the array is divided in half at each step, and there are `log n` levels of division.

The merging process, where two sorted halves are combined, takes 
O(n) time at each level of the recursion.

In total it takes `O(n logn)` time


NOTE:
How many times can you keep dividing the array in half until you reach subarrays of size 1? The number of divisions is equal to the number of times you can divide n by 2 until you get 1, which is the logarithm base 2 of n, denoted as log n with base 2.

For example if n is 8
Then 8/2 = 4, 4/2 = 2, 2/2 = 1 => 3 divisions
or log 8 with base 2 is 3

Log n base 2 means how many times n is recurisvely divisible by 2 to get 1


