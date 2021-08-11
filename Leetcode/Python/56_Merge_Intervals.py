"""
56. Merge Intervals
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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) due to sorting, else O(n)
        merged_intervals = []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        temp_interval = intervals[0]
        for interval in intervals:
            if interval[0] <= temp_interval[1]:
                temp_interval = [min(temp_interval[0],interval[0]), max(temp_interval[1],interval[1])]
            else:
                merged_intervals.append(temp_interval)
                temp_interval = interval
        merged_intervals.append(temp_interval)
        return merged_intervals
