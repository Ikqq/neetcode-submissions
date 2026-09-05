from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count_most = Counter(nums).most_common(2)
        if len(nums) == 0:
            return False
        if nums_count_most[0][1] > 1:
            return True
        else:
            return False