class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for pos, i in enumerate(nums):
            diff = target - i
            if diff in d:
                return [d[diff],pos]
            d[i] = pos