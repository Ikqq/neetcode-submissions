class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        res = []
        for i in nums_sort:
            target = -i
            nums_sort_jk = nums_sort[:]
            nums_sort_jk.remove(i)
            j = 0
            k = len(nums_sort_jk) - 1
            while j < k:
                if nums_sort_jk[j] + nums_sort_jk[k] < target:
                    j += 1
                elif nums_sort_jk[j] + nums_sort_jk[k] > target:
                    k -= 1
                elif nums_sort_jk[j] + nums_sort_jk[k] == target:
                    res.append([nums_sort_jk[j],nums_sort_jk[k],i])
                    j += 1
        ans = []
        for a in res:
            x = sorted(a)
            if not x in ans:
                ans.append(x)
        
        return ans