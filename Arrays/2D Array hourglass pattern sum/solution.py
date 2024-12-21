def findMaxSum(arr):
    """
    NOTE: range(1,5) means 1,2,3,4
    We have to iterate
    from: seond row whose index is 1
    till: second last row i.e no_of_rows - 1
    So if no_of_rows is 5, we iterate till 4th
    and index of 4th row will be 3,
     so we iterate from index 1 to 3 ie range(1,4)

    """
    hourGlassSums = []
    no_of_rows = len(arr)
    no_of_cols = len(arr[0])

    for i in range(1, no_of_rows - 1):
        for j in range(1, no_of_cols - 1):
            sum = (
                arr[i][j]
                + arr[i - 1][j - 1]
                + arr[i - 1][j]
                + arr[i - 1][j + 1]
                + arr[i + 1][j - 1]
                + arr[i + 1][j]
                + arr[i + 1][j + 1]
            )
            hourGlassSums.append(sum)

    return max(hourGlassSums)
