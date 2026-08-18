class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sort_i = "".join(sorted(i))
            if sort_i not in d.keys():
              d[sort_i] = [i]
            else:
              d[sort_i].append(i)
        return list(d.values())
