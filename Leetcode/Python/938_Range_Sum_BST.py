"""
938. Range Sum of BST

Difficulty:- Easy

https://leetcode.com/problems/range-sum-of-bst/
Given a tree and a low,high range, find sum of all nodes that have
values between the range
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

author:- aarifsk
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root, values, high, low):
        if root is None:
            return
        if low<=root.val<=high:
            values.append(root.val)
        self.traversal(root.left,values,high, low)
        self.traversal(root.right, values, high, low)
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        values = []
        self.traversal(root,values,high,low)
        return sum(values)