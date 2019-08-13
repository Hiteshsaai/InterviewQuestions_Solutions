"""
Created on Sat Aug  3 21:13:57 2019

@author: hitesh
"""     

# -------------- Two Sum -----------------------------------

# Sample Input 
arr = [3, 5,-4, 8, 11, 1, -1, 6]
t = 10


# Both the solution works on o(n) time  || o(n) Space
class Solution:
     def twoNumberSum(self, array, targetSum):
         result = []
         for i in range(len(array)):
              if i == len(array)-1:
                   break
              if targetSum - array[i] in array[i+1:]:
                   result.append(targetSum - array[i])
                   result.append(array[i])
         return sorted(result)
     

     def twoNumberSum2(self,array, targetSum):
         dict_val = {}
         for i in array:
              if targetSum - i in dict_val:
                   return sorted([targetSum - i, i])
              dict_val[i] = True
         return []
     
Solution().twoNumberSum2(arr,t)
Solution().twoNumberSum(arr, t)



