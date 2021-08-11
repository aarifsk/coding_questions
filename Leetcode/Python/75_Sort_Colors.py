"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.
You must solve this problem without using the library's sort function.

Difficulty:- Medium

https://leetcode.com/problems/sort-colors/
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

author:- aarifsk
"""

from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        O(2n), O(1)
        """
        mapping = defaultdict(int)
        for _ in nums:
            mapping[_] += 1
        index = 0
        for _ in range(3):
            counts = mapping[_]
            for i in range(counts):
                nums[index] = _
                index += 1
    
    def sortColors(self, nums: List[int]) -> None:
        """
        O(N), O(1)
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while(mid <= high ):
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
