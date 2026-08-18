from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = (Counter(nums).most_common(k))
        result = []
        for i in x:
            result.append(i[0])
        return result
        