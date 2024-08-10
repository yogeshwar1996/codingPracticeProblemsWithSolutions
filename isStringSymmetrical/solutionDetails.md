# Solution1

The function iterates over all possible substrings of s of varying lengths (sub_length), from 1 to n.

For each substring of length sub_length

 * If sub_length is 1: Every single character is considered a special substring, so it is added directly to the substrings list.

 * If sub_length > 1: 

    Extract the substring starting at index i and of length sub_length.

    Calculate the frequency of each character in sub using Counter.

    Then check these conditions: 

    1. If there is only one unique character in the substring, its a special substring
    2. If substring contains more than two unique characters, it's not a special substring
    3. If substring has exactly two unique characters and the substring length is odd
        * count of 1st char should be 1 and count of the other should be sub_length - 1
        * char with count of 1, should be in middle

# Solution2 

Iterate over each character in the string (where index is tracked by i)

* Considering very character as special substring increment special substring count by 1
* Iterate from current char onwards till the next character matches or its end of the string,
  
  * For each matching character increment special substring count by 1

  * Also increment count of matching characters

* Now either its end of string or different char is found, and we have iterated till index i +  count of matching characters. <br> 
If still there are more characters ahead equal to the count of matching characters

    * Then iterate from the different character onwards `count of matching characters` times, 
        
* if all the chars are same as the initial char under consideration, increment special substring count



     

