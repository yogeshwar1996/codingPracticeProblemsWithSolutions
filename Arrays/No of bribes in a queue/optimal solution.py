def minimum_bribes(arr):
    bribes = 0
    n = len(arr)

    """
    Note: indices start from 0 and values start from 1
    Note: value at index i i.e arr[i] should be i + 1 , example value at index 0 is 1
    Note: index of value arr[i] should be arr[i] - 1, example index of value 1 is 0

    Start from  the last index
    go backwards till 0 
    reducing index by 1, 
    hence iterate for range(n-1,-1,-1)
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
        Check how many people have bribed the value arr[i]
        Ideally, the position/index( arr[i] ) => arr[i]-1
        When  arr[i] gets bribed the briber takes its position arr[i]-1 
        The briber can make one more bribe and will then be at arr[i]-2
        So, the bribers position can start from arr[i]-2
        
        0 1 2 3 4 5 6 7
        ---------------
        1 2 3 4 5 6 7 8
        1 2 3 4 5 8 6 7 // 8 has bribed 6, 7
        
        while iterating we are at index 5 value should be 6 ideally, but its 8 
        checking current value - expected value
        8 - 6 = 2 // within limits, not too chaotic
        Now to check if 8 has been bribed
        We check for at most 2 people who are ahead of 8 in the queue 
        Since index(8) = 5 we check for index 3, 4
        at index 3 we have 4
        at index 4 we have 5
        Since both values 4,5 are less than 8 no-body bribed 8

        while iterating we are at index 6 value should be 7 ideally, but its 6 
        checking current value - expected value
        6 - 7 = -1 // within limits, not too chaotic
        Now to check if value 6 has been bribed
        We check for at most 2 people who are ahead of value 6 in the queue 
        Since index(6) = 6 we check for index 4, 5
        at index 4 we have 5
        at index 5 we have 8
        Since 8 is greater than 6 we increment the bribe counter

        Summary - After bribing the person arr[i], the briber takes its position i, which we can also say the briber takes the position arr[i] - 1
        Hence the briber of arr[i] would be either at position arr[i] - 1 or arr[i] - 2, i.e at most 2 positions prior to the current position
        So we will check in the sliding window of size 2, whether a number is greater than current number if so, we count that as a bribe.
        """

        starting_index_for_sliding_window = max(0, arr[i] - 2)
        """Since arr[i]-2 can be -ve also when i = 0|1, we need to ensure starting index is not -ve so we use max(0, arr[i]-2)"""

        for j in range(starting_index_for_sliding_window, i):
            if arr[j] > arr[i]:
                bribes += 1

    print(bribes)
