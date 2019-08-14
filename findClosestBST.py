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

# Average time complexity is O(log n) || Average Space complexity is O(log n)
# Worst time complexity is O(n) || Worst Space complexity is O(n)

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
