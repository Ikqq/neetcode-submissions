import math as m
from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy_nums = nums[:]
        result = []
        x = Counter(nums)
        product1 = m.prod(nums)
        
        if product1 == 0: 
            if x[0] > 1:
                return [0]*len(nums)
            else:
                for i in copy_nums:
                    if i == 0:
                        nums.remove(0)
                        product2 = m.prod(nums)
                        result.append(product2)
                    else:
                        result.append(0)
        else:
            for i in nums: #O(n)              
                result.append(product1// i)
        return result

            

            
