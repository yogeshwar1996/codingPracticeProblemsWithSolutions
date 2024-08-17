def rotateLeft(arr, noOfRotations):
    return arr[noOfRotations:] + arr[:noOfRotations]