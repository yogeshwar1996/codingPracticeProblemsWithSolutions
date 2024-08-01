from collections import Counter
def is_valid_string(s):
    # Step 1: Count frequency of each character
    char_counts = Counter(s)

    # Step 2: Count frequency of these frequencies
    freq_counts = Counter(char_counts.values())

    # If there's only one frequency,
    # which means all the characters of string are same
    # the string is valid
    # Example aaa => char_count={a:3}, freq_count={3:1} len(freq_count)=1
    if len(freq_counts) == 1:
        return "YES"

    # If there are more than 2 different frequencies, it's invalid
    # Example aabbbcccc => char_count={a:2, b:3,c:4}, freq_count={2:1,3:1,4:1} len(freq_count) = 3
    # It means there are at least 2 characters with different frequencies
    # and it will require more deletions to make the string valid
    if len(freq_counts) > 2:
        return "NO"

    # If there are exactly 2 different

    # We fetch the frequencies and how many times they occur (or we can say for how many unique chars they occur)
    (freq1, no_of_chars_with_freq1), (freq2, no_of_chars_with_freq2) = (
        freq_counts.items()
    )

    # If we have frequency 1 means that a character occurred only once
    # and if we have no_of_chars_with_freq1 as 1 this frequency 1 occrred only for 1 type of character
    # and we remove this single character, the string will be valid as all other characters are of same frequency
    # Example abbccdd => char_count={a:1, b:2, c:2, d:2}, freq_count={1:1, 2:3}
    if (freq1 == 1 and no_of_chars_with_freq1 == 1) or (
        freq2 == 1 and no_of_chars_with_freq2 == 1
    ):
        return "YES"

    # if we dont have any character which occured only once
    # Then there should be  just once such char whose  frequency is higher that the frequency of other characters by 1
    # Example aabbccddd => char_count={a:2, b:2, c:2, d:3}, freq_count={2:3, 3:1}

    if (freq1 - 1 == freq2 and no_of_chars_with_freq1 == 1) or (
        freq2 - 1 == freq1 and no_of_chars_with_freq2 == 1
    ):
        return "YES"

    return "NO"

if __name__ == "__main__":
    s = input().strip()
    print(is_valid_string(s))
