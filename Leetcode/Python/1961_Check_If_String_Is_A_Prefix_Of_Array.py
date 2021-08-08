"""
1961. Check if string is a prefix of array

Difficulty:- Easy

https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: True

author:- aarifsk
"""

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        length = len(words)
        current = ""
        for i in range(length):
            current += words[i]
            if not s.startswith(current):
                return False
            if s == current:
                return True
        return False
