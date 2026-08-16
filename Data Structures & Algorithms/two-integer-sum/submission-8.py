class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for pos, i in enumerate(nums):
            if target - i in d:
                return [d[target - i ],pos]
            d[i] = pos