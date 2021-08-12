"""
89. Gray Code
An n bit gray code is a sequence of binary numbers differing by a single bit
It has 2**n entries starting from 0.
The first and the last entry also differ by a single bit

Difficulty:- Medium

https://leetcode.com/problems/gray-code/
Input: n = 2
Output: [0, 1, 3, 2]

Necessary theory:-
^ = Bitwise XOR operator
>> = Bitwise right shift operator
author:- aarifsk
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        answer = []
        for idx in range(2**n):
            answer.append(idx ^ (idx >> 1))
        return answer
