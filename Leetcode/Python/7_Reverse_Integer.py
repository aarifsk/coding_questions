"""
7. Reverse Integer
Given an integer, reverse it. Return 0 if the reversed value falls out of the range of [-2**31, 2**31 - 1]
Difficulty :- Easy

https://leetcode.com/problems/reverse-integer/
Input: x = 123
Output: 321

author:- aarifsk
"""

MAX_NUM = 2**31


class Solution:
    def reverse(self, x: int) -> int:
        negative = x != abs(x)
        string = "" + str(abs(x))
        ans = int(string[::-1])
        if negative and ans > MAX_NUM or ans >= MAX_NUM:
            return 0
        elif negative:
            ans = ans * -1
        return ans
