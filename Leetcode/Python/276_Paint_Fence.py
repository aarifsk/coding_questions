"""
276. Paint Fence

Difficulty:- Medium

https://leetcode.com/problems/paint-fence/
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.
Input: n = 7, k = 2
Output: 42

author:- aarifsk
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k == 0 or n == 0:
            return 0
        if n == 1:
            return k

        same = k # possible colors
        diff = k * (k - 1) # one less choice for possible colors
        for _ in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff
