from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1_count = Counter(s1)
        while right <= len(s2):
            window_count = Counter(s2[left:right])
            if s1_count == window_count:
                return True
            left += 1
            right += 1
        return False