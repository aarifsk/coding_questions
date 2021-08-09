"""
3. Longest Substring Without Repeating Characters

Difficulty:- Medium

https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3

author:- aarifsk
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest_substr = 0
        window = set()
        while j <= len(s):
            if s[j] not in window:
                window.add(s[j])
                longest_substr = max(j - i + 1, longest_substr)
                j+=1
            else:
                window.remove(s[i])
                i += 1
        return longest_substr
