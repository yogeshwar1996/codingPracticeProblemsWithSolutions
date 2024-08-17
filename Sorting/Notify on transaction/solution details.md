## Time Complexity 

### For optimal solution: 
Median Calculation: The median is calculated by iterating through a frequency array of size 201 (since the expenditure values are between 0 and 200). This takes 
O(201) or O(1) time since it's a constant operation.

Main Loop: For each new expenditure (from day d onwards), the solution iterates over the trailing d days to update the frequency array and then calculates the median. This process takes O(n×201) or O(n) time where n is the length of the expenditure list.

Total Time Complexity: O(n). The approach is efficient because the median calculation is done in constant time, thanks to the frequency array.

###For suboptimal solution

Median Calculation: The median is calculated by first sorting the trailing d days' expenditures. Sorting takes 
O(dlogd) time.

Main Loop: For each new expenditure (from day d onwards), the solution extracts the trailing d days, sorts them, and then calculates the median. This takes 
O(d * log d) time per iteration.

Total Time Complexity: O(n * d* logd). This approach is less efficient because sorting the trailing d days' expenditures for each iteration is computationally expensive.

## Space Complexity

Space for Frequency Array: Uses an array of size 201 to store the frequency of expenditures, which is O(1) in terms of space.

Total Space Complexity: O(1). The space usage is constant and minimal.


Space for Sorting: Needs to store the trailing d days' expenditures and sort them, which takes O(d) space.

Total Space Complexity: O(d). The space usage scales with d, so it can be higher depending on the value of d.

## Efficiency Comparison
First one is much more efficient in both time and space. The use of a frequency array allows for constant time median calculation, making the solution scalable even for large inputs.

Second one is less efficient due to the repeated sorting of the trailing d days' expenditures, which becomes computationally expensive as d increases. The space complexity is also higher because it requires storing and sorting the trailing expenses.
