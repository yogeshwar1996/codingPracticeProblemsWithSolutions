def minimumBribes(q):
    bribes = 0
    i = 0
    n = len(q)

    while i < n:
        if q[i] != (i + 1):
            # Check if the current person is too far ahead of their original position
            if q[i] - (i + 1) > 2:
                print("Too chaotic")
                return

            # Check for larger numbers ahead until a smaller number is found
            j = i - 1
            while j >= 0:
                if q[j] > q[i]:
                    bribes += 1
                    j -= 1
                else:
                    break

        i += 1

    print(bribes)


# Example use
minimumBribes([2, 1, 5, 3, 4])  # Output: 3
