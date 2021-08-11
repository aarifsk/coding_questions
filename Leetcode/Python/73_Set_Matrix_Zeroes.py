"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's, and return the matrix.

You must do it in place.

Difficulty:- Medium

https://leetcode.com/problems/set-matrix-zeroes/
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

author:- aarifsk
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        firstrows, firstcols = False, False
        
        
        for row in range(rows):
            if matrix[row][0] == 0:
                firstcols = True
        for col in range(cols):
            if matrix[0][col] ==0:
                firstrows = True
        for row in range(rows):
            for col in range(1,cols):
                if not matrix[row][col]:
                    matrix[row][0] = 0
        for row in range(1,rows):
            for col in range(1, cols):
                if not matrix[row][col]:
                    matrix[0][col] = 0
        for row in range(1, rows):
            if matrix[row][0] == 0:
                matrix[row] = [0]*cols
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for i in range(1,rows):
                    matrix[i][col] = 0
        if firstrows:
            matrix[0] = [0] * cols
        if firstcols:
            for i in range(rows):
                matrix[i][0] = 0
        return matrix
