"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

Difficulty:- Easy

https://leetcode.com/problems/pascals-triangle/
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

author:- aarifsk
"""

import math
class Solution:
    def __init__(self):
        self.pascal_value = {0:1,1:1, 2:2}
    def get_pascal_value(self, row, col):
        
        if row+1 in self.pascal_value:
            nfact = self.pascal_value[row+1]
        else:
            self.pascal_value[row+1] =nfact = math.factorial(row+1)
        if col+1 in self.pascal_value:
            rfact = self.pascal_value[col+1]
        else:
            self.pascal_value[col+1]=rfact = math.factorial(col+1)
        if abs(row-col) in self.pascal_value:
            nminrfact = self.pascal_value[row-col]
        else:
            self.pascal_value[row-col]=nminrfact = math.factorial(row-col)
        
        return int(nfact/(rfact*nminrfact))
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            temp = []
            for col in range(row + 1):
                temp.append(self.get_pascal_value(row-1,col-1))
            ans.append(temp)
        return ans
        