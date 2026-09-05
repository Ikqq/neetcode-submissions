from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sort_i = "".join(sorted(i))
            d[sort_i].append(i)
        return list(d.values())