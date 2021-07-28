"""
9. Palindrome Number
Given an integer, return a boolean indicating whether it is a palindrome or not
Difficulty :- Easy

https://leetcode.com/problems/palindrome-number/
Input: x = 121
Output: True

author:- aarifsk
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num == num[::-1]
