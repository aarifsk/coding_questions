"""
1929. Concatenation of Array
Given an integer array nums of length n, 
you want to create an array ans of length 2n where ans[i] == nums[i] 
and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
Difficulty:- Easy

https://leetcode.com/problems/concatenation-of-array/
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

author:- aarifsk
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * 2 * size
        for _ in range(size):
            ans[_] = ans[size + _]  = nums[_]
        return ans
       