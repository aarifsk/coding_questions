"""
997. Find the Town Judge

Difficulty:- Easy

https://leetcode.com/problems/find-the-town-judge/
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
Input: n = 3, trust = [[1,2],[2,3]]
Output: -1
author:- aarifsk
"""


from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        follows = defaultdict(int)
        followed_by = defaultdict(int)
        for trust_pair in trust:
            
            follows[trust_pair[0]] += 1
            followed_by[trust_pair[1]] += 1
        
        for i in range(1, n+1):
            if i not in follows and  followed_by[i] == n - 1 :
                return i
        return -1
