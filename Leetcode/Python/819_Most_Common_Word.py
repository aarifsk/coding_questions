"""
819. Most Common Word

Difficulty:- Easy

https://leetcode.com/problems/most-common-word/
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
(Contains "!?',;.")
author:- aarifsk
"""

import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for _ in paragraph:
            if _ in "!?',;.":
                paragraph = paragraph.replace(_," ")
        words = paragraph.split()
        
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]
