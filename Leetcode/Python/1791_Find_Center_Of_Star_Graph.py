"""
1791. Find Center of Star Graph

Difficulty:- Easy

https://leetcode.com/problems/find-center-of-star-graph/
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
author:- aarifsk
"""


from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapping = defaultdict(int)
        for edge in edges:
            mapping[edge[0]] += 1
            mapping[edge[1]] += 1
        for key in mapping:
            if mapping[key] > 1:
                return key
