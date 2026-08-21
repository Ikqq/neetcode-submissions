class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for pos,i in enumerate(nums):
            if pos > 0 and i == nums[pos-1]:
                continue

            j = pos + 1
            k = len(nums) - 1

            while j < k:
                if i + nums[j] + nums[k] == 0:
                    res.append([i,nums[j],nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif i + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res