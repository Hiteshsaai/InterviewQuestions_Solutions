#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:49:05 2019

@author: hitesh
"""

import math 

#----- Sample Input --------

#       10
#      /  \
#     5    15
#     / \  / \
#    2   5 13 22
#    /      \
#    1       14 

# ------ Sample Output --------
#    13

class Solution():
     def findClosestValueInBst(self, tree, target):
         # Write your code here.
     	closest = math.inf
     	currentNode = tree
     	while currentNode is not None:
     		if abs(target - closest) > abs(target - currentNode.value):
     			closest = currentNode.value
     		if target > currentNode.value:
     			currentNode = currentNode.right
     		elif target < currentNode.value:
     			currentNode = currentNode.left 
     		else:
     			break
     	return closest
    
     
Solution.findClosestValueInBst(tree, target)