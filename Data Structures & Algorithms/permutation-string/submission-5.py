from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1_count = Counter(s1)
        window_count = Counter(s2[left:right])
        if s1_count == window_count:
            return True

        while right < len(s2):
            if s1_count == window_count:
                return True
            else:
                right += 1
                new_char = s2[right-1]
                window_count[new_char] += 1
                
                left += 1
                old_char = s2[right-1-len(s1)]
                window_count[old_char] -= 1
                if window_count[old_char] == 0:
                    del window_count[old_char]
                    
        if s1_count == window_count:
                return True
        return False