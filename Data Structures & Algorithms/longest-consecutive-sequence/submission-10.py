class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sort = set(nums)
        length = 0

        for i in nums:
            if not (i - 1) in nums_sort:
                long = 1
                while i + long in nums_sort:
                    long += 1
                    
                length = max(length,long) 

        return length       

