'''
Given array of integers nums and target integer,
return indices of two numbers whose sum is target.

example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            #curr: ith index element in array
            curr = nums[i]

            #diff: target and ith index element difference
            diff = target - nums[i]

            if curr in dict:
                return (i, dict[curr])
            else:
                dict[diff] = i