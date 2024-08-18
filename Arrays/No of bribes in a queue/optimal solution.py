def minimum_bribes(arr):
    bribes = 0
    n = len(arr)

    # Note: indices start from 0 and values start from 1
    # Note: value at index i i.e arr[i] should be i + 1 , example value at index 0 is 1
    # Note: index of value arr[i] should be arr[i] - 1, example index of value 1 is 0

    # Start from  the last index go backwards till 0 reducing index by 1, hence iterate for range(n-1,-1,-1)
    for i in range(n-1, -1, -1):
        # If the difference between value at index and expected value at that index is greater than 2, then the person has bribed more than 2 people
        if arr[i] - (i + 1) > 2:            
            print("Too chaotic")
            return

        """
         Check how many people have bribed the value arr[i]
         Ideally, the position of value arr[i] is arr[i]-1
         When  arr[i] gets bribed the briber takes its position arr[i]-1 
         The briber can make one more bribe and will then be at arr[i]-2
         So, the bribers position can start from arr[i]-2
         After bribing the person at position i, the person at position i would be at position arr[i] - 1
         Hence those who bribed arr[i] would start from position arr[i] - 2 
        """
        for j in range(max(0, arr[i] - 2), i):
            if arr[j] > arr[i]:
                bribes += 1

    print(bribes)
