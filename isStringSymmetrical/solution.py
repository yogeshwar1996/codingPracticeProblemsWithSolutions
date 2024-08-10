import math
from collections import Counter
def substrCount(n, s):
    # Example aababb = [a,a,b,a,b,b,aa,bb,aba,bab]
    substrings = []
    for sub_length in range(1, n + 1):
        for i, char in enumerate(s):
            # For length == 1  all the individual characters are special
            if sub_length == 1:
                substrings.append(char)
            # For length > 1
            else:
                if i + sub_length > n:
                    continue
                sub = s[i : i + sub_length]
                char_count_in_sub = Counter(sub)
                # 'aa' =  {'a':2}
                if len(char_count_in_sub) == 1:
                    # if only 1 char then its special
                    # 'a','aa','aaa'
                    substrings.append(sub)
                elif len(char_count_in_sub) > 2:
                    # if more than 2 fdifferent chars in substring
                    # then its not valid
                    pass
                elif len(char_count_in_sub) == 2 and (sub_length % 2 != 0):
                    # For odd length substring with exactily two different chars
                    # count of 1st char should be 1 and
                    # count of the other should be sub_length - 1
                    # char with count of 1, should be in middle
                    (char1, count1), (char2, count2) = char_count_in_sub.items()
                    middle_char = sub[(math.floor(sub_length / 2))]
                    if (
                        count1 == 1
                        and count2 == sub_length - 1
                        and char1 == middle_char
                    ):
                        substrings.append(sub)
                    if (
                        count2 == 1
                        and count1 == sub_length - 1
                        and char2 == middle_char
                    ):
                        substrings.append(sub)

    return substrings

if __name__ == "__main__":
    s = 'aababb'
    n = len(s)
    print('String is ', s)
    print(substrCount(n, s))
