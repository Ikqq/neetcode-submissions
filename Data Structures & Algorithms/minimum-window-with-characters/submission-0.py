class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        countT = Counter(t)
        res = [-1, -1]
        res_len = float("inf")
        left = 0
        need = len(countT)
        have = 0
        window_count = defaultdict(int)
        if len(s) < len(t):
            return ""
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1
            
            if char in countT and window_count[char] == countT[char]:
                have += 1
            
            while have == need:
                
                if right - left + 1 < res_len:
                    res = [left,right]
                    res_len = right - left + 1
                    
                left_char = s[left]
                window_count[left_char] -= 1
                
                if s[left] in countT and window_count[left_char] < countT[left_char]:
                    have -= 1
                    
                left += 1
                
        l,r = res
        if res_len != float("inf"):
            return s[l : r+1]
        else:
            return ""
                  