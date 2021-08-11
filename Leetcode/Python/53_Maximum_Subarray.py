"""
53. Maximum Subarray
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Difficulty:- Easy

https://leetcode.com/problems/maximum-subarray/
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

author:- aarifsk
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N^3), TLE
        max_sum = nums[0]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                temp_sum = 0
                for k in range(i, j+1):
                    temp_sum += nums[k]
                    max_sum = max(max_sum, temp_sum)
        return max_sum
    def maxSubArray(self, nums: List[int]) -> int:        
        # O(N^2), TLE
        max_sum = nums[0]
        
        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i,len(nums)):
                temp_sum += nums[j]
                max_sum = max(max_sum, temp_sum)
        return max_sum
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N), AC  
        max_sum = float('-inf')
        temp_sum = 0
        for i in range(len(nums)):
            temp_sum += nums[i]
            max_sum = max(max_sum, temp_sum)
            temp_sum = max(temp_sum,0)
        return max_sum