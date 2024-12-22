def min_swaps_to_sort(arr):
    # Create a list of tuples of (value, index)
    value_index_list = [(value, index) for index, value in enumerate(arr)]
    # Sort this list by the value in tuples.
    value_index_list.sort(key=lambda x: x[0])

    # To track visited elements, initialize a list with False values
    visited = [False] * len(arr)
    swap_count = 0

    for i in range(len(arr)):
        # Skip if the element is already visited or already in the correct position
        if visited[i] or value_index_list[i][1] == i:
            continue

        # Initialize the cycle size
        cycle_size = 0
        # Initialize the index for cycle
        j = i
        while not visited[j]:
            # Mark current index of cycle as visited
            visited[j] = True
            j = value_index_list[j][1]  # Move to the next index in the cycle
            cycle_size += 1

        """Here is how above logic works. Assume we have arr = [4, 3, 2, 1]
            Sorted value,index list is [(1, 3), (2, 2), (3, 1), (4, 0)]
            
            j=0, corsp tuple is Tuple (1,3), visited[0] = true, now we goto the index mentioned in (1,3), cycle_size++
            j=3, corsp tuple is Tuple (4,0), visited[3] = true, now we goto the index mentioned in (4,0), cycle_size++
            j=0 here the loop breaks as cycle completes as visited[0] is true
       """

        # If there's a cycle of size 'n', it takes 'n-1' swaps to resolve
        # Note a cycle is a group of elements where each element is not at its correct position and
        # needs to be moved to a new position to achieve a sorted order
        if cycle_size > 1:
            swap_count += cycle_size - 1

    return swap_count
