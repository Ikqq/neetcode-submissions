from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_window = len(s1)
        left = 0
        window = s2[left:length_window]
        count_window = Counter(window)
        count_s2 = Counter(s1)
        while length_window < len(s2):
                if count_window == count_s2:
                    return True

                length_window += 1
                count_window[s2[length_window-1]] += 1
                
                count_window[s2[left]] -= 1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1

        if count_window == count_s2:
            return True
        return False
        