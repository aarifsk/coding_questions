#!/bin/bash
# https://leetcode.com/problems/valid-phone-numbers/
# given a file that contains phone numbers, print if valid
# valid formats :- (xxx) xxx-xxxx or xxx-xxx-xxxx where x is a digit
# Difficulty:- Easy
# Input :- Assume that file.txt has the following content 
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# Output :- 
# 987-123-4567
# (123) 456-7890
# author:- aarifsk
egrep  "^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$" file.txt