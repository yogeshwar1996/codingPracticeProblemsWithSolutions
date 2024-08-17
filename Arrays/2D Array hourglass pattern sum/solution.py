def findMaxSum(arr):
    hourGlassSums = []
    for i in range(1,5):
        for j in range(1,5):
            sum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            hourGlassSums.append(sum)

    return max(hourGlassSums)
