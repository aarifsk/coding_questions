"""
1. Two Sum
Given array of integers nums and target integer,
return indices of two numbers whose sum is target.
Difficulty :- Easy

https://leetcode.com/problems/two-sum/
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

author:- sainiop
"""
class Solution:
    @staticmethod
    def twoSum(nums, target):
        target_comp = {}
        for idx, num in enumerate(nums):
            diff = target - num

            if num in target_comp:
                return [idx, target_comp[num]]
            else:
                target_comp[diff] = idx
