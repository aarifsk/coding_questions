"""
1281. Subtract the Product and Sum of Digits of an Integer

Difficulty:- Easy

https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Input: n = 234
Output: 15 

author:- aarifsk
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_as_str = str(n)
        prod = 1
        sums = 0
        for _ in num_as_str:
            _ = int(_)
            prod *= _
            sums += _
        return prod - sums
