from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        result = []
        a = 0
        while a != k:
          result.append(list(sorted_d.keys())[a])
          a += 1
        return result
        