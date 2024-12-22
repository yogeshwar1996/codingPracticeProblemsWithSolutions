def minimumSwaps(arr):
    i = swap = 0

    while i < len(arr):
        print(f"i is {i}")
        """
         currentValue => arr[i]
         expectedIndexOfCurrentValue = arr[i] - 1
         exisitingValueAtExpectedIndexOfCurrentValue => arr[arr[i] - 1]
        """
        while arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swap += 1
        i += 1
    return swap
