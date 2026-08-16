class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        for i in set_s:
            if s.count(i) != t.count(i) or len(s) != len(t):
                return False
        return True