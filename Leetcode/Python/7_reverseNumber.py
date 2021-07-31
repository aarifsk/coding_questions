"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

"""


class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0

        if x < -2147483648 or x > 2147483647 or x == 0:
            return int("0")

        elif x > 0:
            while x > 0:
                remainder = x % 10
                x = x // 10

                reversed = remainder + reversed * 10
            if reversed < -2147483648 or reversed > 2147483647:
                return int("0")
            return reversed

        elif x < 0:
            x = -x
            while x > 0:
                remainder = x % 10
                x = x // 10

                reversed = remainder + reversed * 10
            if reversed < -2147483648 or reversed > 2147483647:
                return int("0")
            return -reversed
