def minimum_bribes(arr):
    bribes = 0
    n = len(arr)

    """
    Start from  the last index n-1 , go backwards till index 0, reducing index by 1 each time 
    """
    for i in range(n - 1, -1, -1):
        """
        If the difference between value at index and expected value at that index is greater than 2,
        then the person has bribed more than 2 people to be in the current position
        """
        if arr[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        """
        Check how many people have bribed the current value arr[i]
        When  arr[i] gets bribed the briber takes its position arr[i]-1 
        The briber can make one more bribe and will then be at arr[i]-2
        
        Note: arr[i]-2 does not mean two steps before the current position 
        It means 1 position before the arr[i]'s expected position

        Example in case where 7 bribes 6, then 7 bribes 5, then 8 bribes 6
        index 0 1 2 3 4 5 6 7
        Value 1 2 3 4 7 5 8 6

        for arr[i] 6, we need to start from 1 index before (6's expected index)i.e 1 index before 5, i.e index 4
        Check values at indices 4,5,6
        """

        starting_index_for_sliding_window = max(0, arr[i] - 2)
        """Since arr[i]-2 can be -ve also when i = 0|1, we need to ensure starting index is not -ve so we use max(0, arr[i]-2)"""

        for j in range(starting_index_for_sliding_window, i):
            if arr[j] > arr[i]:
                bribes += 1

    print(bribes)
