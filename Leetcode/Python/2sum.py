"""
1. Two Sum
Difficulty :- Easy

https://leetcode.com/problems/two-sum/
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

author:- aarifsk
"""


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def two_sum(nums, target):
        answer = []
        target_info = {}
        for index, num in enumerate(nums):
            target_info[num] = index
        for index, num in enumerate(nums):
            if target - num in target_info.keys():
                if index == target_info[target - num]:
                    continue
                answer.append(index)
                answer.append(target_info[target - num])
                break
        return answer


print(Solution.two_sum([2, 7, 11, 15], 9))
