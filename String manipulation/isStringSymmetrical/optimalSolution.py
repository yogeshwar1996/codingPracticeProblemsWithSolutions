def substrCount(totalNoOfChars, s):
    palindrome_count = 0

    # For index of current character in the string
    for i in range(totalNoOfChars):
        # add the current character as a palindrome
        palindrome_count += 1

        # Initialize a variable for index of next character
        noOfMatchingChars  = 1

        # From current character, check next char if it matches its a palindrome, increment the count, then repeat this till we reach a different char or end of string.
        while (
            i + noOfMatchingChars < totalNoOfChars
            and s[i] == s[i + noOfMatchingChars]
        ):
            noOfMatchingChars += 1
            palindrome_count += 1 

        # Now s[i+j] is either at the end of the string, or a different character.

        # The characters we haves seen so far are from i are i + noOfMatchingChars
        # and if we noOfMatchingChars more characters ahead  we can check if palindrome exists for the characters seen so far
        indexOfDiffLetter = i + noOfMatchingChars
        if indexOfDiffLetter + noOfMatchingChars <= totalNoOfChars:
            # Check if any character after i+j, until i+j+j is different than  our start character
            # Since j more characetrs are to be checked, we start from 1 to j ie range(1, j+1)
            # If any different character is found, break the loop, else we have a palindrome
            for indexOfNextCharacter in range(1, j + 1):
                if (
                    indexOfDiffLetter + indexOfNextCharacter >= totalNoOfChars
                    or s[i] != s[indexOfDiffLetter + indexOfNextCharacter]
                ):
                    break

            else:
                palindrome_count += 1
    return palindrome_count


if __name__ == "__main__":
    s = 'aababb'
    print('String is ', s)
    print(substrCount(s, len(s)))


# Iterate over each character in the string
# From curr char check next is same, if yes increment count, keep checking next and incrementing count till end of string or a different char is found
# now either its end of string or different char is found
# Now To find palindromes with character in middle different
# Check if have same number of chars (which matched far till different char), ahead of different char also
# if all the chars ahead are same, then we have a palindrome

"""
Let's analyze the logic step by step:

Loop Breakdown
Outer Loop (for i in range(n)):

This loop iterates over each character in the string as a potential starting point of a "special" substring.
First Inner Loop (while loop):

The loop increments j as long as the characters s[i] and s[i+j] are the same.
For each match, palindrome_count is incremented.
This correctly counts substrings where all characters are the same.
Second Inner Loop (for loop):

After finding the first segment of identical characters, the code checks if there is an odd-length palindrome centered around s[i+j] with the same characters before and after it.
The loop breaks if any character after s[i+j] is different from s[i], which means it stops looking for palindromes.
If it successfully loops through without breaking, it increments palindrome_count by 1, accounting for this special case.
Edge Case Handling
The if i+j+j > n: condition ensures that we don't overrun the end of the string when looking for a valid special palindrome.

The inner for loop correctly checks for palindromes with a different middle character and ensures that it only increments the count if the conditions are fully met.
"""
