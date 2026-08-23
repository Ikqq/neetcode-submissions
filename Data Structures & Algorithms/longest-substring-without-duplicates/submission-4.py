class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_set = set()
        max_len = 0
        for r in range(0, len(s)):
            if not s[r] in hash_set:
                hash_set.add(s[r])
            else:
                while s[r] in hash_set:
                    hash_set.discard(s[l])
                    l += 1
                hash_set.add(s[r])
            max_len = max(max_len,r - l + 1)
        return max_len


