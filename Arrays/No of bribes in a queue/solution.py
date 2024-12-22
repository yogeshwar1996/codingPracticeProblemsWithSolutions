def minimum_bribes(queue):
    chaotic = False
    bribes = 0

    for currentIndex, currentValue in enumerate(queue):
        expectedCurrentValue = currentIndex + 1
        if currentValue - expectedCurrentValue > 2:
            chaotic = True

        # For all values from the starting, and before the current value
        # If any value is greater than current value, it has bribed the current value
        for index in range(currentIndex):
            if queue[index] > currentValue:
                bribes += 1

    if chaotic:
        print("Too chaotic")
    else:
        print(bribes)
