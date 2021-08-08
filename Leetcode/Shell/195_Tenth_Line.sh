#!/bin/bash
# https://leetcode.com/problems/tenth-line/
# given a file, print tenth line
# Difficulty:- Easy
# Input :- Assume that file.txt has the following content 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Output :- Line 10
# author:- aarifsk
cat file.txt | awk 'NR==10'

# Alternative solutions :-
# head -n 10 file.txt | tail -n +10
# cat file.txt | sed -n '10p'
# cat file.txt | sed '10!d'