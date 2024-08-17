"""
Ensure no adjacent characters are same
"""
def min_deletions_to_alternate(string):
    """
    Find the number of deletions are required to be made in the string,
    so that no adjacent characters are same
    """
    deletions = 0
    for i, char in enumerate(string):
        if i + 1 == len(string):
            break
        next_char = string[i + 1]
        if char == next_char:
            deletions += 1

    return deletions


# Example usage
if __name__ == "__main__":
    print(min_deletions_to_alternate("ABBABBAB"))  # Output: 2
