class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l_num = []
        for i in nums:
            diff = target - i
            if diff in l_num:
                if nums[nums.index(diff)] == nums[nums.index(i)]:
                   x1 = nums.index(diff)
                   nums[x1] = " "
                   x2 = nums.index(i)
                   return [x1,x2]
                else:
                    return [nums.index(diff),nums.index(i)]
            l_num.append(i)
