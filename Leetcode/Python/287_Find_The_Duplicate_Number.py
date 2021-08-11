"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses 
only constant extra space.

Difficulty:- Medium

https://leetcode.com/problems/find-the-duplicate-number/
Input: nums = [1,3,4,2,2]
Output: 2

author:- aarifsk
"""

from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N), O(N), uses extra space
        count = defaultdict(int)
        for _ in range(len(nums)):
            count[nums[_]] += 1
            if count[nums[_]] >1:
                return nums[_]
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N), O(1)
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
    