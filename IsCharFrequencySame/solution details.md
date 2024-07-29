We first find the frequency of each character
How many times each char occurs? > Char count
Then we check how many characters are there with same frequency? > Freq count


If there are more than two different frequencies, it's not possible to make the string valid by removing just one character.
Example aabbbcccc
a:2
b:3
c:4

we have 3 different frequencies ie 2,3,4

If there are exactly two frequencies, we check if:

If one of the frequency is 1 and the unique characters with that is also 1. Meaning there was a single extra character. Which we can remove to make the string valid

IF we have a frequency which is 1 more than the other and it occurs for only 1 type of char then also string is valid
Example aabbccddd

a:2 b:2 c:2 d:3

[2,2,2,3] => {2:3, 3:1}
this means we have frequency2 -1  == frequency 2 and no_of_chars_with_frequency2 == s1

