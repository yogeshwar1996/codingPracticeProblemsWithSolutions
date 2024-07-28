"""Here we aim to solve Longest Common Subsequence"""


class LongestCommonSubsequence:
    """Class to  encapsulate the methods involbed in solving LCS"""

    def __init__(self):
        self.str1 = ""
        self.str2 = ""
        self.lcs_table = []
        self.lcs_length = 0
        self

    def read_input(self):
        """Read input from user"""
        self.str1 = input()
        self.str2 = input()

    def solve(self):
        """Method to solve the problem using dynamic programming"""
        print("Solving the problem for inputs ", self.str1, self.str2)
        str1_length = len(self.str1)
        str2_length = len(self.str2)

        row_count = str1_length + 1
        col_count = str2_length + 1
        # Initialize the 2D array with 0s
        # self.lcs_table = [[0] * col_count] * row_count
        self.lcs_table = [[0] * col_count for _ in range(row_count)]
        # Iterate the 2D array and keep evaluating the lcs
        for i in range(1, row_count):
            for j in range(1, col_count):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.lcs_table[i][j] = self.lcs_table[i - 1][j - 1] + 1
                else:
                    self.lcs_table[i][j] = max(self.lcs_table[i][j - 1], self.lcs_table[i - 1][j])

        print(f"The lcs table is {self.lcs_table}")
        self.lcs_length = self.lcs_table[str1_length][str2_length]
        print("Length of Longest Common Subsequence is ", self.lcs_length)

    def print_lcs(self):
        """Method to print the longest common subsequence"""

        lcs_string = ""
        i = len(self.str1)
        j = len(self.str2)
        while i > 0 and j > 0:
            if self.str1[i - 1] == self.str2[j - 1]:
                lcs_string = self.str1[i - 1] + lcs_string
                i -= 1
                j -= 1
            elif self.lcs_table[i - 1][j] > self.lcs_table[i][j - 1]:
                i -= 1
            else:
                j -= 1
        print(f'LCS String is {lcs_string}')

    def print_all_lcs(self):
        """Method to print all the longest common subsequences"""
        def backtrack(i, j):
            if i == 0 or j == 0:
                return {""}

            if self.str1[i - 1] == self.str2[j - 1]:
                # If the characters are same, then  we will iterating backward to i-1 and j-1 and find the LCS for it
                # then add the current character to the each of those LCS                  #

                lcs_set_before = backtrack(i - 1, j - 1)
                lcs_set = {
                    char_in_lcs_set + self.str1[i - 1] for char_in_lcs_set in lcs_set_before
                }
                return lcs_set

            lcs_set = set()
            if self.lcs_table[i - 1][j] >= self.lcs_table[i][j - 1]:
                lcs_set.update(backtrack(i - 1, j))
            if self.lcs_table[i][j - 1] >= self.lcs_table[i - 1][j]:
                lcs_set.update(backtrack(i, j - 1))

            return lcs_set

        # Get all LCSs by backtracking from self.lcs_table[m][n]
        str1_length = len(self.str1)
        str2_length = len(self.str2)
        all_lcs = backtrack(str1_length, str2_length)
        print(f'All of the longest common subsequences are {all_lcs}')


if __name__ == "__main__":
    lcs = LongestCommonSubsequence()
    lcs.read_input()
    lcs.solve()
    # lcs.print_lcs()
    lcs.print_all_lcs()
